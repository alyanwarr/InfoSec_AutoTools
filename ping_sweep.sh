#!/bin/bash

subnet=$(ip -o -f inet addr show | awk '/scope global/ {print $4}');
echo "[-] Scanning Subnet:  "$subnet;
now=$(date +%Y_%m_%d_%H_%M);
filename="ping_sweep_$now"
nmap -sP $subnet -n --max-rtt-timeout 50ms -oG - | awk '/Up$/{print $2}' > $filename;
echo "[-] Results saved to $(pwd)/$filename";
read -p "[-] View Results? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    cat $filename
fi
