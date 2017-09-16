# 雖然我用幾行 寫出來了，但這個很明顥，就是要你讀 一次
# 就把問題 給 解了，而我用到 set  count ，每call 一次，
# 其它就 等於把input 給掃過一次
def compress(s):
    if s == "": return ""
    print(sorted( set(s) ) )
    str1 = ""
    for i in sorted( set(s) ):
        str1 = str1 + i + str(s.count(i))
        #dict1 = {i:s.count(i)}
    print(str1)
    return str1

"""
掃二次, 一次要初始化 dict ,

第二次給 把對應的values 給填上。

我把字典的key跟值，給 合起來，超 酷 的。

把for loop 寫在 list or dict 中，去建資料，好秋。
"""
def compress2(s):
    if s == "": return ""
    dict1 = {i:0 for i in sorted( set(s) )}
    for i in s:
        dict1[i] += 1
    print( "".join( [ i+str( dict1[i] ) for i in dict1.keys() ] ) )
    return "".join( [ i+str( dict1[i] ) for i in dict1.keys() ] )

def compress_author(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.

    力害，真的只掃了一次。

    這題 ，在主軸的演算法中，用到了[i - 1] , 這種 index，

    這要很注意，邊界， 因為會用到 i - 1 ，所 以作者，

    index 從 1 開始， 初值的設 定也是設到了2個元素 的情況。
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)
t.test(compress2)
