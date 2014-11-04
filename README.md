badrill
=======

### Basic Authentication DRILL

* Python version available. 
* BASH version available. |Deprecated|

-----
### Description

Originally created to **search for routers with default password** and management http interface publicly available, although can be used agains any server protected with **basic authentication**.

This script assumes you have a list of **ip addresses** stored in one file and list of **username:password** pairs in the other.

Example content of username:password file:

    admin:admin
    admin:password
    admin:
    ADSL:expert03
    ZXDSL:ZXDSL
    admin:administrator
    admin:comcast
    admin:1234

## badrill.py

Standard output with elements explained:
```python
 15:03 > python .\badrill.py
 #
 # IP           HTTP_CODES  ATTEMPTS   PAGE TITLES
 #
 
 155.x.x.16         4         |        SUCCESS:  admin:admin
 155.x.x.17         4         ||       401 Error
 155.x.x.26         4         ||       401 Error
 155.x.x.27         32                 Authentication Page
 155.x.x.10         32                 -
 155.x.x.199        2                  -
 155.x.x.95         2                  -
 155.x.x.104        2                  -
```

Options available:
```python 
 15:07 > python .\badrill.py -h
 
usage: badrill.py [-h] [-q] [-m] [-i iplist] [-a authlist]

optional arguments:
  -h, --help                            show this help message and exit
  -q, --quiet                           If quiet is set, html>title will not be shown.
  -m, --mute                            Do not show each attempt of authentication.
  -i iplist, --iplist iplist            Override path to file that contains ip list.
  -a authlist, --authlist authlist      Override path to file that contains username:password pairs.
  
```


Minimal view:
```python
 15:08 > python .\badrill.py -mq

 155.x.x.16         4       SUCCESS:  admin:admin
 155.x.x.17         4
 155.x.x.26         4
 155.x.x.27         32
 155.x.x.10         32
 155.x.x.199        2
 155.x.x.95         2
 155.x.x.104        2
```


-----
## badrill.sh

### Note: 
There are some variables within the script itself which allow you to limit the search to the hosts that respond to ICMP echo requests or display only those IP’s that responded to ping. This is designed such way because some hosts might not respond to ICMP echo request and still have open port 80.

### Variables

```bash
ips=`cat ip.list`       # File with list of IPs
users=`cat users.list`  # File with list of username:password pairs
PING_CHECK=0            # whether to check if there is a ping response
DISPLAY_DEAD=1          # whether to show those that did not respond to ping
```

Here is script output produced when displaying all IPs and their statuses:

![Finding routers with default password](https://raw.githubusercontent.com/mnmnc/img/master/full2.png)


..and the other output displaying only alive ones:

![Finding routers with default password](https://raw.githubusercontent.com/mnmnc/img/master/active2.png)

* `ALIVE` means host responded to ping.
* `200` means HTTP server response on port 80 was HTTP/1.* 200 OK.
* `401` means HTTP server requested authorisation – this is what we are looking for.

Vertical bars after 401 status indicate username:password pairs used to authenticate. If correct pair is found – it is displayed after PASS.
