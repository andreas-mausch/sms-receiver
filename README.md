Small tool to receive SMS text messages from a USB modem.

# Requirements

## Modeswitch

```bash
sudo usb_modeswitch -v 0x12d1 -p 0x1446 -V 0x12d1 -P 0x1436 -M 55534243123456780000000000000011062000000100000000000000000000
```

## Gammu

```bash
sudo apt-get install gammu-smsd
cp ./gammu-smsdrc /etc/
```

You might need to change the *port* and the *RunOnReceive* line in */etc/gammu-smsdrc*.  
Then restart.

## Mongo

Install and run mongo. Make sure it starts on boot.

See *mongo-start.sh*.

Change the mongodb uri in *receive.py* and *website.py*.

## iptables

You might need to change your iptables rules in order to access the webserver.

# Run

Gammu should automatically start on boot.

It calls the python script which writes the data into the mongodb database.

Run this:

```bash
python website.py
```

to start the flask server. Then navigate to it via a browser to see the received SMS.

# Security

This started as a local git repo, that's why you find passwords in the git history for the mongo connection string.  
I am aware of this and have changed them. ;)

# Debug

```bash
cat /var/log/syslog  | grep gammu
sudo ls -l /var/spool/gammu/inbox/
sudo ls -l /var/spool/gammu/error/
ls -l /dev/ttyU*
ls -l /dev/ttyUSB1
ls -l /dev/serial/by-id/usb-HUAWEI_Technology_HUAWEI_Mobile-if00-port0
dmesg | grep ttyUSB
```
