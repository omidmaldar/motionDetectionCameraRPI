# For sending email
* If you use Gmail, make `Less Secure APP Access` **ON** Read [Less Secure APP Access and Google Account](https://support.google.com/accounts/answer/6010255?authuser=1&p=less-secure-apps&hl=en&authuser=1&visit_id=637046560394549091-3119828862&rd=1) 

# Finding IP addr
* `ifconfig wlan0 | grep 'inet ' | awk '{print $2}'`
* **ETHR** `ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1`
* **WLAN** `ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1`

# Preparation
* sudo apt update
* sudo apt upgrade
* sudo apt autoremove

# Install USB Webcam 
* sudo apt install rpi-update
* sudo rpi-update (you may skip this step, pay full attention to the warning it shows)
* sudo apt install fswebcam  

# Take a photo
* fswebcam test.jpg

# View the photo
* install `ImageMagic` by `sudo apt install imagemagick`
* display test.jpg

# Installing Motion
* sudo apt install motion

# Configuring Motion for streaming over Internet
*  Edit the config file: `sudo nano /etc/motion/motion.conf`
* `daemon on`: Set this to ‘on’ if you want motion to be able to run as a background process
* `stream_port`: This is the default port that the webcam server will run on.
* `webcontrol_localhost`: Set this to off if you want to access the webcam stream remotely
* `width 1024` 
* `height 768`
* `framerate 25`
* `stream_maxrate 10`

# Activate Camera driver to be detected by Motion (Might be needed)
* sudo modprobe bcm2835-v4l2
* Edit `sudo /etc/modules` and add these two lines
  * snd-bcm2835
  * bcm2835-v4l2
  
# Controlling Motion Service
* sudo service motion start
* sudo service motion status
* sudo service motion stop

# Logs
* tail -f /var/log/motion/motion.log

# Watch the stream from your laptop
* connect to http://localhost:8081 

# Links: 
* [Motion Detector](https://www.instructables.com/id/Raspberry-Pi-Motion-Detector-and-Alert-System/)
* [Motion](https://motion-project.github.io/) 
* [USB Camera for Motion](http://www.richardmudhar.com/blog/2015/02/raspberry-pi-camera-and-motion-out-of-the-box-sparrowcam/)
* [Standard USB Camera for Raspberry Pi](https://www.raspberrypi.org/documentation/usage/webcams/)
