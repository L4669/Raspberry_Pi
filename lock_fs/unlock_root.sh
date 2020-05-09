#!/bin/sh
# remount the file system to support read/write operations
# in case of any update or tweak any files
# the effect of this script is temporary.
# check /etc/fstab file to find out the default options at boot time

mount -o remount,rw $(mount | grep " on / " | awk '{print $1}')
