def str_to_list_int(input: str)-> list[int]:
    import ast
    try:
        res = ast.literal_eval(input)
        return res
    except:
        return -1
    
def convert_date_format(date):
    import datetime

    return date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
