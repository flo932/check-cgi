
# SPDX-License-Identifier: GPL-2.0-only
# - flo932@uxsrv.de micha.r

#www-data ALL=(ALL:ALL) NOPASSWD:/opt/check/check_mount.sh
#master ALL=(ALL:ALL) NOPASSWD:/opt/check/check_mount.sh


#su - master -c 'python3 /opt/check/check_mount.py'
su - user -c 'python3 /opt/check/check_mountB.py'
