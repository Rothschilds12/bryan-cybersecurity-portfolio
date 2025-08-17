#!/bin/bash

#List available SMB shares (requires no password for anonymous access, or -U for user)

echo "Anonymous Access: y/n  (yes/no)"
read anonymous
echo "What is the target ip"
read target

if [ "$anonymous" =  "y" ]; then
  smbclient -L //"$target" / -N
else
  echo "What is the username?"
  read username
  smbclient -L //"$target" / -U "$username"
fi