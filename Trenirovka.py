#Тренировка - отработка


# 1.Максимум в списке
# 2.Подсчет четных чисел в списке
# 3.Уникальный список

def find_max (list_): #1 Максимум в списке
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

print(find_max([1,1]))

def count_even(list_): #2 Подсчет четных чисел в списке
    counter = 0
    for i in list_:
        if i % 2 == 0:
            counter += 1
    return counter
print(count_even([2,2,3,4,2,1]))



def delta (list_): #3 Уникальный список
    spot_ = []
    for i in list_:
        if i not in spot_:
           spot_.append(i)

    return spot_
print(delta([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]))
