#!/usr/bin/env python
# Detect Domain Parked on IP
# Written by ToToDoDo (QQ:8924007) Email: plone2#yahoo.com.cn
import sys,urllib,re,string

ip = '114.255.238.233';

#try:
#    ip = sys.argv[1]
#    ip = '114.255.238.233';
#except:
#    print 'U must supply a IP U want to check'
#    sys.exit(1)
try:
    urlfile = urllib.urlopen('http://whois.webhosting.info/'+ip)
except IOError,msg:
    print "Error:",url,":",msg
    sys.exit(1)

htmlcodes = urlfile.read()
m = re.search('The IP Address entered by you is InValid',htmlcodes)
if  m != None:
    print 'The IP Address entered by you is InValid!!!'

n = re.search('IP Details - N/A.',htmlcodes)
if  m != None:
    print ip,'- IP Details - N/A.'

if re.search('Domains ...',htmlcodes) or re.search('Total Domains',htmlcodes):
    print "Check Successful!"
    splitcodes = string.join([string.strip(ip),'</b> - IP hosts <b>'],'')
    result1 = re.split(splitcodes,htmlcodes)
    _logfile = open('domain.txt','w');
    _logfile.writelines(result1)
    _logfile.close()
    print result1
    if len(result1) <= 1:
        print 'not found'
        sys.exit(1)
    else:
		print len(result1[0])
    result2 = re.split('</b> Total',result1[1])
    print "Found ",result2[0],"domains on this IP "
    result3 = re.split('<td><a href="webhosting.info/',result2[1])#">http://whois.webhosting.info/',result2[1])
    for x in result3[1:]:
        y = re.split('.">',x)
        print y[0]
else:
    print "Sorry, Error to complete check!"