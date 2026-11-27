s='sita'
print(type(s))
s=34
print(type(s))
print('-'*40)
text: str ='good morning'
print(type(text))
text1: int =123
print(type(text1))
text3: int ='hello'
print(type(text3))
print('-'*40)
def fun(para:list[str])-> list[str]:
    para.reverse()
    return para
print(fun(['abc','xyz','pqr']))
print('-'*40)

def fullname(firstname:str,lastname:str)->str:
    return firstname.title()+' '+lastname.title()
print(fullname('shruti','shinde'))

def fullnamecap(fname:str,lname:str)->str:
    return fname.upper()+' '+lname.upper()
print(fullnamecap('shruti','shinde'))

print('-'*40)

def fun1(a:int,b:str,c:float,d:bool,e:byte):
    return a,b,c,d,e

print(fun1(1,'hello',3.5,True,b'byte'))

print('-'*40)

def fun2(info:Any)->Any:
    return info

print(fun2("good morning"))

def fun2(info:Any)->Any:
    return info

print(fun2([1,2,3,4,5]))

print('-'*40)

def fun3(info:dict[str,int])->dict[str,int]:
    return type(info.keys()),type(info.values()),info

print(fun3({'a':1,'b':2,'c':3}))

def fun4(marks:list[int])-> None:
    for score in marks:
        print(score)

print(fun4([85,90,78,92]))

print('-'*40)

def fun5(t:tuple[str,int,float],s:set[str,int,float])->Any:
    return t,s

print(fun5(('sita',26,5.5),{'gita',24,5.7}))

print('-'*40)

def fun6(t:tuple[str,int,float],s:set[str,int,float])->tuple|set:
    return t,s

print(fun6(('smita',36,6.5),{'gaurav',34,5.8}))

print('-'*40)

def fun7(data:str|int|float):
    return data,'is of type : ',type(data)
print(fun7('bhima'))
print(fun7(200))
print(fun7(3.14))

print('-'*40)

def fun8(data:str|None=None):
    return data,type(data)
print(fun8('b--hima'))
print(fun8())

print('-'*40)

from collections.abc import Iterable

def fun9(colours:iterable[str])->tuple[str]:
    return colours[::-1]

print(fun9(('red','green','blue')))

print('-'*40)

class student:
    def __init__(self,name,age)->str|int:
        self.name=name
        self.age=age

def getinfo(st:student)->str|int:
    return st.name,st.age

print(getinfo(student('shruti',29)))        
