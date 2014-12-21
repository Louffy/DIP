import os
import sys
import urllib2
re=urllib2.urlopen("https://code.google.com/feeds/issues/p/chromium/issues/full/3")
text=re.read()
print text