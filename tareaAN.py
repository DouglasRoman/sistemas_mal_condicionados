import numpy as np

# Definir la matriz de coeficientes A y el vector de términos independientes b
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])  # Un sistema mal condicionado

b = np.array([1, 2, 3])

# Intentar resolver el sistema
try:
    solution = np.linalg.solve(A, b)
    print("Solución:", solution)
except np.linalg.LinAlgError as e:
    print("Error en la resolución del sistema:", e)
