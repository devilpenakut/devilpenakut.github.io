---
layout: post
title: Install Modem Indosatm2 ZTE MF622 di Linux Ubuntu
date: '2008-06-29 12:23:36'
tags:
- indosatm2
- linux
- mf622
- ubuntu
- zte
- hash-import-2024-05-05-07-58
---

Saya memakai modem indosatm2 ini sebelumnya di Windows XP dan Vista berjalan dengan instalasi yang mudah karena modem berjalan secara autorun, setelah selesai modem sudah dapat digunakan. Nah, kemudian saya ingin mencoba di Ubuntu 8.04 saya, dan ternyata tidak semudah itu.he.

Di ubuntu modem ini dideteksi sebagai usb device, yang seharusnya di detect sebagai modem, karena instalasi didalam modem merupakan instalasi untuk windows. Jadi tujuan instalasi ini adalah membuat ubuntu mengidentifikasi MF622 ini sebagai modem, sedangkan untuk dial modemnya merupakan langkah yang biasa dilakuakann ketika dial connection manual.

<!--more-->

Karena saya newbie di Ubuntu maka pastinya saya mencari di google tentang masalah ini, dan menemukan 2 website yang relevan yaitu:

## [Menginstall ZTE MF622 USB Modem di Linux Ubuntu](http://ex3me.org/2008/04/20/menginstall-zte-mf622-usb-modem-di-linux-ubuntu/ "Permanent Link to ")

## [Tutorial Instalasi Modem 3G / HSDPA ZTE MF622 di Linux (Tested in Debian and Ubuntu)](http://dony-ramansyah.blogspot.com/2008/02/tutorial-instalasi-modem-3g-hsdpa-zte.html)

Peratamanya saya menggunakan kedua cara tersebut, namun setelah beberapa kali berusaha yang berhasil adalah cara yang kedua, berikut urutan instalasinya:

1. Modem ditancapkan ke USB **pada saat pertama booting/sebelum PC dinyalakan**. Kenapa harus sejak awal? masalahnya belum di ketahui, karena jika di tancapkan ketika sudah masuk ke Ubuntuk kadang2 modem tersebut tidak terdetect, dari pada harus restart lagi maka lebih baik dari pertama sudah ditancapkan.

2. Agar usb lain selain mf622 dideteksi sebagai usb biasa maka perlu packet modem switch di http://www.draisberghof.de/usb\_modeswitch/usb\_modeswitch-0.9.3.tar.bz2

atau menggunakan dvd repo

**4.Extract file tersebut dengan perintah :  
`$ tar -jxvf usb_modeswitch-0.9..3.tar.bz2`**

```bash
$ ls  
usb_modeswitch-0.9.3.tar.bz2

$ tar -xvjf usb_modeswitch-0.9.3.tar.bz2  
usb_modeswitch-0.9.3/  
usb_modeswitch-0.9.3/compile.sh  
usb_modeswitch-0.9.3/usb_modeswitch  
usb_modeswitch-0.9.3/usb_modeswitch.conf  
usb_modeswitch-0.9.3/usb_modeswitch.c  
usb_modeswitch-0.9.3/usb_modeswitch.h  
usb_modeswitch-0.9.3/COPYING  
usb_modeswitch-0.9.3/README

$ ls  
usb_modeswitch-0.9.3 usb_modeswitch-0.9.3.tar.bz2

$ cd usb_modeswitch-0.9.3/

~/usb_modeswitch-0.9.3$ ls  
compile.sh  
README  
usb_modeswitch.c  
usb_modeswitch.h  
COPYING  
usb_modeswitch  
usb_modeswitch.conf
```

3.Login sebagai root

```bash
$ su atau  
$ sudo su
```

5.Copy file executable “usb\_modeswitch” pada directory “`/sbin`” dan “`/usr/sbin`”

```bash
~/usb_modeswitch-0.9.2# cp usb_modeswitch /sbin/usb_modeswitch  
~/usb_modeswitch-0.9.2# cp usb_modeswitch /usr/sbin/usb_modeswitch
```

6.Copy file “usb\_modeswitch.conf” ke directory “`/etc`”

```bash
~/usb_modeswitch-0.9.2# cp usb_modeswitch.conf /etc/usb_modeswitch.conf
```

7.Buat file rules di `/etc/udev/rules.d/15-zte-mf620.rules` yang berisikan : (rue ini berguna untuk membuat mf622 diddeteksi sebagai modem)

```text
#————————————————–  
ACTION!=”add”, GOTO=”ZTE_End”

# Is this the ZeroCD device?  
SUBSYSTEM==”usb”, SYSFS{idProduct}==”2000″,  
SYSFS{idVendor}==”19d2″, GOTO=”ZTE_ZeroCD”

# Is this the actual modem?  
SUBSYSTEM==”usb”, SYSFS{idProduct}==”0001″,  
SYSFS{idVendor}==”19d2″, GOTO=”ZTE_Modem”

LABEL=”ZTE_ZeroCD”  
# This is the ZeroCD part of the card, remove  
# the usb_storage kernel module so  
# it does not get treated like a storage device  
#RUN+=”/sbin/rmmod usb_storage”  
RUN+=”/usr/sbin/usb_modeswitch -d 1 -v 0x19d2 -p 0x2000 -V 0x19d2 -P 0x0001″

LABEL=”ZTE_Modem”  
# This is the Modem part of the card, let’s  
# load usbserial with the correct vendor  
# and product ID’s so we get our usb serial devices  
RUN+=”/sbin/modprobe usbserial vendor=0x19d2 product=0x0001″,  
# Make users belonging to the dialout group  
# able to use the usb serial devices.  
MODE=”660″, GROUP=”dialout”

LABEL=”ZTE_End”  
#——————– eof —————
```

Pastikan permision filenya sama dengan rule yang lain. # `chmod 644 15-zte-mf622.rules`

8.Pastikan Anda telah menginstall wvdial di Linux, (di Debian atau Ubuntu tinggal install melalui `apt-get` atau melalui Synaptic).

```bash
# apt-get install wvdial
```

9.Buat script di `/etc/wvdial.conf` berisikan : ( **user name** dan **password** diisi sesuai user name masing2)

```ini
[Dialer Defaults]  
Modem = /dev/ttyUSB0  
Baud = 3600000  
Init1 = ATZ  
Init2 = ATQ0 V1 E1 S0=0 &C1 &D2  
Init3 = AT+CGDCONT=1,”IP”,”indosatm2″  
Area Code =  
Phone = *99#  
Username =  
Password =  
Ask Password = 0  
Dial Command = ATDT  
Stupid Mode = 1  
Compuserve = 0  
Force Address =  
Idle Seconds = 0  
DialMessage1 =  
DialMessage2 =  
ISDN = 0  
Auto DNS = 1  
```
  
10. Restart Linux anda sekarang

11. Jalankan program wvdial nya :
{: start="10"}

```bash
# wvdial  
```

```text
WvDial<*1>: WvDial: Internet dialer version 1.56  
WvModem<*1>: Cannot get information for serial port.  
WvDial<*1>: Initializing modem.  
WvDial<*1>: Sending: ATZ  
WvDial Modem<*1>: ATZ  
WvDial Modem<*1>: OK  
WvDial<*1>: Sending: ATQ0 V1 E1 S0=0 &C1 &D2  
WvDial Modem<*1>: ATQ0 V1 E1 S0=0 &C1 &D2  
WvDial Modem<*1>: OK  
WvDial<*1>: Sending: AT+CGDCONT=1,”IP”,”indosatm2″  
WvDial Modem<*1>: AT+CGDCONT=1,”IP”,”indosatm2″  
WvDial Modem<*1>: OK  
WvDial<*1>: Modem initialized.  
WvDial<*1>: Sending: ATDT*99#  
WvDial<*1>: Waiting for carrier.  
WvDial Modem<*1>: ATDT*99#  
WvDial Modem<*1>: CONNECT  
WvDial<*1>: Carrier detected. Starting PPP immediately.  
WvDial: Starting pppd at Mon Feb 11 01:06:45 2008  
WvDial: Pid of pppd: 14291  
WvDial<*1>: pppd: H�  
WvDial<*1>: Using interface ppp0  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: pppd: H�  
WvDial<*1>: local IP address 124.81.144.28  
WvDial<*1>: pppd: H�  
WvDial<*1>: remote IP address 10.64.64.64  
WvDial<*1>: pppd: H�  
WvDial<*1>: primary DNS address 202.155.0.10  
WvDial<*1>: pppd: H�  
WvDial<*1>: secondary DNS address 202.155.0.15  
WvDial<*1>: pppd: H�
```

Jika muncul seperti diatas berarti kita sudah terkoneksi dengan 3G HSDPA dan sudah mendapatkan IP maupun DNS.

**9. Selesai =)**

Kestabilan koneksi di ubuntu ternyata lebih baik dari pada di windows, sering kali di windows koneksi terputus karena ada gangguan driver, ternyata di ubuntu sampai dengan saat ini lancar, kecuali jika lama tidak ada akses maka koneksi akan terputus sendiri.

<!--kg-card-end: html-->