#!/bin/bash

echo "Enter target username"
read username
echo "Enter target ip"
read address

ssh "$username"@"$address"

#You will be prompted for the password