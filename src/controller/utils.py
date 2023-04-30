import ast

def str_to_list_int(input: str)-> int:
    try:
        res = ast.literal_eval(input)
        return res
    except:
        return -1