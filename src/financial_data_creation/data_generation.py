"""Utilities for generating derived financial indicators from raw inputs."""

from __future__ import annotations

import inspect
from numbers import Real

from financial_data_creation import fundamental_indicators_formulas


def validate_availability(data):
    """Return True when input data is present."""

    return bool(data)


def validate_input_data(financial_indicator_name_and_value_mapping):
    """Split input values into numeric and non-numeric mappings."""

    validated_financial_indicator_name_and_value_mapping = {}
    invalidated_financial_indicator_name_and_value_mapping = {}

    for financial_name, financial_value in financial_indicator_name_and_value_mapping.items():
        if isinstance(financial_value, bool) or not isinstance(financial_value, Real):
            invalidated_financial_indicator_name_and_value_mapping[financial_name] = financial_value
        else:
            validated_financial_indicator_name_and_value_mapping[financial_name] = financial_value

    return (
        validated_financial_indicator_name_and_value_mapping,
        invalidated_financial_indicator_name_and_value_mapping,
    )


def exception_handling_division_by_zero(function, **kwargs):
    """Return ``None`` when a ratio cannot be computed because of division by zero."""

    try:
        return function(**kwargs)
    except ZeroDivisionError:
        return None


class ModuleFunctions:
    """Inspect formula modules and generate indicators from available inputs."""

    def __init__(self, module, input_data=None):
        self.module = module
        self.data = validate_input_data(input_data)[0] if input_data else {}

    def get_list_of_tuples_of_functions_name_and_function_object(self):
        return inspect.getmembers(self.module, inspect.isfunction)

    def function_names_set(self):
        return {
            function_name
            for function_name, _function_object in self.get_list_of_tuples_of_functions_name_and_function_object()
        }

    def parameter_set(self):
        parameters_set = set()
        for _function_name, function_object in self.get_list_of_tuples_of_functions_name_and_function_object():
            signature = inspect.signature(function_object)
            parameters_set.update(signature.parameters.keys())
        return parameters_set

    def create_function_parameter_mapping(self):
        """Map each formula to its required and optional parameters."""

        function_parameter_mapping = {}

        for function_name, function_object in self.get_list_of_tuples_of_functions_name_and_function_object():
            required_parameters = []
            optional_parameters = []

            for parameter_name, parameter in inspect.signature(function_object).parameters.items():
                if parameter.default is inspect._empty:
                    required_parameters.append(parameter_name)
                else:
                    optional_parameters.append(parameter_name)

            function_parameter_mapping[function_name] = [tuple(required_parameters), tuple(optional_parameters)]

        return function_parameter_mapping

    def function_name_string_function_object_mapping(self):
        return {
            function_name: function_object
            for function_name, function_object in self.get_list_of_tuples_of_functions_name_and_function_object()
        }

    def get_formula_based_on_name_string(self, formula_name):
        return self.function_name_string_function_object_mapping()[formula_name]

    def formula_executor(self, formula_name, data):
        function_and_parameters = self.create_function_parameter_mapping()
        parameters = ParameterMatcher(data, function_and_parameters[formula_name]).parameter()

        variable_value = exception_handling_division_by_zero(
            self.get_formula_based_on_name_string(formula_name),
            **parameters,
        )
        if variable_value is None:
            return None

        variable_name = f"{formula_name}_value"
        return {variable_name: variable_value}

    def data_generator(self):
        """Iteratively generate every formula that can be derived from the available inputs."""

        data = dict(self.data)
        function_parameter_dict = self.create_function_parameter_mapping()

        while function_parameter_dict:
            progress_made = False

            for formula_name, parameters in list(function_parameter_dict.items()):
                if not ParameterMatcher(data, parameters).status():
                    continue

                generated_name_value = self.formula_executor(formula_name, data)
                del function_parameter_dict[formula_name]

                if generated_name_value is None:
                    continue

                data.update(generated_name_value)
                progress_made = True

            if not progress_made:
                break

        return data


def membership_checker(item, data_structure):
    return item in data_structure


class ParameterMatcher:
    def __init__(self, data, parameters):
        self.parameters = parameters
        self.data = data

    def status(self, default_parameters_check=True):
        """Return True when every required parameter is available."""

        del default_parameters_check
        return all(membership_checker(var, self.data) for var in self.parameters[0])

    def parameter(self):
        parameters_dict = {}

        for var in self.parameters[0]:
            if membership_checker(var, self.data):
                parameters_dict[var] = self.data[var]

        for default_variable in self.parameters[1]:
            if membership_checker(default_variable, self.data):
                parameters_dict[default_variable] = self.data[default_variable]

        return parameters_dict


class DataCreation:
    """Public API for deriving fundamental indicators from raw statement values."""

    def __init__(self, input_data=None, type_of_data="fundamental_data"):
        self.type_of_data = type_of_data.lower()
        self.input_data = input_data or {}

    def _module_functions(self):
        if self.type_of_data == "fundamental_data":
            return ModuleFunctions(fundamental_indicators_formulas, self.input_data)
        raise ValueError(f"Unsupported type_of_data: {self.type_of_data}")

    def generate(self):
        return self._module_functions().data_generator()

    def function_names_set(self):
        return self._module_functions().function_names_set()

    def parameter_set(self):
        return self._module_functions().parameter_set()


def convert_to_average_stock_prices(bse_stockprice, time_column_name="Bmonth_Month End"):
    """Aggregate monthly stock-price data into yearly company-level averages."""

    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError(
            "pandas is required to use convert_to_average_stock_prices."
        ) from exc

    cleaned_stockprice = bse_stockprice.copy()
    cleaned_stockprice.dropna(how="all", axis=1, inplace=True)

    totalyears = len(cleaned_stockprice[time_column_name].unique()) // 12
    yearlist = []
    number = 202103.0
    for _index in range(totalyears):
        yearlist.append(number)
        number -= 100

    filtered_numeric_columns = [
        "Bmonth_Open",
        "Bmonth_High",
        "Bmonth_Low",
        "Bmonth_Close",
        "Bmonth_Volume ('000)",
        "Bmonth_Value",
    ]
    average_stock_price_columns = [f"avg__{column_name}" for column_name in filtered_numeric_columns]
    average_stock_price_columns = [
        "Accord Code",
        "Company Name",
        "Bmonth_Month End",
        *average_stock_price_columns,
    ]

    company_names = list(cleaned_stockprice["Company Name"].unique())
    data = []

    for company in company_names:
        for index in range(totalyears - 1):
            filtered = cleaned_stockprice.loc[
                (cleaned_stockprice["Company Name"] == company)
                & (cleaned_stockprice["Bmonth_Month End"] < yearlist[index])
                & (cleaned_stockprice["Bmonth_Month End"] >= yearlist[index + 1])
            ]

            if filtered.empty:
                continue

            values = [filtered["Accord Code"].values[0], company, yearlist[index]]
            for numeric_column in filtered_numeric_columns:
                values.append(filtered[numeric_column].mean())
            data.append(dict(zip(average_stock_price_columns, values)))

    return pd.DataFrame(data)

