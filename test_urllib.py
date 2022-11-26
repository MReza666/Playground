import urllib.request, urllib.parse, urllib.error

uhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in uhandle:
    print(line.decode().rstrip())
