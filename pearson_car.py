from cmath import sqrt
import statistics

arrayX = [6,9,6,4,3,6,8]
arrayY = [9,5,7,9,3,8,1]

def carrelation(array1:list, array2:list):
    averageX =  statistics.mean(array1)
    averageY =  statistics.mean(array2)

    def chast(array1, array2):
        return (array1 - averageX)*(array2 - averageY)
    def delitel(array1, array2):
        return (array1 - averageX)**2 *(array2 - averageY)**2

    return sum(list(map(chast, arrayX, arrayY))) / sqrt(sum(list(map(delitel, arrayX, arrayY))))
print ('Корреляция: ')
print(round(carrelation(arrayX, arrayY).real, 5) + round(carrelation(arrayX, arrayY).imag, 5)* 5j)
