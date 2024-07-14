def list_to_dict(input_list):
    '''
    This function returns a dictionary where each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`.
    '''
    return {index: value for index, value in enumerate(input_list)}





