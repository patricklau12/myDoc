## 1. edit /etc/hosts
```ruby
sudo vim /etc/hosts 
```
Enter the nodes static IP address 
```ruby
192.168.0.210   node01
192.168.0.211   node02
```

Check the configuration
Try ssh node2 from node01 (master node)
```ruby
ssh node02
```

## 2. Setup SSH Key-Based Authentication
On node01
```ruby
ssh-keygen
```

```ruby
ssh-copy-id node02
```

Should be able to ssh into node02 without using password

Do the above step for each of the worker machines, and localhost

