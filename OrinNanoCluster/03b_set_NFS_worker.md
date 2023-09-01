## For worker nodes

### Installation
```ruby
sudo apt-get install nfs-common
```

### Create a directory with same name as the server directory
"cloud" in this case

```ruby
mkdir cloud
```

### Mount the shared directory
```ruby
sudo mount -t nfs node01:/home/jetbot/Desktop/mpiProject/cloud ~/Desktop/mpiProject/cloud
```

### Check mounted?
```ruby
df -h
```


```ruby
# Example output:
jetbot@node02:~/Desktop/mpiProject$ df -h
Filesystem                                    Size  Used Avail Use% Mounted on
/dev/mmcblk1p1                                 57G   27G   28G  49% /
none                                          3.6G     0  3.6G   0% /dev
tmpfs                                         3.7G     0  3.7G   0% /dev/shm
tmpfs                                         748M   19M  729M   3% /run
tmpfs                                         5.0M  4.0K  5.0M   1% /run/lock
tmpfs                                         3.7G     0  3.7G   0% /sys/fs/cgroup
tmpfs                                         748M   16K  748M   1% /run/user/124
tmpfs                                         748M  8.0K  748M   1% /run/user/1000

# mounted dir appears here
node01:/home/jetbot/Desktop/mpiProject/cloud  458G   61G  379G  14% /home/jetbot/Desktop/mpiProject/cloud
```

#### To make the mount permanent so you don’t have to manually mount the shared directory everytime you do a system reboot, you can create an entry in your file systems table - i.e., /etc/fstab file like this:
```ruby
sudo vim /etc/fstab
```
#### Add the line below to the /etc/fstab
```ruby
node01:/home/jetbot/Desktop/mpiProject/cloud    /home/jetbot/Desktop/mpiProject/cloud    nfs    defaults    0 0