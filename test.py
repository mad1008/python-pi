
def dispatch(url):
	return url.split("/")

def message(msg):
	print(msg)

print(dispatch("home/user/projects/file.txt"))