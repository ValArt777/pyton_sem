revenue = int(input('Введите выручку : '))
cost = int(input('Введите издержки : '))
if revenue < cost:
    print(f'Финансовый результат убыток : Величина убытка {revenue - cost}')
else:
    profit = revenue - cost
    print(f'Финансовый результат прибыль : {profit}')
    print(
        f'Вычисляем рентабельность выручки (соотношение прибыли к выручке): {profit / revenue} ')
    empl = int(input('Введите число сотрудников : '))
    empl_res = profit / empl
    print(f'Прибыль фирмы в расчете на одного сотрудника: {empl_res}')