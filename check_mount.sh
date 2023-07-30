
#www-data ALL=(ALL:ALL) NOPASSWD:/opt/check/check_mount.sh
#master ALL=(ALL:ALL) NOPASSWD:/opt/check/check_mount.sh

su - master -c 'python3 /opt/check/check_mount.py'
