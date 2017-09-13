from nose.tools import assert_equal

class AnagramTest(object):

    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

def anagram(s1,s2):
    set1 = set( iter( s1.replace(' ', '').lower() ) )
    set2 = set( iter( s2.replace(' ', '').lower() ) )
    if set1 != set2:
        return False
    else:
        for i in set1:
            if s1.count(i) != s2.count(i):
                return False
        return True
    #print(s1.replace(' ', ''))
    # 下面二行 的輸出，不會變，因為str 是 immutable，這裡是call by value
    #print(s1)
    #print(s2)


#print( anagram('go go go','gggooo') )
# Run Tests
t = AnagramTest()
t.test(anagram)

"""
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"

    Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".


不用管大小寫，也不用管空白， 我會先白空白都給 處 理掉，

然後 用set 去存這二個，再用set 比較，應該 就 可以解決問題 了吧，

但跟array 好像沒什麼關 係丫。

大小寫不用管，那可能要全部轉 小寫來比。

作者第二個解法，跟我用set 的方法很像，但，我的比較好吧。

"""


"""
>>> type({})
<class 'dict'>
>>> type(set())
<class 'set'>
"""
