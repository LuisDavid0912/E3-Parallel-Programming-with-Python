import time
start_time = time.time()  # Registrar el tiempo de inicio de la ejecución

#Importa la clase Pool del módulo de multiprocesamiento. Pool se utiliza para paralelizar tareas a través de múltiples procesos.
from multiprocessing import Pool
import numpy as np


#Define una función llamada f que toma dos argumentos, i y dx. Esta función calcula la altura del rectángulo en la coordenada x dada.
def f(i, dx):

#Calcula la coordenada x a partir del índice i y la anchura de cada intervalo dx.
    x = i * dx
#Calcula la altura del rectángulo en la coordenada x dada utilizando la fórmula de la función de cuarto de círculo,
# y multiplícala por la anchura dx para obtener el área del rectángulo.
    return np.sqrt(1 - x**2) * dx


#Define una función llamada compute_pi_multiprocessing que toma dos argumentos, N (el número de intervalos)
# y num_processes (el número de procesos a utilizar para la paralelización).
def compute_pi_multiprocessing(N, num_processes):

#Calcular la anchura de cada intervalo dx
    dx = 1.0 / N
#Crea un objeto Pool con el número de procesos especificado.
    with Pool(num_processes) as pool:
#Utilice el método starmap del objeto Pool para aplicar la función f a cada i en el rango N, pasando los argumentos (i, dx).
# Esto paraleliza el cálculo de la altura de cada rectángulo.
        result = pool.starmap(f, [(i, dx) for i in range(N)])
#Calcula la aproximación de π sumando los resultados obtenidos de todos los procesos y escalando por 4.
    return 4 * sum(result)

#Comprueba si el script se está ejecutando directamente (no importado como módulo).
if __name__ == '__main__':
#Definir el número de intervalos N para la integración numérica.
    N = 1000000
#Definir el número de procesos a utilizar para la paralelización.
    num_processes = 4

#Llame a la función compute_pi_multiprocessing con el número especificado de intervalos N y el número de procesos num_processes.
# Esto inicia el cálculo paralelo de la aproximación de π.

    pi_approx_multiprocessing = compute_pi_multiprocessing(N, num_processes)

#Imprime la aproximación de π obtenida mediante multiproceso.
    print(f"Multiprocessing π approximation: {pi_approx_multiprocessing}")


end_time = time.time()  # Registrar el tiempo de finalización de la ejecución

execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")