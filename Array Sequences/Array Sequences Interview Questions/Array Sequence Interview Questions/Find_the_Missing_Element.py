from nose.tools import assert_equal

class TestFinder(object):

    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# 用集合的方式寫，很常 會忘了思考重複的元素
"""
def finder(arr1,arr2):
    set1 = set( iter(arr1) )
    set2 = set( iter(arr2) )
    diff = set1.difference(set2)
    return diff.pop()
"""
def finder(arr1,arr2):
    dict1 = {i:arr1.count(i) for i in arr1}
    dict2 = {i:arr2.count(i) for i in arr2}
    for i in arr1:
        # 一直中KeyError ，原來是沒那個key值。
        try:
            if dict1[i] != dict2[i]: return i
        except KeyError:
            return i

def finder3(arr1, arr2):
    result=0
    # 這裡的arr1 + arr2 只是把二個list給串起來而已
    print(arr1+arr2)
    # Perform an XOR between the numbers in the arrays
    # 這個解  的概念是，相同的值之間做XOR , 出來是0
    # 所 以0跟每個值做xor 會迫出，少了的那個值。
    for num in arr1+arr2:
        result^=num
        #print(result)

    return result

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print( finder3(arr1,arr2) )

# Run test
t = TestFinder()
t.test(finder)

"""
判斷 key 有沒有在一個字典內。
d = {'a': 1, 'b': 2}
'a' in d
True
"""
