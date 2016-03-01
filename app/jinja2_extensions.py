def rounding(val):
    if val < 1000:
        return val
    else:
        val = str(val / 100)
        return val[:-1] + '.' + val[-1] + 'k'

user_functions = {'rounding': rounding}
