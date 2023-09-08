# Intel MPI Benchmark
## 1. Pull the source code from here
https://github.com/intel/mpi-benchmarks


## 2. Environment
Ensure that the MPI compiler wrappers (mpicc, mpic++, etc.) are in your PATH. Check with 
```ruby
which mpicc
```
## 3. Set 'CC' variable
```ruby
export CC=mpicc
```
```ruby
export CXX=mpicxx
```

## 4. Make
```ruby
make all
```

## 5. Run
```ruby
mpirun -np 24 -hostfile hosts.txt ./IMB-MPI1
```

## A. hosts.txt
```ruby
node01
node02
node03
node04
```

-End----------------------------------------------------------------