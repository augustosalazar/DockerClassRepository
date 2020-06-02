FROM ubuntu:18.04
RUN apt update
RUN apt -y install nano
RUN apt -y install sudo
RUN apt -y install net-tools
RUN apt -y install software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y openssh-server
RUN apt -y install python3.7
RUN apt -y install python3-pip
RUN apt -y install libopenmpi-dev
RUN pip3 install mpi4py
RUN pip3 install numpy
RUN echo "btl_base_warn_component_unused = 0" >> /etc/openmpi/openmpi-mca-params.conf 
RUN adduser --disabled-password --gecos "" mpirun
RUN echo "mpirun ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir /app
RUN chown mpirun:mpirun /app