#!/bin/sh
echo starting ssh connection...
ssh -i /home/pi/.ssh/amazon_key.pem -N -g -R :7070:localhost:7070 ec2-user@tesseract-aws.ddns.net &
echo starting sever...
python ./serverjq/PiBot_remote_control.py