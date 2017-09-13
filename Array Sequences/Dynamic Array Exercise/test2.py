class Foo(object):
    def __init__(self):
        self.__baz = 42
    def foo(self):
        print self.__baz
    
class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        self.__baz = 21
    def bar(self):
        print self.__baz

x = Bar()
x.foo()
x.bar()
print x.__dict__


"""

網路上有人用, 這段來解說
The name scrambling is used to ensure that subclasses don't accidentally override the private methods and attributes of their superclasses. It's not designed to prevent deliberate access from outside.


我把這行給mark掉, 會出現錯誤:
super(Bar, self).__init__()

Traceback (most recent call last):
  File "test2.py", line 15, in <module>
    x.foo()
  File "test2.py", line 5, in foo
    print self.__baz

喔, __init__ 是內建的class 初始化function, 

它不能被overwrite , 難怪都要再多執行一次 , 讓它去初始化父類別的__init__


這段英文講, __雙底線不是防別人呼叫它, 是防被overwrite.

要保護 module 變數或函式，可在變數名稱前加上單一底線，若用 from foo import * 時，這些變數不會被 import。
(編案：若用 from foo import _var 則還是能使用 _var 變數)。
若要在 class 內宣告 private 變數或方法，則在變數名或 方法名之前加上兩個底線 (__)，private 的效果是透過 name mangling 達成。(編案： name mangling 本質上只是把變數重新命名，因此使用者若執意要呼叫 private 變數還 是能夠達成。)

"""
