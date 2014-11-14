#! /bin/sh

##
# Credit
# https://github.com/leosartaj/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# The directory where the install.sh script is kept
SCRIPT_DIR=$(readlink -f ${0%/*})

INSTALL_DIR=/usr/local/credit

if [ ! -d $INSTALL_DIR ]
then
    mkdir $INSTALL_DIR           # Make directory if directory does not exist
fi

# Install files
install -m 0755 "$SCRIPT_DIR/scripts/credit" "/usr/bin/" # Copy the credit script
install -m 0755 "$SCRIPT_DIR"/src/*.py "$INSTALL_DIR"
