def format_money(value):
    return f'R${value:>.2f}'.replace('.', ',')

def summary(value, xp, xm, f):
    print()
    print("Value Summary")
    print()
    print(f'Analyzed Price: {format_money(value)}')
    print(f'Double Price: {double(value, f)}')
    print(f'Half Price: {half(value, f)}')
    print(f'Increasing {format_money(xp)}: {increase(value, xp, f)}')
    print(f'Decreasing {format_money(xm)}: {decrease(value, xm, f)}')
    
def increase(value, x, f):
    c = value + x
    return c if not f else format_money(c)

def decrease(value, x, f):
    c = value - x
    
    if c < 0:
        c = 0
    
    return c if not f else format_money(c)

def double(value, f):
    c = value * 2
    return c if not f else format_money(c)

def half(value, f):
    c = value / 2
    return c if not f else format_money(c)
