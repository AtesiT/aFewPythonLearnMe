#                                                         matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(matrix)

#                                           toTakeAnyElement
# print(matrix[1][2])

def newMatrix(matrix):
    for arr in matrix:
        for element in arr: #Проход циклом по матрице
            print(element, end = ' ') #Замена ненужных [] and ,
        print() #Перевод на другую строку, что парадоксально
# newMatrix(matrix)


def newSecondMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()

newSecondMatrix(matrix)

