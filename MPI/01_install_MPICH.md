#### Download link: https://www.mpich.org/

## Installation
```ruby
wget https://www.mpich.org/static/downloads/4.1.2/mpich-4.1.2.tar.gz
```
```ruby
tar -xzf mpich-4.1.2.tar.gz
```

```ruby
cd mpich-4.1.2
```

```ruby
./configure
```
#### When configuration is done, it should say “Configuration completed.” 

#### Once this is through, build and install MPICH2 with make; sudo make install
```ruby
make
```

```ruby
sudo make install
```

Check if installed successfully
```ruby
mpiexec --version
```

Output:
```ruby
HYDRA build details:
    Version:                                 4.1.2
    Release Date:                            Wed Jun  7 15:22:45 CDT 2023
    CC:                              gcc      
    Configure options:                       '--disable-option-checking' '--prefix=NONE' '--with-hwloc=embedded' '--cache-file=/dev/null' '--srcdir=.' 'CC=gcc' 'CFLAGS= -O2' 'LDFLAGS=' 'LIBS=' 'CPPFLAGS= -DNETMOD_INLINE=__netmod_inline_ofi__ -I/home/plau/Downloads/mpich-4.1.2/src/mpl/include -I/home/plau/Downloads/mpich-4.1.2/modules/json-c -I/home/plau/Downloads/mpich-4.1.2/modules/hwloc/include -D_REENTRANT -I/home/plau/Downloads/mpich-4.1.2/src/mpi/romio/include -I/home/plau/Downloads/mpich-4.1.2/src/pmi/include -I/home/plau/Downloads/mpich-4.1.2/modules/yaksa/src/frontend/include -I/home/plau/Downloads/mpich-4.1.2/modules/libfabric/include'
    Process Manager:                         pmi
    Launchers available:                     ssh rsh fork slurm ll lsf sge manual persist
    Topology libraries available:            hwloc
    Resource management kernels available:   user slurm ll lsf sge pbs cobalt
    Demux engines available:                 poll select

```