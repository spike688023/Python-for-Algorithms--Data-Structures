"""
我的話, 會把make_array() 拿掉, 併入 _resize() , 

會看起來簡潔一點, 但可讀性就不好了.
"""
import ctypes

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
    
    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n
    
    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!') # Check it k index is in bounds of array
        
        return self.A[k] #Retrieve from array at index k
        
    def append(self, ele):
        """
        Add element to end of the array
        """
        # 難怪要二個變數, 一個n 一個capacity, 
        # n 是實際用的, capacity則是真正配給的空間 , 所以這個判斷是看size 有沒有爆了
        if self.n == self.capacity:
            self._resize(2*self.capacity) #Double capacity if not enough room
        
        self.A[self.n] = ele #Set self.n index to element
        self.n += 1
        
    def _resize(self,new_cap):
        """
        Resize internal array to capacity new_cap
        """
        
        B = self.make_array(new_cap) # New bigger array
        
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
            
        # 這行算是 list的複製, list A copy 成 list B , 所以前面才要先把值給過去.
        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity
        
    def make_array(self,new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

# Instantiate
arr = DynamicArray()

# Append new element
arr.append(1)

# Check length
len(arr)

# Append new element
arr.append(2)

# Check length
len(arr)

# Index
arr[0]

arr[1]

"""

我拿掉這行最後的func , 會發生錯誤如下, 為什麼?
        return (new_cap * ctypes.py_object)()


Traceback (most recent call last):
  File "test3.py", line 61, in <module>
    arr.append(1)
  File "test3.py", line 35, in append
    self.A[self.n] = ele #Set self.n index to element
TypeError: '_ctypes.PyCArrayType' object does not support item assignment


又觀察到一個東西, dir出來的東西, 都是__開頭, 

代表,它是個 abstract class
>>> ctypes.Array()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abstract class
>>> dir(ctypes.Array)
['__class__', '__ctypes_from_outparam__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '_b_base_', '_b_needsfree_', '_objects']



Arrays are sequences, containing a fixed number of instances of the same type.

The recommended way to create array types is by multiplying a data type with a positive integer:

拿這個例子來看, IntArray5 只是一個未初始化的class, 裡面都沒有值, 

而IntArray5(5, 1, 7, 33, 99) 就是做初始化的動作.
>>> IntArray5 = c_int * 5
>>> ia = IntArray5(5, 1, 7, 33, 99)
>>> ia[0]
5
>>> len(ia)
5
>>> ib = IntArray5(5, 1, 7, 33)
>>> len(ib)
5

這麼一來, 這行就可以理解了, 
(new_cap * ctypes.py_object)() , 因為不知道要裝什麼,

所以型態給 py_object 讓使用者之後自己去處理.

>>> NoneArray5 = ctypes.py_object * 5
>>> a5 = NoneArray5("a","b","c","d","e")
>>> a5[0]
'a'
>>> type(a5[0])
<class 'str'>
>>> b5 = NoneArray5(1.0,2.0,3.0,4.0,5.0)
>>> type(b5[0])
<class 'float'>


Reference:
https://docs.python.org/2/library/ctypes.html

"""
