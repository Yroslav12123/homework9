from pywebio.input import input as pw_input
from pywebio.output import put_text, put_error, put_success

total_price = 0
discount_50 = 0.50
discount_25 = 0.25
discount_30 = 0.30
price_1 = 50
price_2 = 75
price_3 = 70

enter_your_age = pw_input(label='Введіть свій вік')
enter_your_age = int(enter_your_age)

if enter_your_age < 0:
    put_error('Ваш вік не може бути мінусовим.')
elif enter_your_age <= 6:
    put_success('Вартість вашого квитка безкоштовно!!')
elif enter_your_age <= 12:
    put_success(f'Вартість вашого квитка 50 грн (50% знижка ={enter_your_age}).')
    total_price += price_1 - price_1 * discount_50
elif enter_your_age <= 17:
    put_success(f'Вартість вашого квитка 75 грн (25% знижка={enter_your_age}).')
    total_price = price_2 - price_2 * discount_25
elif enter_your_age <= 59:
    put_success('Вартість вашого квитка 100 грн.')
else:
    put_success(f'Вартість вашого квитка 70 грн (30% знижка={enter_your_age}).')
    total_price += price_3 - price_3 * discount_30
