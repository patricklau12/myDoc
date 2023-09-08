It may works for Ubuntu 22.04 only
# 1. Install CUDA 
CUDA should be already installed if the Orin was flashed with the SDK manager,
if not, install CUDA by following tutorial 00

# 2. Install OpenBLAS
```ruby
sudo apt update
sudo apt install libopenblas-dev
```

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
export CUDADIR=/usr/local/cuda
export OPENBLASDIR=/lib/aarch64-linux-gnu/openblas-pthread
export LD_LIBRARY_PATH=/usr/local/magma/lib
```
Source the .bashrc
```ruby
source ~/.bashrc
```
## Make parameters
go into make.inc-examples and copy make.inc.openblas into the parent directory and rename it make.inc

```ruby
mv make.inc-examples/make.inc.openblas ./make.inc
```
The Makefile_single file is here
```ruby
git clone https://github.com/patricklau12/myDoc.git
```
modify the make.inc to compile only for ampere architecture by modifying the GPU_TARGET variable on line 57 in make.inc to only be Ampere

for single precision, replace the original makefile with Makefile_single file from this repository, then
```ruby
make dense -j8
```
```ruby
sudo -E make install prefix=/usr/local/magma
```
```ruby
sudo chown -R root /usr/local/magma
```

-End-