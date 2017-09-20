
# coding: utf-8

# # Largest Continuous Sum
# 
# ## Problem
# Given an array of integers (positive and negative) find the largest continuous sum. 
# 
# ## Solution
# 
# Fill out your solution below:

# 這題 的想法不是很明確， 
# 
# 先把Local_max 給抓出來， 以負數為分隔點，把各個區塊的正數先抓出來，
# 
# 用個字典紀録 local_max 的最大值，以值區間，區間怎麼抓還不知道，
# 
# 但Local_max 只要遇到正數就加總，遇到負數就歸零，再跟之前的Local_max比，看要不要
# 
# 蓋過去。
# 
# 感覺是要你抓出Global max 的值，跟範圍，我先抓Local好了。
# negative_point 用來記上次，負值的index.
# 
# 先抓出個local_max, 用做比對的基準，只要超過這個值，就是最新的global_max_sum.
# 
# 哈，看來是用不到 local_max，直接比較好了。

# In[40]:

def large_cont_sum(arr): 
    
    start_point = 0
    end_point = 0
    negative_point = -1
    local_max_sum = 0
    current_sum = 0
    global_max_sum = 0
    
    
    if len(arr) == 0: return 0
    
    for i in range( len(arr) ):
        if arr[i] > 0:
            current_sum += arr[i]
        else:
            if current_sum > 0 and current_sum > local_max_sum: 
                local_max_sum = current_sum
                current_sum = 0
        
    #return local_max_sum  
    print "local_max_sum =" + str(local_max_sum)
    
    current_sum = 0
    for i in range( len(arr) ):
        if arr[i] > 0:
            current_sum += arr[i]
        else:
            current_sum += arr[i]
            if current_sum < 0:
                current_sum = 0
                negative_point = i
                
        if current_sum > global_max_sum:
            global_max_sum = current_sum
            end_point = i
            if negative_point >= 0:
                start_point = negative_point + 1
    
    print "start_point = " + str(start_point)
    print "end_point = " + str(end_point)
    return global_max_sum  

                
    


# In[38]:

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])


# ____
# Many times in an interview setting the question also requires you to report back the start and end points of the sum. Keep this in mind and see if you can solve that problem, we'll see it in the mock interview section of the course!

# # Test Your Solution

# In[41]:

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)


# ## Good Job!
