import numpy as np
# as np выражение позволяет нам получать доступ к numpy объектам используя np. вместо numpy.
matrix = np.array([[0, 4, 2, 9, 11], [3, 0, 9, 12, 5], [9, 4, 12, 12, 11]])    # объект array
p = [0.0, 0.0, 0.55, 0.45, 0.0]
q = [0.55, 0.45, 0.0, 0.0, 0.0]

answer = {}  # создаём словарь

lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)])  # транспонируем матрицу

if lower_price == upper_price:
    print("седловая точка есть", f"ответ v = {lower_price}")
else:
    buff = 0
    for i, pin in zip(matrix, p):
        buff += pin * sum([x * y for x, y in zip(i, q)])
    answer["H(P,Q)"] = buff
    for k, i in enumerate(np.rot90(matrix), 1):   # enumerate нумерует, то есть мы получает сразу индекс элемента и его значение.
        answer["H(P,B{})".format(k)] = sum([x * y for x, y in zip(i, p)])
for i in [(x, y) for x, y in answer.items()]:
    print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))