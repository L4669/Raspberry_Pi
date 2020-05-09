#!/bin/sh
# make the boot partition writable
# for updating kernels
# argument for grep command may change. check with mount command.
# the effect of this script is temporary. 
# check /etc/fstab file to find out the default options at boot time

mount -o remount,rw $(mount | grep " on /boot/firmware " | awk '{print $1}')
