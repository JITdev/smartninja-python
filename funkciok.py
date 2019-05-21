def say_hello(nev: str = 'World', irasjel: str = '!') -> str:
    """ Hello """
    return f"Hello {nev}{irasjel}"

def osszeadas(a: int, b: int) -> int:
    c = a + b
    return c

def muvelet(a: int, b: int, o: str):
    ret = None

    if o == '+':
        ret = a + b
    elif o == '-':
        ret = a - b
    elif o == '/':
        if b == 0:
            ret = 'n/a'
        else:
            ret = a / b
    elif o == '*':
        ret = a * b
    else:
        ret = 'n/a'

    return ret

print(muvelet(4, 5, '*'))

# x = say_hello()
# sum = 0
# for i in range(1, 11, 1):
#     sum = osszeadas(sum, i)

# print(sum)





