#!/bin/bash

echo "What is the domain name?"
read domain

dig "$domain"


#Attempt a DNS zone transfer (if allowed)

#dig axfr @<dns_server_IP> <domain_name>