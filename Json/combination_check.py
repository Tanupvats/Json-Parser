from functools import reduce
from checker import  null_checker
from checker import number_checker
from checker import bool_checker


from checker import colon_checker
from checker import comma_checker
from checker import string_checker


###########------------------------------checking dictionary and array-------------------------------##############

def dict_checker(pass_data):
    """
    :param pass_data:
    :return:
    """
    if pass_data[0] != "{":
        return None
    data_in_dict = {}
    pass_data = pass_data[1:].strip()
    while pass_data[0] != "}":
        residual = string_checker(pass_data)
        if residual is None:
            return None
        key = residual[0]
        residual = colon_checker(residual[1].strip())
        if residual is None:
            return None
        residual = comb_check(residual[1].strip())
        if residual is None:
            return None
        data_in_dict[key] = residual[0]
        pass_data = residual[1].lstrip()
        residual = comma_checker(pass_data)
        if residual:
            pass_data = residual[1].strip()
    return [data_in_dict, pass_data[1:]]

def array_checker(pass_data):
    """
    :param pass_data:
    :return:
    """
    if pass_data[0] != "[":
        return None
    data_in_list = []
    pass_data = pass_data[1:].strip()
    while len(pass_data):
        residual = comb_check(pass_data)
        if residual is None:
            return None
        data_in_list.append(residual[0])
        pass_data = residual[1].strip()
        if pass_data[0] == "]":
            return [data_in_list, pass_data[1:].strip()]
        residual = comma_checker(pass_data)
        if residual is None:
            return None
        pass_data = residual[1].strip()


def possible_combo(*parms):
    """
    :param parms:
    :return:dict
    """
    return lambda data: (reduce(lambda a, b: a if a(data) else b, parms)(data))

comb_check=possible_combo(null_checker,number_checker,bool_checker,string_checker,dict_checker,array_checker)