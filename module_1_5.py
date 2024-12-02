# Залание 1
tuple_immutable_var_ = 1, 2, False, 'Python', [1, 2]
# задание 2
print(tuple_immutable_var_)
# задание 3
#tuple_immutable_var_[1] = 1
#выдает ошибку, так как кортежи не поддерживает обращение по элементам
# задание 4
tuple_mutable_list_ = (3, 4, [3, 4], 'Limit')
print(tuple_mutable_list_)
tuple_mutable_list_[2][1] = 2
print(tuple_mutable_list_)
tuple_mutable_list_[2][0] = 1
print(tuple_mutable_list_)