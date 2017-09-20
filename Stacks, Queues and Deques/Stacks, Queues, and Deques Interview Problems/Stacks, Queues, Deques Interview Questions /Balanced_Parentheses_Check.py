"""
目前的想法, 用字典, 把對應的配對, 先寫死起來, 

遇到opening parenthesis, 就先放到stack中, 

所以要有個list,是存 opening parenthesis.
"""
from stack import Stack
def balance_check(s):
    opening = [ '(', '[', '{']
    close = { ')':'(', ']':'[', '}':'{'}
    s1 = Stack()

    if len(s) == 0 or len(s)%2 == 1: return False

    for i in s:
        if i in opening: s1.push(i)
        else:
            if close[i] != s1.pop(): return False
        
    return True
    

print( balance_check('[]') )
print( balance_check('[](){([[[]]])}')  )
print( balance_check('()(){]}')  )

print( balance_check('[](){([[[]]])}(')  )
print( balance_check('[{{{(())}}}]((()))')  )
print( balance_check('[[[]])]')  )
