## python simple cgi monitoring script's

to get informations about a system
- server's
- Proxmox


## setup / install
```
#install jq (json) pkg 
apt install jq

# clone the repo to /opt/check/
cd /opt/
git clone https://github.com/flo932/check-cgi.git check

cd /opt/check/
# create a psk/password 
# copy this to icinga2 and other nodes
pwgen -n 30 -c 1 > psk

# install a webserver with cgi enabled
# then link the www dir
ln -s /opt/check/www /var/www/html/sys/

# check if cgi scritp's availibel
curl ip-addresse/sys/
# should return 
no token

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


