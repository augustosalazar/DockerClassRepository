#!/bin/bash
# Script to add a user to Linux system
read -p "Web port: " webPort
read -p "php-apache 1 , nodejs 0: " webType
if [$webType -eq 1]; then
    echo "PHP"
    
else
    echo "NodeJs"
    
fi