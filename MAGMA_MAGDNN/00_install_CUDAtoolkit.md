# Maybe useful
Some random packages
```ruby
sudo apt install unzip build-essential git curl vlc htop gnome-tweaks rar unrar
```
# CUDA Toolkit
Follow the instructions from Nvidia
## Example: Ubuntu 22.04
### a. Install the package
```ruby
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin

sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/12.2.1/local_installers/cuda-repo-ubuntu2204-12-2-local_12.2.1-535.86.10-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu2204-12-2-local_12.2.1-535.86.10-1_amd64.deb

sudo cp /var/cuda-repo-ubuntu2204-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cuda
``` 

### b. Locate the package
```ruby
find /usr/local/ -name nvcc
```

### c. Add to .bashrc
```ruby
vim  ~/.bashrc
```
Add to the bottom of the file
```ruby
export PATH=/usr/local/cuda/bin:$PATH
```
Save and close the file. Then soruce the .bashrc
```ruby
source ~/.bashrc
```

## Jetson Orin Nano 
```ruby
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/arm64/cuda-ubuntu2004.pin
```
```
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
```
```
wget https://developer.download.nvidia.com/compute/cuda/12.2.1/local_installers/cuda-tegra-repo-ubuntu2004-12-2-local_12.2.1-1_arm64.deb

```
```
sudo dpkg -i cuda-tegra-repo-ubuntu2004-12-2-local_12.2.1-1_arm64.deb
```
```
sudo cp /var/cuda-tegra-repo-ubuntu2004-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/
```
```
sudo apt-get update
```
```
sudo apt-get -y install cuda
```
### Ref. link
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local

-End-
