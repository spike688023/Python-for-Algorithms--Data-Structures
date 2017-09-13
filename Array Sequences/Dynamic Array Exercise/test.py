class M(object):
    
    def public(self):
        print 'Use Tab to see me!'
        
    def __private(self):
        print "You won't be able to Tab to see me!"


m = M()
m.public()

dir(m)
