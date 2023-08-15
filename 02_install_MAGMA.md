It may works for Ubuntu 22.04 only
# 1. Install CUDA 
Read 00

# 2. Install OpenBLAS
Read 01

# 3. Install gfortran
```ruby
sudo apt install gfortran
```

# 4. Install MAGMA
## Download .tar.gz from website
```ruby
wget http://icl.utk.edu/projectsfiles/magma/downloads/magma-2.7.1.tar.gz
```

## Extract it 
```ruby
tar -xvf magma-2.7.1.tar.gz
```
## Update ~/.bashrc
```ruby
vim ~/.bashrc
```
Add following lines in the .bashrc
```ruby
export PATH=/usr/local/cuda/bin/:$PATH
export CUDADIR=/usr/local/cuda
export OPENBLASDIR=/usr/lib/x86_64-linux-gnu/openblas-pthread
export LD_LIBRARY_PATH=/usr/local/magma/lib
```
Source the .bashrc
```ruby
source ~/.bashrc
```
```ruby
make -j 12
```
```ruby
sudo -E make install prefix=/usr/local/magma
```
```ruby
sudo chown -R root /usr/local/magma
```

-End-