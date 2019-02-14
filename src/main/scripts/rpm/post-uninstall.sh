#!/bin/sh

echo "Running post-uninstall script" $@

if [ $1 == 0 ]; then # this is an uninstall
    rm -rf /opt/mit500/m1
fi