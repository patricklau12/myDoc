# VNC Setup
#### Remote control the nodes

## Setup VNC server on the Jetson developer kit

### 1. Setting
        Setting -> Sharing -> Screen Sharing -> Set 'Active' or 'Enable'

        And set 'Auto Login' to true


### 2. Enable VNC Server
#### Enable the VNC server to start each time you log in
```ruby
cd /usr/lib/systemd/user/graphical-session.target.wants
sudo ln -s ../vino-server.service ./.
```
```ruby
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
```
```ruby
# Replace the password with your desired password
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n 'YourPassword'|base64)
```

# Important: VNC requires a monitor plugged in to use
## Solution: Enable virtual display
### 1. Install xserver-xorg-video-dummy
```ruby
sudo apt update
sudo apt install xserver-xorg-video-dummy
```
### 2. Create config for dummy display
```ruby
cd /etc/X11
sudo vim xorg.conf.dummy
```
#### Add the following lines in the xorg.conf.dummy. You can change resolution
```ruby
Section "Device"
    Identifier "DummyDevice"
    Driver "dummy"
    VideoRam 256000
EndSection
 
Section "Screen"
    Identifier "DummyScreen"
    Device "DummyDevice"
    Monitor "DummyMonitor"
    DefaultDepth 24
    SubSection "Display"
        Depth 24
        Modes "1920x1080_60.0"
    EndSubSection
EndSection
 
Section "Monitor"
    Identifier "DummyMonitor"
    HorizSync 30-70
    VertRefresh 50-75
    ModeLine "1920x1080" 148.50 1920 2448 2492 2640 1080 1084 1089 1125 +Hsync +Vsync
EndSection
```
### 3. Update /etc/X11/xorg.conf
```ruby
cp xorg.conf xorg.conf.backup
cp xorg.conf.dummy xorg.conf
```
```ruby
sudo reboot 
```

## Download VNC Viewer in your machine
https://www.realvnc.com/en/connect/download/viewer/

### Remote the Jetson with their IP