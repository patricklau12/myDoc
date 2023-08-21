## 1. Define dataset
```ruby
export IMAGENET_DATASET=~/Desktop/imagenet12/
```


## 2. Run the Docker
### Train ResNet-50 in TensorFlow

```ruby
nvidia-docker run -it --rm --shm-size=1g --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
-v $IMAGENET_DATASET:/imagenet \
-w /workspace/nvidia-examples/cnn \
nvcr.io/nvidia/tensorflow:23.07-tf2-py3 \
python resnet.py --data_dir /imagenet -b 32 -i 500 --use_xla
```

#### Output
```ruby
500/500 - 105s - loss: 12.2749 - top1: 0.0012 - top5: 0.0063 - val_loss: 12.2358 - val_top1: 7.8125e-04 - val_top5: 0.0063 - 105s/epoch - 210ms/step
```

## Result
#### GPU: GTX 4070 Ti 
#### Batch size: 128 
|   Loss  	| Val_loss 	| sec/epoch 	| ms/step 	|
|:-------:	|:--------:	|:---------:	|:-------:	|
| 12.2749 	|  12.2358 	|    105s   	|  210ms  	|