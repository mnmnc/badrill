badrill
=======

Basic Authentication DRILL

** BASH version available.

** Python version in alpha.

Originally created to search for routers with default password and management http interface publicly available, although can be used agains any server protected with basic authentication.

This script assumes you have a list of ip addresses stored in one file and list of username:password pairs in the other. There are some variables within the script itself which allow you to limit the search to the hosts that respond to ICMP echo requests or display only those IP’s that responded to ping. This is designed such way because some hosts might not respond to ICMP echo request and still have open port 80.

Example content of username:password file:

    admin:admin
    admin:password
    admin:
    ADSL:expert03
    ZXDSL:ZXDSL
    admin:administrator
    admin:comcast
    admin:1234

Here is script output produced when displaying all IPs and their statuses:

![Finding routers with default password](https://raw.githubusercontent.com/mnmnc/img/master/full2.png)


..and the other output displaying only alive ones:

![Finding routers with default password](https://raw.githubusercontent.com/mnmnc/img/master/active2.png)

* `ALIVE` means host responded to ping.
* `200` means HTTP server response on port 80 was HTTP/1.* 200 OK.
* `401` means HTTP server requested authorisation – this is what we are looking for.

Vertical bars after 401 status indicate username:password pairs used to authenticate. If correct pair is found – it is displayed after PASS.
