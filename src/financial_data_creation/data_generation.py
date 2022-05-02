import inspect

from financial_data_creation import fundamental_indicators_formulas


# validation
def validate_availability(data):
    return True if data else False


def validate_input_data(financial_indicator_name_and_value_mapping):
    validated_financial_indicator_name_and_value_mapping, invalidated_financial_indicator_name_and_value_mapping = dict(), dict()
    for financial_name, financial_value in financial_indicator_name_and_value_mapping.items():
        if not type(financial_value) in (int, float):
            print(f"{financial_value} is not int or float")
            invalidated_financial_indicator_name_and_value_mapping.update({financial_name: financial_value})
        else:
            validated_financial_indicator_name_and_value_mapping.update({financial_name: financial_value})
    return validated_financial_indicator_name_and_value_mapping, invalidated_financial_indicator_name_and_value_mapping


def exception_handling_division_by_zero(function, **kwargs):
    try:
        return function(**kwargs)
    except ZeroDivisionError:
        return None


class ModuleFunctions:
    def __init__(self, module, input_data=None):

        self.module = module
        self.data = validate_input_data(input_data)[0] if input_data else None

    # Parameters related
    def get_list_of_tuples_of_functions_name_and_function_object(self):
        return inspect.getmembers(self.module, inspect.isfunction)

    def function_names_set(self):
        list_of_tuples_of_functions_name_and_function_object = self.get_list_of_tuples_of_functions_name_and_function_object()
        function_name_set = set()

        for tuples_of_functions_name_and_function_object in list_of_tuples_of_functions_name_and_function_object:
            function_name = tuples_of_functions_name_and_function_object[0]
            function_name_set.add(function_name)

        return function_name_set

    def parameter_set(self):
        list_of_tuples_of_functions_name_and_function_object = self.get_list_of_tuples_of_functions_name_and_function_object()
        parameters_set = set()

        for tuples_of_functions_name_and_function_object in list_of_tuples_of_functions_name_and_function_object:
            for parameter_name in tuples_of_functions_name_and_function_object[1].__code__.co_varnames:
                parameters_set.add(parameter_name)

        return parameters_set

    def create_function_parameter_mapping(self):
        """Future features: this will create mapping based on all, profitability, liquidity, efficiency ratios

        Returns
        -------

        """

        list_of_tuples_of_functions_name_and_function_object = self.get_list_of_tuples_of_functions_name_and_function_object()
        function_parameter_mapping = dict()

        for function in list_of_tuples_of_functions_name_and_function_object:
            argument_counts = function[1].__code__.co_argcount if function[1].__code__.co_argcount else 0
            default_counts = len(function[1].__defaults__) if function[1].__defaults__ else 0
            non_default_count = argument_counts - default_counts
            parameter_list = [function[1].__code__.co_varnames[:non_default_count],
                              function[1].__code__.co_varnames[non_default_count:]]
            function_parameter_mapping[function[0]] = parameter_list

        return function_parameter_mapping

    def function_name_string_function_object_mapping(self):
        name_and_function_dict = dict()
        list_of_tuples_of_functions_name_and_function_object = self.get_list_of_tuples_of_functions_name_and_function_object()
        for function_detail in list_of_tuples_of_functions_name_and_function_object:
            name_and_function_dict[function_detail[0]] = function_detail[1]

        return name_and_function_dict

    def get_formula_based_on_name_string(self, formula_name):
        return self.function_name_string_function_object_mapping()[formula_name]

    def formula_executor(self, formula_name, data):

        function_and_parameters = self.create_function_parameter_mapping()
        parameters = ParameterMatcher(data, function_and_parameters[formula_name]).parameter()

        variable_value = exception_handling_division_by_zero(self.get_formula_based_on_name_string(formula_name),
                                                             **parameters)
        if not variable_value:
            return None
        variable_name = f"{formula_name}_value"

        return {variable_name: variable_value}

    def data_generator(self):
        """Future features: this will create mapping based on all, profitability, liquidity, efficiency ratios

        Returns
        -------

        """
        data = self.data
        function_parameter_dict = self.create_function_parameter_mapping()

        while True:
            formulas_tried = 0
            for formula_name, parameters in function_parameter_dict.items():

                if ParameterMatcher(data, parameters).status():
                    generated_name_value = self.formula_executor(formula_name, data)
                    if not generated_name_value:
                        formulas_tried += 1
                        continue
                    data.update(generated_name_value)
                    del function_parameter_dict[formula_name]
                    break
                formulas_tried += 1

            if formulas_tried == len(function_parameter_dict):
                return data


def membership_checker(item, data_structure):
    return True if item in data_structure else False


class ParameterMatcher:
    def __init__(self, data, parameters):
        self.parameters = parameters
        self.data = data

    def status(self, default_parameters_check=True):

        if default_parameters_check:
            for default_variable in self.parameters[1]:
                if not membership_checker(default_variable, self.data):
                    print(
                        f"{default_variable} is not provided, data_generator will use default value in formula function")

        for var in self.parameters[0]:
            if not membership_checker(var, self.data):
                return False

        return True

    def parameter(self):
        parameters_dict = dict()

        for var in self.parameters[0]:
            if membership_checker(var, self.data):
                parameters_dict[var] = self.data[var]

        for default_variable in self.parameters[1]:
            if membership_checker(default_variable, self.data):
                parameters_dict[default_variable] = self.data[default_variable]
        return parameters_dict


class DataCreation:
    def __init__(self, input_data=None, type_of_data="fundamental_data"):
        self.type_of_data = type_of_data
        self.input_data = input_data

    def generate(self):
        if self.type_of_data.lower() == "fundamental_data":
            return ModuleFunctions(fundamental_indicators_formulas, self.input_data).data_generator()

    def function_names_set(self):
        if self.type_of_data.lower() == "fundamental_data":
            return ModuleFunctions(fundamental_indicators_formulas).function_names_set()

    def parameter_set(self):
        if self.type_of_data.lower() == "fundamental_data":
            return ModuleFunctions(fundamental_indicators_formulas).parameter_set()


if __name__ == "__main__":
    pass
