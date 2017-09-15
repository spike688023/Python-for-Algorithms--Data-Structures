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
    list1 = s.strip().split()
    # 我想到了, 針對每個拆出來的元素, 再做一次strip
    print(list1[::-1])
    #print( ' '.join(list1[::-1]) )
    return ' '.join(list1[::-1])

"""
While these are valid solutions, in an interview setting you'll have to work out the basic algorithm that is used. In this case what we want to do is loop over the text and extract words form the string ourselves. Then we can push the words to a "stack" and in the end opo them all to reverse. Let's see what this actually looks like:
"""

def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))
    
    
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

告夭, 我自己把sep 給寫進去, 反倒不好, 

因為預設不給它, 它會把所有的 whitespace 都當成一個給拿掉, 

我就不用為了空的元素, 再處理一次了.

 |  split(...)
 |      S.split([sep[, maxsplit]]) -> list of strings
 |
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
"""
