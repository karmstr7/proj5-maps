#! /bin/bash
#
# Kill all current instances of flask_maps on this machine
#
#

# Grep for all running processes containing flask_maps in description
# EXCEPT the grep command itself; turn them into 'kill' commands and
# execute the commands with bash
#
ps -x | grep flask_maps | grep -v grep | \
    awk '{print "kill " $1}' | bash


