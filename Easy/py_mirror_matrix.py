"""
Escribe una funciГіn que espeje una matriz 2D horizontalmente invirtiendo cada fila.

La funciГіn debe:
- Recibir una lista 2D (matriz) de enteros
- Devolver una nueva lista 2D donde cada fila estГ© invertida horizontalmente
- Manejar matrices de cualquier tamaГ±o (cuadradas o rectangulares)
- Conservar el orden original de las filas
- No modificar la matriz original

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:

mirror_matrix([[1,2,3],[4,5,6]])
[[3,2,1],[6,5,4]]

mirror_matrix([[1,2],[3,4],[5,6]])
[[2,1],[4,3],[6,5]]

mirror_matrix([[7]])
[[7]]

mirror_matrix([[1,2,3,4]])
[[4,3,2,1]]

mirror_matrix([[-1,-2],[-3,-4]])
[[-2,-1],[-4,-3]]
"""

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    copy_matrix = []

    for f in matrix:
        copy_matrix.append(f[::-1])
    
    return copy_matrix


if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))
    print(mirror_matrix([[1,2],[3,4],[5,6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1,2,3,4]]))
    print(mirror_matrix([[-1,-2],[-3,-4]]))


