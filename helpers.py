def get_input(path: str = './input.txt') -> list[str]:
    """Parses input to list of strings.

    Args:
        path (str): path for input file

    Returns:
        list[str]: contents of file as list of str, without newline characters
    """
    with open(path) as file:
        return file.read().splitlines()
