def temp_advisory(temp, unit='C', threshold=35):
    """
    temp: numeric temperature
    unit: 'C' or 'F', default 'C'
    threshold: threshold in the opposite unit
    """
    unit = unit.upper()
    if unit == 'C':
        converted = (temp * 9/5) + 32  # C -> F
    elif unit == 'F':
        converted = (temp - 32) * 5/9  # F -> C
    else:
        raise ValueError("Unit must be 'C' or 'F'")

    if converted < threshold:
        return "Cold advisory"
    else:
        return "Heat alert"
