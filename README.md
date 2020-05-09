# Raspberry_Pi
settings and configuration files for pi

## File System Corruption
* SD cards get corrupted easily during read/write operations due to various reasons like power failure etc. This is a problem when the sdcard contains your OS. In order to increase the life of sd card with OS, boot and root file system can be made read only. Moreover, the /var/log and /tmp folders may be mounted on RAM and swap file can be disabled.
* These settings will render your Pi OS stateless.
* To achieve this, fstab configuration is given in fstab_pi file.
* In order to get temporary write access to boot and root partitions, scripts are included in lock_fs folder. This maybe useful to update the OS or change any setting files.
* Change the settings for PiHole, Plex and Nextcloud to use external usb for log files and other data storage.
* Plex Server Setting
```
  $ sudo mv /var/lib/plexmediaserver <external usb>
  $ sudo ln -s <absolute path of plex folder on external usb> /var/lib
```
* Pi hole logging to external usb. Edit /etc/pihole/logrotate
```
/mnt/usb2/log/pihole.log {
	su root syslog
	daily
	copytruncate
	rotate 5
	compress
	delaycompress
	notifempty
	nomail
}

/mnt/usb2/log/pihole-FTL.log {
	su root syslog
	weekly
	copytruncate
	rotate 3
	compress
	delaycompress
	notifempty
	nomail
}
```

