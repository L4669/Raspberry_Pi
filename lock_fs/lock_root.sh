#!/bin/sh
# locks the root file system as read only
# to avoid any write operation on file system and avoid corruption
# the effect of this script is temporary.
# check /etc/fstab file to find out the default options at boot time

mount -o remount,ro $(mount | grep " on / " | awk '{print $1}')
