## 1. Pull tutorial repo
```ruby
git clone https://github.com/mpitutorial/mpitutorial
```
```ruby
cd mpitutorial/tutorials/mpi-hello-world/code
```
```ruby
cat makefile
```
Output
```ruby
EXECS=mpi_hello_world
MPICC?=mpicc

all: ${EXECS}

mpi_hello_world: mpi_hello_world.c
    ${MPICC} -o mpi_hello_world mpi_hello_world.c

clean:
    rm ${EXECS}

```
## 2. Make
### a. find where is mpicc
```ruby
which mpicc
```

Output:
```ruby
/usr/local/bin/mpicc
```

### b. export
```ruby
export MPICC=/usr/local/bin/mpicc
```
```ruby
make
```