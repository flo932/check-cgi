#!/usr/bin/bash

#echo "$(date)" >> /gotify.log
#printenv > /tmp/gotify.log
#cat /gotify.log
title="$SERVICESTATE $NOTIFICATIONTYPE $HOSTDISPLAYNAME $SERVICEDISPLAYNAME" #=micha_cpu
msg="$LONGDATETIME $SERVICEOUTPUT \n---\n $NOTIFICATIONCOMMENT" 
OUTP="$(echo $SERVICEOUTPUT | head -c 80)"
msg="$LONGDATETIME msg: $NOTIFICATIONCOMMENT $OUTP" 
msg="$LONGDATETIME msg: $NOTIFICATIONCOMMENT $OUTP $SERVICENAME $SERVICEOUTPUT"

# ⚠ ⛔ ❌ ❎ ❗ ❓ 🔶 👍 👎

if [ -z "${title##*CRITICAL*}" ] ;then
    pfx="❗"
elif [ -z "${title##*OK*}" ] ;then
    pfx="👍 "
elif [ -z "${title##*WARNING*}" ] ;then
    pfx="⚠"
elif [ -z "${title##*RECOVER*}" ] ;then
    pfx="✅"
elif [ -z "${title##*UNKNOWN*}" ] ;then
    pfx="❓ "
else
    pfx="-"
fi
title="$pfx $title"

echo "-"
# notification server 1
token=$(head -n1 xxx_gotify.token )
server=$(head -n1 xxx_gotify.server )
curl $server/message?token=$token -F "title=$title" -F "message=$msg" -F "priority=50"
echo "-"
# notification server 2
token=$(head -n2 xxx_gotify.token | tail -n1)
server=$(head -n2 xxx_gotify.server | tail -n1)
curl $server/message?token=$token -F "title=$title" -F "message=$msg" -F "priority=50"
echo "-"
