# Raspberry_Pi
settings and configuration files for pi

## File System Corruption
* SD cards get corrupted easily during read/write operations due to various reasons like power failure etc. This is a problem when the sdcard contains your OS. In order to increase the life of sd card with OS, boot and root file system can be made read only. Moreover, the /var/log and /tmp folders may be mounted on RAM
* These settings will render your Pi OS stateless.
* To achieve this, fstab configuration is given in fstab_pi file.
* In order to get temporary write access to boot and root partitions, scripts are included in lock_fs folder. This maybe useful to update the OS or change any setting files.


