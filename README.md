## python simple cgi monitoring script's
```
I do not want to use a monitoring-agent 
on various systems/servers

I prefer to use simple python-cgi scritps to request
system status like disk,zfs,memory,cpu...

you can also request system status with curl
but you have to calculate the token first (psk)

```

## setup / install
```
#install jq (json) pkg 
apt install jq

# clone the repo to /opt/check/
cd /opt/
git clone https://github.com/flo932/check-cgi.git check

cd /opt/check/
# create a psk/password 
pwgen -n 30 -c 1 > psk
# copy this to icinga2 and other nodes
# to /opt/check/psk or /etc/icinga2/scripts/xxx_psk

# install a webserver with cgi enabled
# then link the www dir
ln -s /opt/check/www /var/www/html/sys/

# check if cgi scritp's availibel
curl ip-addresse/sys/
# should return 
>  system

# some scripts in /opt/check/check_x.py need root on the system
# setup sudo / visudo like
...

# on icinga2 monitoring node
# copy scripts/* to icinga2/scritps/
rsync -apv /opt/check/scripts/ /etc/icinga2/scripts/

# edit icinga2 config ..
vi /etc/icinga2/conf.d/host.conf
...

```

## file structur
```

```


