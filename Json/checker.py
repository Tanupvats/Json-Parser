import re
########---------------------------check system------------------------------#######
def string_checker(new_data):
    """
    :param new_data:
    :return: list
    """
    if new_data[0]== '"':
        new_data= new_data[1:].strip()
        ind=new_data.find('"')
        return [new_data[:ind], new_data[ind + 1:].strip()]

def colon_checker(new_data):
    """
    :param new_data:
    :return: list
    """
    if new_data[0] == ":":
        return [new_data[0], new_data[1:].lstrip()]

def comma_checker(new_data):
    """
    :param new_data:
    :return: list
    """
    if new_data and new_data[0] == ",":
        return [new_data[0], new_data[1:].strip()]

def bool_checker(new_data):
    """
    :param new_data:
    :return: list
    """
    if new_data[0:4] == "true":
        return [True, new_data[4:].strip()]
    elif new_data[0:5] == "false":
        return [False, new_data[5:].strip()]

def null_checker(new_data):
    """
    :param new_data:
    :return: list
    """
    if new_data[0:4] == "null":
        return [None, new_data[4:].strip()]

def number_checker(new_data):
    """
    :param new_data:
    :return:list
    """
    regular_exp_occ = re.findall("^(-?(?:[0-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)",
                                 new_data)
    if not regular_exp_occ:
        return None
    ind = len(regular_exp_occ[0])
    try:
        return [int(regular_exp_occ[0]), new_data[ind:].strip()]
    except ValueError:
        return [float(regular_exp_occ[0]), new_data[ind:].strip()]

