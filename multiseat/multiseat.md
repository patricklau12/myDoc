A full comprehensive guide can be found [here](https://docs.google.com/document/d/1LGUJnEZ7c6VP3upGLUYFddncEqKEW4GCDJKc0esoJbw/edit#heading=h.2v8j146zl0i4). 

The simplified version below using 22.04 as a guide

First install everything the computer neees especially the nvidia binary drivers as well as ssh in case you mess up the setup using 

```
"however to download cuda"
sudo apt-get install openssh-server
```

Then run the command below to see all the seats as well as the adddresses. Initially there should only be a seat0

```
sudo loginctl list-seats (should only be one seat)
sudo loginctl seat-status seat0 (shows all the connections)
```

it is recommended to save the output of  ```sudo loginctl seat-status seat0``` into a text file somewhere so it is easier to copy the addresses later

To add the components to a different seat, run
```
sudo loginctl attach seat1 /sys/devices/<ADDRESS>
```
with the address being the whole /sys/devices/pcie.... line.
You must always add the gpu card first which should have a [MASTER] label next to it. 

You can see which GPU is which by running ```nvidia-settings``` and clicking on the specific GPU which should tell you the addresses.

While you are here, click on ```X Server Display Configuration``` and allow all monitors and setup any multihead configurations. To save it will want to write into the /etc/X11/xorg.conf file but it sometimes will not allow you to do so. A workaround is to copy the contents and the manually paste the contents into the file using ``` sudo vim ```

After the GPU is added, you then add the mouse and keyboards, as well as the sound card and specific usb ports that you want using the same command. Each GPU should have a sound card so you should double check the addresses of the GPU and sound card are the same. 

If you mess up, you can run ```sudo loginctl flush-devices``` to undo all changes to start again.

After you have added everything you should restart the computer and you should have two login screens. If this doesn't work try reading the documentation google doc. Else you can email or text me.