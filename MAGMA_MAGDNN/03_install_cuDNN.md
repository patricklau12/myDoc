# Install CUDA
see 00
### Check installed
```
nvcc --version
```
Output below means CUDA 12.2 is installed
```ruby
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Jul_11_02:20:44_PDT_2023
Cuda compilation tools, release 12.2, V12.2.128
Build cuda_12.2.r12.2/compiler.33053471_0
```

# Install Zlib
```
sudo apt-get install zlib1g
```

# Download cuDNN
https://developer.nvidia.com/rdp/cudnn-download

## Install cuDNN GPG key (It may changes)
```ruby
sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.4.25/cudnn-local-3C3A81D3-keyring.gpg /usr/share/keyrings/
```

## Install cuDNN
```ruby
sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.4.25_1.0-1_amd64.deb
```

## Import CUDA GPG key
```ruby
sudo cp /var/cudnn-local-repo-*/cudnn-local-*-keyring.gpg /usr/share/keyrings/
```
```ruby
sudo apt-get update
```
## Install the runtime library
### I am using CUDA12.2
```ruby
sudo apt-get install libcudnn8=8.9.4.25-1+cuda12.2
```

## Install the developer library
```ruby
sudo apt-get install libcudnn8-dev=8.9.4.25-1+cuda12.2
```

## Install the code samples
```ruby
sudo apt-get install libcudnn8-samples=8.9.4.25-1+cuda12.2
```