import ast

def str_to_list_int(input: str)-> int:
    try:
        res = ast.literal_eval(input)
        res = [n.strip() for n in res]
        return res
    except:
        return -1