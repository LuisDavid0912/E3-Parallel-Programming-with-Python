import time
start_time = time.time() 
import numpy as np

#Definir una función llamada compute_pi_sequential que toma un argumento N, que representa el número de intervalos a utilizar para la integración numérica.
def compute_pi_sequential(N):

#Calcula la anchura de cada intervalo dx.
    dx = 1 / N

#Calcula la suma de los valores de la función de cuarto de círculo para cada coordenada x en el intervalo dado.
    total = sum(np.sqrt(1 - (i * dx) ** 2) for i in range(N))

#Calcula la aproximación de π multiplicando la suma total por 4 y escalándola por la anchura del intervalo.
    return 4 * total * dx

#Definir el número de intervalos N para la integración numérica.
#N = 1000000 se elige probablemente porque proporciona una buena aproximación de π con un tiempo de ejecución razonable.
N = 1000000

#Llama a la función compute_pi_sequential con el número especificado de intervalos N. Esto calcula la aproximación de π secuencialmente.
pi_approx_sequential = compute_pi_sequential(N)

#Imprime la aproximación de π obtenida mediante cálculo secuencial.
print(f"Sequential π approximation: {pi_approx_sequential}")


end_time = time.time()  # Registrar el tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")