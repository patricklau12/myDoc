https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html

## 1. Assume JetPack installed

## 2. Install Tensorflow required libraries
```ruby
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
```

## 3. Install Python package dependencies
```ruby
sudo pip3 install -U numpy==1.22 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig packaging h5py==3.6.0
```

## 4. Install TF (compatible with JetPack 5.1.2)
```ruby
sudo pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v512 tensorflow==2.12.0+nv23.06
```

-End-