import re
import urllib2

url = raw_input("Enter the website URL: ")
html = urllib2.urlopen(url).read()
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html)

if len(emails) > 0:
    for email in emails:
        print(email)
else:
    print("No emails found.")
