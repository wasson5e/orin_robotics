# Rebuilding Steps

## SSD
1) Burn the SSD using the images from Nvidia using Etcher
2) Reinstall the SSD and boot the Nano using the SDCard with the working image
3) Create a mount folder in the Documents folder
```
sudo mount /dev/nvme0n1p1 <mountFolder>
```

4) Update the boot information
```
vim /boot/extlinux/extlinux.conf
```
Change root to `APPEND ${cbootargs} root=/dev/nvme0n1p1`
5) Shutdown the Nano, and remove the SDCard
6) Boot nano and finish installation

## Fix Browser Issue - if there
```
sudo snap download snapd --revision=24724
sudo snap ack snapd_24724.assert
sudo snap install snapd_24724.snap
sudo snap refresh --hold snapd
```

## SSH Keys for github
`ssh-keygen`