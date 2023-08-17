# Install MAGMA
see 02
### Check installed
```ruby
grep MAGMA_VERSION /usr/local/magma/include/*.h
```
Output below means MAGMA 2.7.1 is installed
```ruby
/usr/local/magma/include/magma_types.h:#define MAGMA_VERSION_MAJOR 2
/usr/local/magma/include/magma_types.h:#define MAGMA_VERSION_MINOR 7
/usr/local/magma/include/magma_types.h:#define MAGMA_VERSION_MICRO 1
/usr/local/magma/include/magma_types.h:#define MAGMA_VERSION_STAGE ""
```