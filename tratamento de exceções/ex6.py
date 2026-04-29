def divisao_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None