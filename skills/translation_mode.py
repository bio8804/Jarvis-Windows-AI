CURRENT_MODE = 'general'


def set_mode(mode):
    global CURRENT_MODE
    CURRENT_MODE = mode


def get_mode():
    return CURRENT_MODE
