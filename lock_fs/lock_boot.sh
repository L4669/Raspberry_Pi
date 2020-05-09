#!/bin/sh
# make the boot partition read-only
# to avoid any write operations to fs and avoid any corruption
# argument for grep may change. check with mount command
# the effect of this script is temporary. 
# check /etc/fstab file to find out the default options at boot time

mount -o remount,ro $(mount | grep " on /boot/firmware " | awk '{print $1}')
