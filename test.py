import re
txt='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
ext=re.findall('\S+@\S+', txt)
print(ext)
