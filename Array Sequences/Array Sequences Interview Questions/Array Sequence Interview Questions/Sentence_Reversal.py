"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")

def rev_word(s):
    #print(s.strip())
    list1 = s.strip().split(' ')
    # 我想到了, 針對每個拆出來的元素, 再做一次strip
    print(list1[::-1])
    list2 = []
    for i in range( len(list1) ):
        if list1[i] != "": list2.append( list1[i] )
    print(list2[::-1])
    #print( ' '.join(list1[::-1]) )
    return ' '.join(list2[::-1])
    
    
print( rev_word('   Hi John,   are you ready to go?  ') )

# Run and test
t = ReversalTest()
t.test(rev_word)


"""
 |  join(...)
 |      S.join(iterable) -> str
 |
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
"""
