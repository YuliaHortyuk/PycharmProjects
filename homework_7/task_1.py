class Matrix:
    def __init__(self, my_list_1, my_list_2):
        self.my_list_1 = my_list_1
        self.my_list_2 = my_list_2

    def __add__(self):
        my_matr = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        for i in range(len(self.my_list_1)):
            for el in range(len(self.my_list_2)):
                my_matr[i][el] = self.my_list_1[i][el] + self.my_list_2[i][el]
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in my_matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in my_matr]))


my_new_matr = Matrix([[3, 5, 8],
                     [2, 4, 6],
                     [9, 4, 1]],
                     [[6, 7, 5],
                     [2, 11, 8],
                     [9, 5, 4]])
print(my_new_matr.__add__())