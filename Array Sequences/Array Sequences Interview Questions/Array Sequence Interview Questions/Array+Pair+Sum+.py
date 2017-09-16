
# coding: utf-8

# # Array Pair Sum
# 
# ## Problem
# 
# Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.
# 
# So the input:
#     
#     pair_sum([1,3,2,2],4)
# 
# would return **2** pairs:
# 
#      (1,3)
#      (2,2)
# 
# **NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**
# 
# ## Solution
# 
# Fill out your solution below:

# 目前的想法是，用一個相等大小的list 去存，True False，
# 能找到另一半就 把二個給 True ， 而且count++ ，
# 
# 找不到另一半的話， 一樣要給 True , 但count 不能加加。
# 
# 演算法的時間，大概是落在  nlogn.
# 
# 我怎麼覺得  find 這個功能可以用 dict 去實作，value 就 放index的位置 。
# 
# 又想到另一個實作的方法了，用dict ，去記録每個key的數目，每配到一次，
# 
# 就減1。
# 
# 用dict.keys() 去判斷有沒有另一半。
# 
# 我也要試 著去評估，我演算法的時間複雜度，
# 
# 我光是 建dict1 就 Quadratic time.
# 
# Big-O	Name
# 1	Constant
# log(n)	Logarithmic
# n	Linear
# nlog(n)	Log Linear
# n^2	Quadratic
# n^3	Cubic
# 2^n	Exponential
# 
# 在 dict1.keys() 裡面找東西，要當binary search 當 log time or 
# 
# linear time search.

# In[11]:

def pair_sum(arr,k):
    count = 0
    dict1 = {i:arr.count(i) for i in set(arr)}
    print dict1
    for i in arr:
        # find the other
        if k-i in dict1.keys() and dict1[i] > 0 and dict1[k-i] > 0:
            count += 1
            dict1[i] -= 1
            dict1[k-i] -= 1
        else:
            dict1[i] -= 1
    return count
            


# In[12]:

pair_sum([1,3,2,2],4)


# # Test Your Solution

# In[13]:

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print 'ALL TEST CASES PASSED'
        
#Run tests
t = TestPair()
t.test(pair_sum)
    


# ## Good Job!
