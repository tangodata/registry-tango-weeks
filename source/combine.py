#!/usr/bin/python

import yaml
import os
import fnmatch
import datetime

# take x, push it into arrays of that country
def process2(x) :
  # weeks = {}
  c = x.pop('country')
  if (c not in weeks) :
    weeks[c]=[]
  weeks[c].append(x)

# output decoratively
def dumpdata(m) :
  i=0
  for item in weeks:
    print ("%s-%s : %s" % (item['country'], item['city'], item['longname'])),
    i=i+1
    if (m in item):
      thisyear = item[m]
      sd=thisyear['startdate']
      ed=thisyear['enddate']
      print sd.strftime('%Y-%m-%d'),'-',
      print ed.strftime('%Y-%m-%d'),'==',
      print sd.isocalendar()[1],
    print
  print 'Total (%s)' % i




weeks = []
def process(x) :
  weeks.append(x)

rootdir = './series/'
pattern = '*.yml'

# start at the root of repo by calling 'source/combine.py'
for dirname, subdirlist, filelist in os.walk(rootdir):
  print ('goto %s' % dirname)
  for fname in fnmatch.filter(filelist,pattern):
    print ('\t%s' % fname)
    with open(dirname+'/'+fname,'r') as stream:
      try:
        x= yaml.safe_load(stream)
        process(x)
      except yaml.YAMLError as exc:
        print (exc)

print "===============\n"
dumpdata('y2020')
