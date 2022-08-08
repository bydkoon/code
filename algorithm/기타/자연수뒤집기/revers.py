
from unicodedata import digit


def digit_reverse(a):
    b = [int(x) for x in str(a) ]
    b.reverse()
    return b

def digit_reverse2(a):
    return list(map(int, reversed(str(a))))

def digit_reverse3(a):
    return a[::-1]

a :int = 12345

print(digit_reverse(a))
print(digit_reverse2(a))

b : list = [1,2,3,4,5]
print(digit_reverse3(b))