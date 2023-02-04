# #                                                         matrix
# # matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# # print(matrix)
#
# #                                           toTakeAnyElement
# # print(matrix[1][2])
# #
# # def newMatrix(matrix):
# #     for arr in matrix:
# #         for element in arr: #Проход циклом по матрице
# #             print(element, end = ' ') #Замена ненужных [] and ,
# #         print() #Перевод на другую строку, что парадоксально
# # newMatrix(matrix)
#
#
# # def newSecondMatrix(matrix):
# #     for i in range(len(matrix)):
# #         for j in range(len(matrix[i])):
# #             print(matrix[i][j], end = ' ')
# #         print()
#
# # newSecondMatrix(matrix)
#
# # matrix[1][1] = 100
# # newSecondMatrix(matrix)
#
#
# # # matrix[1][1] = 5
# #
# #
# # #Таск - Двумерный список заполнить нулями
# # def createMatrix(m, n): #строк #столбцов
# #     theFutureMassive = []
# #
# #     for i in range(m):
# #         internalMassive = []
# #
# #         for j in range(n):
# #             internalMassive.append(0)
# #
# #         theFutureMassive.append(internalMassive)
# #
# #     return theFutureMassive
# #
# #
# # print(createMatrix(5, 10))
# #
# #
#



# TheProjectOfGame
def deposit():
    while True:
        amount = input('Ваша ставка? Р ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Ставка должна быть больше ноля')
        else:
            print('Введите число')
    return amount

deposit()