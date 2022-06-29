import random

a = input('За кого зочешь узнать?\nВведи имя: ')

g = ['Нормальный пацан!', 'Уважаемый', 'Хороший человек']
k = ['Толстый', 'Спортсмен не очень', 'Так себе спортик', 'Не уважаемый']
r = ['Угрюмый', 'Шляпа', 'Варчун', 'Так себе человечек']
x = 'Не знаем про таких...'

if a == 'Гошан' or a == 'Георгий' or a == 'Георгийс' or a == 'Georgij' or a == 'Goshan' or a == 'Жора':
    print(random.choice(g))
elif a == 'Костя' or a == 'Константин' or a == 'Костян'or a == 'Kostja' or a == 'Konstantin':
    print(random.choice(k))
elif a == 'Рома' or a == 'Роман' or a == 'Романо' or a == 'Roma' or a == 'Roman' or a == 'Romano':
    print(random.choice(r))
else:
    print(x)
