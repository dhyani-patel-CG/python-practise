add = 0
def addition(n):
    global add
    add+=n
    if (n==10):
        return add
    return addition(n+1)
print(addition(1))