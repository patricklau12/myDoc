## 1. Preparation
```ruby
sudo apt install build-essential libglvnd-dev pkg-config
```

## 2. Disable current driver
```ruby
sudo telinit 3
```

## 3. Remove previous driver, and install
### Method 1
Remove your previous drivers as well as start the installer (replace the name of the .run file below with the one downloaded previously):
```ruby
sudo apt purge nvidia-*

cd ~/Downloads

sudo chmod +x NVIDIA-Linux-x86_64-xxx.xx.run

sudo ./NVIDIA-Linux-x86_64-xxx.xx.run
```

### Method 2 
Replace nvidia-xxx below with preferred driver version 

Latest drivers: https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa

```ruby
sudo apt purge nvidia-*

sudo add-apt-repository ppa:graphics-drivers/ppa

sudo apt update

sudo apt install nvidia-driver-xxx
```
```ruby
sudo reboot
```

-End-