# Pre-requisities
1. GNU/Linux x86_64 with kernel version > 3.10
2. Docker >= 1.12
3. NVIDIA GPU with Architecture > Fermi (2.1)
4. NVIDIA drivers ~= 361.93 (untested on older versions)

## Remove nvidia-docker 1.0 (if installed before)
```ruby
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f

sudo apt-get purge nvidia-docker
```

## Install nvidia-docker 2.0
```ruby
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
```
```ruby
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```
```ruby
sudo apt-get update
```
```ruby
sudo apt-get install nvidia-docker2

sudo pkill -SIGHUP dockerd
```
```ruby
sudo usermod -a -G docker $USER
```

