"""Various validators"""

def validate_integers(
        arg_name, arg_value, min_value=None, max_value=None,
        custom_min_message=None, custom_max_message=None
):
    """Validates that arg_value is an integer and optionally falls within bounds.
    A custom override error message can be provided 

    Args:
        arg_name(str): the name of arg.
        arg_value.... 
        some more documentaion.

    Returns:
        None: no exceptions raised if validation passes

    Raises:
        TypeError: if arg_value is not an integer
        ValueError: if arg_value does not satisfy bounds
    """

    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} must be an integer.")

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_value} cannot be less than {min_value}')
    
    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_value} cannot be greater than {max_value}')
    
    