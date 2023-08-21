# Prepare dataset

## Create ImageNet Account

## Download ImageNet

Make a folder to store the dataset. Any place you want
```ruby 
mkdir ~/Desktop/imagenet12  
```
#### These 4 files can be downloaded here: 

http://image-net.org/challenges/LSVRC/2012/2012-downloads

```ruby
ILSVRC2012_img_test_v10102019.tar
ILSVRC2012_img_train_t3.tar
ILSVRC2012_img_train.tar
ILSVRC2012_img_val.tar
```

#### Run the Docker image
```ruby
sudo nvidia-docker run -it --rm --shm-size=1g --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
-v ~/Desktop/imagenet12:/imagenet \
-w /workspace/nvidia-examples/build_imagenet_data/ \
nvcr.io/nvidia/tensorflow:23.07-tf2-py3
```

####  Prepare the necessary folders
```ruby
mkdir -p /imagenet/raw-data
cp /imagenet/ILSVRC2012_img_*.tar /imagenet/raw-data/
```

#### Launch the script within the container
```ruby
./download_and_preprocess_imagenet.sh /imagenet
```


### User manual
##### https://developer.nvidia.com/deep-learning-performance-training-inference/Measuring_Training_and_Inferencing_Performance_on_NVIDIA_AI_Platforms.pdf

