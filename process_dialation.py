from predict_n_list import generate_n_list

list1 = [7, 9, 10, 11]
print(list1)
list2 = [9, 12, 13, 14, 15]
print(list2)
list3 = [11, 15, 16, 17, 18, 19]
print(list3)
n = 100

rd_list = generate_n_list(list1, list2, list3, n)
print(rd_list)