#!/bin/bash

echo "Enter target ip"
read target
echo "You target $target"
nmap -p 21 --script ftp-anon "$target"

