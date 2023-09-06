## 1. Configure hosts file 
### Edit /etc/hosts
#### to communicate between the computers and you don’t want to type in the IP addresses every so often. Instead, give a name to the various nodes in the network that you wish to communicate with. hosts file is used by your device operating system to map hostnames to IP addresses.

```ruby
sudo vim /etc/hosts 
```
### Enter the nodes static IP address 

#### The node02 here is the machine you’d like to do your computation with. Likewise, do the same about node01 in the node02. 

#### Or just enter all nodes' IP addresses into /etc/hosts
```ruby
192.168.0.210   node01
192.168.0.211   node02
```



## 2. SSH Setup
#### Nodes are communicating via SSH and share data via NFS

### On node01 (Server)
```ruby
sudo apt­-get install openssh-server
```
#### Generate keys and copy them to other machines'list of authorized_keys, for easier login

```ruby
ssh-keygen -t rsa -f ~/.ssh/id_rsa
```
#### Add the generated key to each of the other computers. In our case, the node02 machine
```ruby
ssh-copy-id -i ~/.ssh/id_rsa.pub jetbot@node02
```
## Do the above step for each of the worker machines, and localhost
#### This will setup openssh-server for you to securely communicate with the worker machines. ssh all machines once, so they get added to your list of known_hosts. This is a very simple but essential step failing which passwordless ssh will be a trouble

<!-- #### Enable passwordless SSH
```ruby
eval `ssh-agent`
```
```ruby
ssh-add ~/.ssh/id_dsa
``` -->

## 3. Check the configuration
#### Try ssh node2 from node01 (master node)
```ruby
ssh node02
```

Should be able to ssh into node02 without using password



## Sample hostfile entry of a Server
```ruby
cat /etc/hosts
127.0.0.1	localhost

#MPI CLUSTER SETUP
172.50.88.22	manager
172.50.88.56 	worker1
172.50.88.34 	worker2
172.50.88.54	worker3
172.50.88.60 	worker4
172.50.88.46	worker5
```

## Sample hostfile entry of a worker
```ruby
cat /etc/hosts
127.0.0.1	localhost

#MPI CLUSTER SETUP
172.50.88.22	manager
172.50.88.54	worker3
```

