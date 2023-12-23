import sys
import requests


if (__name__ == "__main__"):
	url  = sys.argv[1]
	name = sys.argv[2].replace(".safetensors", "")
	with open(name + ".safetensors", "wb") as fp:
		rsp = requests.get(url)
		if (rsp.status_code == 200):
			fp.write(rsp.content)
