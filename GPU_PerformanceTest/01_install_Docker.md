# Docker
Detail: https://www.docker.com/what-docker

## 1. Remove previous version
```ruby
sudo apt-get remove docker docker-engine docker.io
```

## 2. Install Docker CE
Ref: https://docs.docker.com/engine/install/ubuntu/

```ruby
sudo apt-get udpate

sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release
```
```ruby
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
```ruby
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```ruby
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Verify the installation
```ruby
sudo docker run hello-world
```