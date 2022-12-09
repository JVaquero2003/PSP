#Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, 
# que contenga los siguientes métodos: 

#     - getNumberRows(): devuelve el número de filas de la matriz.

#     - getNumberColumns(): devuelve el número de columnas de la matriz.

#     - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].

#     - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix],
#        y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas 
#        y columnas que la matriz inicial, la operación no se puede realizar (notificalo).

#     - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de 
#       [matrix], y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número 
#       de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).


class Matriz:

    def __init__(self, rows, columns, matriz = [[],[]]):
        self.rows = rows
        self.columns = columns
        self.matriz = [[0 for y in range(columns)] for x in range(rows)]

    def getNumRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.columns

    def setElement(self, row, col, item):
        self.matriz[row][col] = item
        
    def addMatriz(self, tabla):
        
        if len(self.matriz)==len(tabla) and len(self.matriz[0])==len(tabla[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matriz[i][j] = self.matriz[i][j]+tabla[i][j]
            print(self.matriz)
        else:
            print("las matrices no se pueden sumar ya que no tienen las mismas dimensiones")
    
    def mulMatriz(self, tabla):
        if len(self.matriz)==len(tabla) and len(self.matriz[0])==len(tabla[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matriz[i][j] = self.matriz[i][j]*tabla[i][j]
            print(self.matriz)
        else:
            print("las matrices no se pueden multiplicar ya que no tienen las mismas dimensiones")


mat = Matriz(2,3)
tabla=[[1,2,3],[1,2,3]]
mat.addMatriz(tabla)
mat.setElement(0,0,2)
mat.setElement(0,1,3)
mat.setElement(0,2,4)
mat.mulMatriz(tabla)