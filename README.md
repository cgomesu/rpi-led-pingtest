# Description
This is a simple python script for the Raspberry Pi to run a ping command and blink a GREEN LED if the host is up and otherwise, blink a RED LED.  LEDs are connected to the RPI via its GPIO pins.

# Default wiring
For both LEDs, make sure to use an approriate current limiting resistor.

* RED LED: GPIO **#18**
* GREEN LED: GPIO **#15**

# Installation
- Raspbian OS:
```
apt-get update
apt-get install git
cd /opt
git clone https://github.com/cgomesu/rpi-led-pingtest.git
# IFF you have permission issues, run 'sudo chown -R pi:sudo rpi-led-pingtest' to change the folder ownership to user pi.
cd rpi-led-pingtest
# Run the script
python3 main.py
```

# Usage
By default, the script will ping **Google's 8.8.8.8** to check for Internet connectivity **every 5 seconds**.  To change the host, use the argument `--pinghost` and to change the ping test period, use the argument `--pingtime`.  Example, ping IP=1.1.1.1 every 15 seconds: `python3 main.py --pinghost=1.1.1.1 --pingtime=15`.  It's possible to use hostnames as well (anything that `man ping` will accept as valid).  For additional information, use the argument `--help`, per usual.

# Running as a service (systemd)
```
# IFF you have permission issues, just add 'sudo' before each command
cp /opt/rpi-led-pingtest/led-pingtest-rpi.service /lib/systemd/system/
systemctl enable led-pingtest-rpi.service
systemctl start led-pingtest-rpi.service
# Check status it's running without issues
systemctl status led-pingtest-rpi.service
```

