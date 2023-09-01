## Run MPI programs
#### For consideration sake, let’s just take a sample program, that comes along with MPICH2 installation package mpich2/examples/cpi. We shall take this executable and try to run it parallely.

#### Or if you want to compile your own code, the name of which let’s say is mpi_sample.c, you will compile it the way given below, to generate an executable "mpi_sample"
```ruby
mpicc -o mpi_sample mpi_sample.c
```

#### First copy your executable into the shared directory cloud or better yet, compile your code within the NFS shared directory.

### Run it ONLY in local machine
```ruby
mpirun -np 2 ./cpi # No. of processes = 2
```

### Run it within a cluster
```ruby
mpirun -np 5 -hosts node02,node01 ./cpi
#hostnames can also be substituted with ip addresses
```

### We can
### 1. Run the process locally
```ruby
mpirun -np 10 --hosts node01 ./cpi # OK
```
### 2. Run the process as a combination of local and remote nodes
```ruby
mpirun -np 10 --hosts node01,node02,node03 ./cpi # OK
```

### We CANNOT
### 1. Run the process only on other nodes
```ruby
mpirun -np 10 --hosts worker1 ./cpi # NOT WORK
```

