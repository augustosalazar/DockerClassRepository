# DockerClassRepository

Some examples:

MPI Cluster:
https://github.com/oweidner/docker.openmpi.git

MPI cluster:
https://github.com/dispel4py/docker.openmpi


docker inspect --format '{{ .NetworkSettings.IPAddress }}' dockeropenmpi_mpi_head_1

chmod 400 ssh/id_rsa.mpi
ssh -i ssh/id_rsa.mpi tutorial@<ip>

inside the mpi head:
cd /home/tutorial/mpi4py_benchmarks

To create the mpi host file:
- cat /etc/hosts | grep mpi_node --color=none | awk '{print $1}' | sort -u > machines && cat ./machines
- Add the mpihead ip to the machines file

mpiexec -hostfile machines -n 16 python helloworld.py

