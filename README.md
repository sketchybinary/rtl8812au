<<<<<<< Updated upstream
## RTL8812AU/21AU and RTL8814AU drivers
### Supports Realtek 8811, 8812, 8814 and 8821 chipsets

[![Monitor mode](https://img.shields.io/badge/monitor%20mode-working-brightgreen.svg)](#)
[![Frame Injection](https://img.shields.io/badge/frame%20injection-working-brightgreen.svg)](#)
[![GitHub version](https://badge.fury.io/gh/aircrack-ng%2Frtl8812au.svg)](https://badge.fury.io/gh/aircrack-ng%2Frtl8812au)
[![GitHub issues](https://img.shields.io/github/issues/aircrack-ng/rtl8812au.svg)](https://github.com/aircrack-ng/rtl8812au/issues)
[![GitHub forks](https://img.shields.io/github/forks/aircrack-ng/rtl8812au.svg)](https://github.com/aircrack-ng/rtl8812au/network)
[![GitHub stars](https://img.shields.io/github/stars/aircrack-ng/rtl8812au.svg)](https://github.com/aircrack-ng/rtl8812au/stargazers)
[![GitHub license](https://img.shields.io/github/license/aircrack-ng/rtl8812au.svg)](https://github.com/aircrack-ng/rtl8812au/blob/master/LICENSE)
<br>
[![Kali](https://img.shields.io/badge/Kali-supported-blue.svg)](https://www.kali.org)
[![Arch](https://img.shields.io/badge/Arch-supported-blue.svg)](https://www.archlinux.org)
[![Armbian](https://img.shields.io/badge/Armbian-supported-blue.svg)](https://www.armbian.com)
[![ArchLinux](https://img.shields.io/badge/ArchLinux-supported-blue.svg)](https://img.shields.io/badge/ArchLinux-supported-blue.svg)
[![aircrack-ng](https://img.shields.io/badge/aircrack--ng-supported-blue.svg)](https://github.com/aircrack-ng/aircrack-ng)
[![wifite2](https://img.shields.io/badge/wifite2-supported-blue.svg)](https://github.com/derv82/wifite2)

### TODO

## This driver is brand new, it will take some time to add all patches from v5.3.4 even though many got merged into it.
## This driver only supports 8812au chipset at the moment. We're working on it, so please be patient. Thanks

### DKMS
This driver can be installed using [DKMS]. This is a system which will automatically recompile and install a kernel module when a new kernel gets installed or updated. To make use of DKMS, install the `dkms` package, which on Debian (based) systems is done like this:
```
sudo apt-get install dkms
```
=======
# RTL8812AU/21AU and RTL8814AU linux driver with monitor mode and frame injection
`The master branch is based on https://github.com/ulli-kroll/rtl8821au branch v4.3.22-beta/rework.
According to rtw_version.c the real driver version is 4.3.20.`

# Info
`We recommend building from the v5.1.5 branch, which got kernel v4.12 support & more adapters supported. 
Both the 8812AU & 8814AU is supported on the v5.1.5 branch.`


The branch v4.3.21 may also be built for RTL8814AU or RTL8812AU/RTL8821AU chipset. 
Notice, kernel v4.12 support is still missing on the v4.3.21 branch.

## Installing from package in Fedora
Checkout my [copr repo](https://copr.fedorainfracloud.org/coprs/sketchybinary/RTL8812AU)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/sketchybinary/RTL8812AU/package/rtl8812au/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sketchybinary/RTL8812AU/package/rtl8812au/)

## Build it yourself
For building RTL8812AU/RTL8821AU driver type:

`$ make`
>>>>>>> Stashed changes

### Installation of Driver
In order to install the driver open a terminal in the directory with the source code and execute the following command:
```
sudo ./dkms-install.sh
```

### Removal of Driver
In order to remove the driver from your system open a terminal in the directory with the source code and execute the following command:
```
sudo ./dkms-remove.sh
```

### Make
For building & installing the driver with 'make' use
```
make
make install
```

### Notes
Download
```
git clone -b v5.6.4 https://github.com/aircrack-ng/rtl8812au.git
cd rtl*
```
Package / Build dependencies (Kali)
```
sudo apt-get install build-essential
sudo apt-get install bc
sudo apt-get install libelf-dev
sudo apt-get install linux-headers-`uname -r`
```
#### For Raspberry (RPI)

```
sudo apt-get install bc raspberrypi-kernel-headers
```

Then run this step to change platform in Makefile, For RPI 2/3:
```
$ sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
$ sed -i 's/CONFIG_PLATFORM_ARM_RPI = n/CONFIG_PLATFORM_ARM_RPI = y/g' Makefile
```

But for RPI 3 B+ you will need to run those below which builds the ARM64 arch driver:
```
$ sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
$ sed -i 's/CONFIG_PLATFORM_ARM64_RPI = n/CONFIG_PLATFORM_ARM64_RPI = y/g' Makefile
```

For setting monitor mode
  1. Fix problematic interference in monitor mode. 
  ```
  airmon-ng check kill
  ```
  You may also uncheck the box "Automatically connect to this network when it is avaiable" in nm-connection-editor. This only works if you have a saved wifi connection.
  
  2. Set interface down
  ```
  sudo ip link set wlan0 down
  ``` 
  3. Set monitor mode
  ```
  sudo iw dev wlan0 set type monitor
  ```
  4. Set interface up
  ```
  sudo ip link set wlan0 up
  ```
For setting TX power
```
sudo iw wlan0 set txpower fixed 3000
```

### LED control

#### You can now control LED behaviour statically by Makefile, for example:

```sh
CONFIG_LED_ENABLE = n
```
value can be y or n

#### statically by module parameter in /etc/modprobe.d/8812au.conf or wherever, for example:

```sh
options 88XXau rtw_led_enable=0
```
value can be 0 or 1

#### or dynamically by writing to /proc/net/rtl8812au/$(your interface name)/led_enable, for example:

```sh
$ echo "0" > /proc/net/rtl8812au/$(your interface name)/led_enable
```
value can be 0 or 1

#### check current value:

```sh
$ cat /proc/net/rtl8812au/$(your interface name)/led_enable
```

### NetworkManager

Newer versions of NetworkManager switches to random MAC address. Some users would prefer to use a fixed address. 
Simply add these lines below
```
[device]
wifi.scan-rand-mac-address=no
```
at the end of file /etc/NetworkManager/NetworkManager.conf and restart NetworkManager with the command:
```
sudo service NetworkManager restart
```

### Other sources worth checking out
```
new rtw88 mac80211 driver: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/log/rtw88
wireless git: https://git.kernel.org/pub/scm/linux/kernel/git/jh/wireless.git/log/
wireless testing git: https://git.kernel.org/pub/scm/linux/kernel/git/linville/wireless-testing.git/log/
wpa_supplicant git: https://w1.fi/cgit/hostap/log/
