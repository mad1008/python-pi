
def dispatch(url):
	return url.split("/")

def message(msg):
	print(msg)

def add(*args):
	z=0
	for a in args:
		try:
			z+=a
		except:
			print(str(a),"is not a number")
	return(z)


print("Test add func",add(5,2,33,33,"t"))
print("Test dispatch func",dispatch("home/user/projects/file.txt"))