
# coding: utf-8

# # Unique Characters in String
# 
# ## Problem
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

# ## Solution
# Fill out your solution below:
# 這題呢， 用set 以及count 一下就 寫出來了，
# 
# 但是 count 每呼叫一次，就 是  對全部的資料掃過一次，
# 
# 這個問題 一定是要你只掃一次。
# 
# 一用排序，時間複雜度就 會掉到 nlogn .
# 
# 還是說用字典 O(cn)

# In[6]:

def uni_char(s):
    if s == "": return True
    dict1 = {i:0 for i in set(s)}
    for i in s:
        dict1[i] += 1
        if dict1[i] == 2:return False
    print dict1
    return True


# # Test Your Solution

# In[7]:

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)


# ## Good Job!
