#! /bin/sh

##
# Credit
# https://github.com/leosartaj/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# The directory where the uninstall.sh script is kept
SCRIPT_DIR=$(readlink -f ${0%/*})

# Path to install
path=/usr/local/credit

if [ -d "$path" ]
then
    rm -rf "$path"
    rm -f /usr/bin/credit
else
    echo 'Credit is not installed yet. Use install.sh to install.'
fi
