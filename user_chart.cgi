#!/usr/bin/python

import random
import sys

# Not using the cgi module at the moment.
#import cgi
#import cgitb; cgitb.enable()

from pychart import *
import psycopg2

import csv

data = []

try:
  conn = psycopg2.connect("dbname=openstreetmap user=openstreetmap")
except:
  print "Unable to connect to the database"
  exit

cur = conn.cursor()

sql = "SELECT id, display_name FROM users where display_name <> 'OSMCP'"

cur.execute(sql)

for (id, name) in cur:
    
    sql = "select count(distinct id) from nodes where changeset_id in " + \
          " (select id from changesets where user_id = " + str(id)  + ");"
       
    cur2 = conn.cursor()
        
    cur2.execute(sql)        
        
    e = cur2.fetchone()
    
    for l in e:
        point_total = int(l)
       

    if point_total > 0:
        data.append([name, point_total])

# with...


#
# data should be a list of username, # of points sorted smallest to largest # of points
#
data = sorted(data, key=lambda d: d[1])
#print data
#sys.exit()

from pychart import *

print "Content-type: image/png"
print

sys.argv.append( '--format=png' )

theme.get_options()

ar = area.T( x_coord = category_coord.T(data, 0), 
             y_range = (0, None),
             # NOTE: Added a space between /a90 and %s. If a username starts with a number,
             #       like "4-mapper" it is interpretted as /a904. generating an error
             x_axis = axis.X(label = "User", format = "/a90 %s"),
#             x_axis = axis.X(label = "User", format = "%s"),
             y_axis = axis.Y(label = "Points"),
             legend = None,
             size = (800,400))
             
ar.add_plot(bar_plot.T(data = data))

ar.draw()
