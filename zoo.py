from pywebio.input import input as pw_input, NUMBER
from pywebio.output import put_text, put_error, put_success

total_price = 0
discount_6_12 = 0.50
discount_12_17 = 0.25
discount_18_60 = 0.30
discount_6 = 1
price = 100

enter_your_age = pw_input(label='Введіть свій вік', type=NUMBER, min = 1)
#enter_your_age = int(enter_your_age)

if enter_your_age < 0:
    put_error('Ваш вік не може бути мінусовим.')
    exit()
elif enter_your_age <= 6:
    total_price += price - price * discount_6
    put_success(f'Вартість вашого квитка {total_price} грн (знижка = {price - total_price} гривень!')
elif enter_your_age <= 12:
    total_price += price - price * discount_6_12
    put_success(f'Вартість вашого квитка {total_price} грн (знижка = {price - total_price} гривень!).')
elif enter_your_age <= 17:
    total_price += price - price * discount_12_17
    put_success(f'Вартість вашого квитка {total_price} грн (знижка = {price - total_price} гривень!).')
elif enter_your_age <= 59:
    total_price += price - price * discount_18_60
    put_success(f'Вартість вашого квитка {total_price} грн (знижка = {price - total_price} гривень!')
else:
    total_price += price - price * discount_18_60
    put_success(f'Вартість вашого квитка {total_price} грн (знижка = {price - total_price} гривень!).')
