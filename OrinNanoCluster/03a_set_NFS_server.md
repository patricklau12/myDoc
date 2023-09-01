# NFS
 Share a directory via NFS in manager which the worker mounts to exchange data

## 1. NFS-Server (In node01, or the master node)
#### Installation
```ruby
sudo apt-get install nfs-kernel-server
```

#### Create a folder that will share across in the network
```ruby
mkdir cloud
```


#### Create an entry in /etc/exports
```ruby
# To export the cloud directory, you create an entry in /etc/exports
vim /etc/exports
```
```ruby
/home/jetbot/Desktop/mpiProject/cloud   *(rw,sync,no_root_squash,no_subtree_check)
```
### instead of * you can specifically give out the IP address to which you want to share this folder to. But, this will just make our job easier.


        1. rw: This is to enable both read and write option. ro is for read-only.

        2. sync: This applies changes to the shared directory only after changes are committed.

        3. no_subtree_check: This option prevents the subtree checking. When a shared directory is the subdirectory of a larger filesystem, nfs performs scans of every directory above it, in order to verify its permissions and details. Disabling the subtree check may increase the reliability of NFS, but reduce security.

        4. no_root_squash: This allows root account to connect to the folder.

#### Every time you make a change to /etc/exports, run this:
```ruby
exportfs -a
```
#### Restart the NFS server
```ruby
sudo service nfs-kernel-server restart
```
