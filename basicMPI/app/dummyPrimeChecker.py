import sys
import math
import time
from mpi4py import MPI
comm = MPI.COMM_WORLD   # Defines the default communicator
num_procs = comm.Get_size()  # Stores the number of processes in num_procs.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process

def checkPrime(n):
    if(n%2 == 0):
        return 0
    for i in range(3,math.floor(math.sqrt(n))+1,2):
        if (n%i == 0):
            return 0
    return 1
        
#print("Proceso verificador ! ",rank, " con argumento ",sys.argv[1])

k = int(sys.argv[1])

if rank == 0:
    start = time.time()
    primes = 0
    num_paq = [0]*(num_procs-1)
    for i in range(1,k+1, 100*(num_procs-1)):
        for proc in range(1, num_procs):
            li = i+100*(proc-1)
            ls = i+100*proc
            if ls > k+1:
                ls = li + k%100
            if li < k+1:
                num_paq[proc-1]+=1
                sw = 0
                if(100*sum(num_paq)>=k-100*(num_procs-2)):
                    sw = 1
                comm.send([li,ls,num_paq[proc-1],sw], dest=proc)
            else:
                comm.send(None, dest=proc)
        for proc in range(1, num_procs):
            primes+= comm.recv(source=proc)
    for proc in range(1, num_procs):
        comm.send(None, dest=proc)
    print("Numero de primos hasta ",k," :", primes)
    print("Tiempo: ",time.time()-start, "s")
else:
    data = [0,0,0,0]
    while data is not None:
        data = comm.recv(source=0)
        if data is not None:
            sumprimes = 0
            for i in range(data[0], data[1]):
                sumprimes+= checkPrime(i)
            comm.send(sumprimes, dest=0)
            if (data[3] == 1):
                print("El proceso ", rank, " verifico ", data[2], " paquetes.")
            