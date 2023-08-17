## Sign Up for Nvidia GPU Cloud
### Open your browser to https://ngc.nvidia.com and click on Sign Up to create an account for the NVIDIA GPU Cloud.

### Once logged in, click on Get API Key and generate your NGC API key. This key will be used each time you log in to Docker.

#### The username is exactly "$oauthtoken"
```ruby
sudo docker login nvcr.io

Username: $oauthtoken

Password: Your API Key
```
## Pull container from Nvidia GPU Cloud Registry
### e.g. TensorFlow: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow

### pyTorch and other performs also aviliable

Using the interactive parameter (-it) which allows you to use the container workspace like a typical Terminal session.

You may also change the TF version.
```ruby
sudo docker pull nvcr.io/nvidia/tensorflow:23.07-tf2-py3
```
#### To view current Docker container instances and their status, use the below command (notice that the container will be listed by name, eg. optimistic_mcnulty):
```ruby
sudo docker ps -a
```

#### To remove a running container:
```ruby
docker rm container_name
```
