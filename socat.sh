#!/bin/bash
# A script to read a.a.m over tor with aampy, socat, and stunnel
#
# usage: ./socat.sh <news server address>

if [ $1x = "x" ]; then
  echo "Usage: ./socat.sh <news server address>"
  exit 0
fi

# To use aampy securely with stunnel over tor, there are three ports of interest:
#  1) 119 - un-ssl'd news port aampy reads from
#  2) 10063 - stunnel maps from 119 to 10063 (you need to run an stunnel instance for this)
#  3) 563 - port used by news server (socat maps from 10063 to this port via tor)
#
# Your stunnel.conf file should include this:
#  [aampy]
#  client = yes
#  accept = 127.0.0.1:119
#  connect = 127.0.0.1:10063

NEWS_SERVER_PORT=563
NEWS_CLIENT_PORT=10063

socat TCP4-LISTEN:$NEWS_CLIENT_PORT,fork SOCKS4A:localhost:$1:$NEWS_SERVER_PORT,socksport=9050 &
