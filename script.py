import sys
import requests

CHUNK_SIZE = 8192

def create_directory_of(filename):
	dirname = ""
	for item in filename.split("/")[:-1]:
		dirname += item + "/"
		try:
			os.mkdir(dirname)
			return (True)
		except:
			pass
	return (False)

def download_large_file(url, destination_path):
	create_directory_of(destination_path)
	try:
		response = requests.get(url, stream = True)
		response.raise_for_status()
		size = 0
		with open(destination_path, 'wb') as file:
			for chunk in response.iter_content(chunk_size = CHUNK_SIZE):
				if chunk:
					file.write(chunk)
				size += len(chunk)
				print("DOWNLOADING[" + str(size) + "]...")
	except requests.exceptions.HTTPError as e:
		print("HTTP error occurred: " + str(e))
	except Exception as e:
		print(f"An error occurred: " + str(e))

if (__name__ == "__main__"):
	if (len(sys.argv) < 2):
		print("usage: <script> <url> <filename>")
		exit()
	url  = sys.argv[1]
	if (len(sys.argv) > 2):
		name = sys.argv[2]
	else:
		try:
			name = url.lower().split(".safetensors")[-2].split("/")[-1]
		except:
			name = ""
	for k in "\r\t\n\v\f ":
		name = name.lower().replace(k, "")
	name = name.replace(".safetensors", "") + ".safetensors"
	download_large_file(url, name)
