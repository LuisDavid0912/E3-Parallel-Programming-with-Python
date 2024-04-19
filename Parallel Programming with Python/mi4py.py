import time
start_time = time.time()  # Registrar el tiempo de inicio de la ejecución

#Import the MPI (Message Passing Interface) module from the mpi4py package. MPI is used for distributed parallel computing.
from mpi4py import MPI 
#: Import the numpy library as np. numpy is used for numerical computations.
import numpy as np

 
#Define una función llamada compute_pi que toma un argumento N, que representa el número de intervalos a utilizar para la integración numérica.
def compute_pi(N):

# Initialize MPI environment
#comm that represents the group of processes.
    comm = MPI.COMM_WORLD #Initialize the MPI environment and create a communicator object 
#Obtiene el rango del proceso actual dentro del comunicador. A cada proceso se le asigna un rango único.
    rank = comm.Get_rank()
#Obtiene el número total de procesos en el comunicador.
    size = comm.Get_size()

#Calcula el número de intervalos gestionados por cada proceso. Divide el número total de intervalos N por el tamaño del número de procesos
#y añade 1 al recuento local de intervalos para los procesos restantes (si los hay).
    local_n = N // size + (rank < N % size)
#Calcula el índice inicial del intervalo local para el proceso actual.
    start = rank * local_n
#Calcula el índice final del intervalo local para el proceso actual.
    end = start + local_n

#Generar una matriz de valores local_n igualmente espaciados entre inicio/N y fin/N. Estos valores representan las coordenadas x para la integración numérica.
    x = np.linspace(start/N, end/N, local_n, endpoint=False)
#Calcula la suma local para el proceso actual sumando los valores de la función de cuarto de círculo para las coordenadas x generadas y escalando por la anchura del intervalo.
    local_sum = np.sum(np.sqrt(1 - x**2)) * (1.0 / N)

#Reduce( funciónreducir ) las sumas locales de todos los procesos al proceso raíz (rango 0) utilizando la operación MPI SUM. A continuación,
#escala la suma por 4 para obtener la aproximación de π.
    pi_approx = 4 * comm.reduce(local_sum, op=MPI.SUM, root=0)

#Comprueba si el proceso actual es el proceso raíz (rango 0).
    if rank == 0:
        #Si el proceso actual es el proceso raíz, imprime la aproximación de π.
        print("Pi with MPI:", pi_approx)

#Comprueba si el script se está ejecutando directamente (no importado como módulo).
if __name__ == "__main__":
#Definir el número de intervalos N para la integración numérica.
    N = 10_500_000
 #toda la función compute_pi con el número especificado de intervalos N. Esto iniciará el cálculo de la aproximación de π usando MPI.   
    compute_pi(N)



end_time = time.time()  # Registrar el tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")