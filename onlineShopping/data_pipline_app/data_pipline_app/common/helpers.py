mapping = dict()


def set_handler_mapping(operation):
    """
    Creates mapping for the operations to be carried out

    :param operation: Operation to be carried out
    :return: Function
    """

    def wrapper(func):
        """
        Maps operation name to the Function

        :param func: Function
        :return: Mapping
        """
        mapping[operation] = func
        return func

    return wrapper
