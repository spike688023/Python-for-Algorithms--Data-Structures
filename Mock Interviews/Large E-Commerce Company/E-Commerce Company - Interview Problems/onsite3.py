def overlap(r1,r2):
    see_x , see_y = False, False

    ru_min = min( r1['x'] + r1['w'] , r2['x'] + r2['w'])
    lb_max = max( r1['x'], r2['x'])

    if ru_min > lb_max: see_x = True

    ru_min = min( r1['y'] + r1['h'] , r2['y'] + r2['h'])
    lb_max = max( r1['y'], r2['y'])

    if ru_min > lb_max: see_y = True


    print "see_x = " + str(see_x)
    print "see_x = " + str(see_y)

    if see_x and see_y : 
        print "overlap!"
        return True
    else: 
        print "not overlap!"
        return False

# overlap case
r1 = { 'x': 2 , 'y': 4,'w':5,'h':12}
r2 = { 'x': 3 , 'y': 5,'w':5,'h':8 }
print overlap(r1,r2)

# nonoverlap
r3 = { 'x': 1 , 'y': 1,'w':1,'h':1}
r4 = { 'x': 3 , 'y': 3,'w':1,'h':1 }
print overlap(r3,r4)
