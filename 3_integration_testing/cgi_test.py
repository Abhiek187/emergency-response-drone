# Written and Debugged by: Abhishek Chaudhuri
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
'''import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello World!")

print("Content-type: text/html")
print()
with open('../Location/SEtest.html') as f:
  print(f.read())'''

#!/usr/bin/python3

import requests as req

url = "https://abhiek187.github.io/emergency-response-drone/1_code/Location/SEtest.html"
resp = req.get(url)

if resp.status_code == 200:
	print(resp.text)
else:
	print("{} is unavailable.".format(url))

'''data = {'data': 'Hello World!'}
resp2 = req.post(url, data)
print(resp2.text)'''
