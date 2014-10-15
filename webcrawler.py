#!/usr/bin/env python

import urllib2

# get source code from a specific website
url = 'http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=262' # write URL here
      
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read() 
# print the_page # test if fetch source code successfully
# end - get source code


# output source code to a temp file
file = open("temp.txt", "w")
print "Name of the file: ", file.name

for line in the_page:
    file.write(line)

file.close()
# end - output temp file