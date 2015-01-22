#!/bin/bash
#####################################################
#
# Purpose:      For re-enabling SSLv2 in Kali Linux
# Written By:   Eric J. Walker
# Date:         19 Nov 2014
# Version:      0.2
# 
#####################################################
# UPDATES:
# 20 Nov 2014: added a check for needed packages
#
#
######################################################
#Change into TMP directory
cd /tmp
echo -e "---------------------------------------------------------"
echo -e "|                                                       |"
echo -e "|               Script will rebuild OpenSSL             |"
echo -e "|                To remove the SSLv2 patch              |" 
echo -e "|           allow for scanning of client systems        |"
echo -e "|                                                       |"
echo -e "|              YES Clients still run SSLv2!!!!          |"
echo -e "---------------------------------------------------------"

##Check for required packages

PKG1="devscripts"
PKG2="quilt"

for pkg in $PKG1 $PKG2
do
if [ "dpkg-query -W $pkg | awk {'print $1'} = $pkg" ]
then
    echo -e " $pkg is installed "
else
    echo -e " Need to install $pkg "
    apt-get -y install $pkg
    echo "Successfully installed $pkg"
fi
done
######################################################
#       Get OpenSSL Source to rebuild with SSLv2     #
#     This is still needed to test client Systems    #
######################################################
## Get source code
apt-get source openssl

cd openssl*

## remove patches 
quilt pop -a 

## delete ssltest_no_sslv2.patch from debian/patches/series

sed -i '/ssltest_no_sslv2.patch/d' debian/patches/series

## delete no-ssl2 from debian/rules

sed -i 's/no-ssl2//g' debian/rules

## Take a short pause
echo -e "---------------------------------------------------------"
echo -e "|                                                       |"
echo -e "|                  Pausing for a second                 |"
echo -e "|       To let you know this will take a few minutes    |" 
echo -e "|                                                       |"
echo -e "---------------------------------------------------------"

sleep 3

## repatch 
quilt push -a 

## change description for change log
dch -n 'Allow SSLv2'
## commit any changes 
dpkg-source --commit
## rebuild OpenSSL with customizations
debuild -uc -us

cd ..

## Install updated ssl package
dpkg -i *ssl*.deb

####################################################
##          Rebuild SSLSCAN for SSLv2             ##
####################################################
echo -e "    Getting SSLSCAN source    "
echo -e " to rebuild with SSLv2 enabled"
echo -e " "
#Get SSLCSCAN source 
apt-get source sslscan
#CD into sslscan directory
cd sslscan-*
#rebuild SSLSCAN with changes to OpenSSL
debuild -uc -us
#CD back one directory
cd ..
##Reinstall package 
dpkg -i sslscan*.deb
echo -e "---------------------------------------------------------"
echo -e "|                                                       |"
echo -e "|                     We are DONE!!!                    |"
echo -e "|    You can Delete source directories if not needed    |"
echo -e "|                                                       |"
echo -e "---------------------------------------------------------"

cd ~
