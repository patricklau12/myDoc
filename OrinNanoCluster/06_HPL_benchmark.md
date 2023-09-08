# HPL

## 1. Download and unzip
```ruby
wget https://icl.utk.edu/projectsfiles/hpl/hpl-2.1.tar.gz
```


```ruby
# Copied from the INSTALL.md 

1) Retrieve the tar file, then

    gunzip hpl.tgz; tar -xvf hpl.tar

 this  will create an  hpl  directory,  that we call below the
 top-level directory.

 2) Create a file Make.<arch> in the  top-level directory. For
 this purpose,  you  may  want  to re-use one contained in the
 setup directory. This file essentially contains the compilers
 and librairies with their paths to be used.

 3) Type "make arch=<arch>". This  should create an executable
 in the bin/<arch> directory called xhpl.

 For example, on our Linux PII cluster, I create a file called
 Make.Linux_PII in the top-level directory. Then, I type
    "make arch=Linux_PII" 
 This creates the executable file bin/Linux_PII/xhpl.

 4) Quick check: run a few tests:

    cd bin/<arch>
    mpirun -np 4 xhpl

 5) Tuning: Most of the performance  parameters can be tuned,
 by modifying the input file bin/HPL.dat. See the file TUNING
 in the top-level directory.

 ```