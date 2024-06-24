from Modules import Controls, Validations

n = Validations.validate_money("Money: R$")
fn = float(n)

increase_x = float(input("Increase: R$"))
decrease_x = float(input("Decrease: R$"))
want_format = input("What you do want formated? [y/n]: ").lower()

bl = False

if want_format in 'yn':
    if want_format == 'y':
        bl = True
    else:
        bl = False

Controls.summary(fn, increase_x, decrease_x, bl)