output_data = dict()

import inspect

from financial_data_creation import fundamental_indicators_formulas as formulas


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


# Division by zero
def exception_handling_division_by_zero(function):
    try:
        return function()
    except ZeroDivisionError:
        return None


# Parameters related
def get_functions_name_and_details(module):
    return inspect.getmembers(module, inspect.isfunction)


def create_function_parameter_mapping(module):

    functions_name_and_details = get_functions_name_and_details(module)
    function_parameter_mapping = dict()

    for function in functions_name_and_details:
        argument_counts = function[1].__code__.co_argcount if function[1].__code__.co_argcount else 0
        default_counts = len(function[1].__defaults__) if function[1].__defaults__ else 0
        non_default_count = argument_counts - default_counts
        parameter_list = [function[1].__code__.co_varnames[:non_default_count],
                          function[1].__code__.co_varnames[non_default_count:]]
        function_parameter_mapping[function[0]] = parameter_list

    return function_parameter_mapping


def function_name_string_function_object_mapping(module):
    name_and_function_dict = dict()
    functions_name_and_details = get_functions_name_and_details(module)
    for function_detail in functions_name_and_details:
        name_and_function_dict[function_detail[0]] = function_detail[1]

    return name_and_function_dict


def get_formula_based_on_name_string(formula_name, module):
    return get_functions_name_and_details(module)[formula_name]


def membership_checker(item, data_structure):
    return True if item in data_structure else False


def input_data_parameters_matcher(data, parameters, default_parameters_check=True):

    for variable in parameters:
        if default_parameters_check:
            for default_variable in variable[1]:
                if not membership_checker(default_variable, data):
                    print(f"{default_variable} is not provided, data_generator will use default value in formula function")

        for var in variable[0]:
            if not membership_checker(var, data):
                return False

    return True


def run_formula(formula, input_data):
    return formula(input_data)


def data_update():
    pass


# Indicators Generator
def remove_entry_from_function_parameter_mapping_data():
    pass


def formula_executor(formula_name, data, functions_name_and_details):


    return {variable_name: variable_value}


def data_generator(input_data, function_parameter_mapping_data):
    data = input_data

    while True:
        formulas_tried = 0
        for formula_name, parameters in function_parameter_mapping_data.items():

            update_flag = False
            if input_data_parameters_matcher(data, parameters):
                generated_name_value = formula_executor(formula_name, data)
                update_flag = data_update(data, generated_name_value)
                remove_entry_from_function_parameter_mapping_data()
            if update_flag:
                break
            formulas_tried += 1

        if formulas_tried == len(function_parameter_mapping_data):
            return data


# Look out observer and parameter cache


if __name__ == '__main__':
    pass
