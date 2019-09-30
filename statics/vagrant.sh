#!/bin/bash

sudo fuser -vu /var/lib/dpkg/lock

sudo rm -v /var/lib/dpkg/lock

sudo dpkg --configure -a

dir=`ls /media/`

sudo dpkg -i /media/$dir/Vini/virtualbox_5.2.32-dfsg-0~ubuntu18.04.1_amd64.deb --force

sudo dpkg -i /media/$dir/Vini/vagrant_2.0.2+dfsg-2ubuntu8_all.deb --force

sudo apt --fix-broken install -y

vagrant --version
