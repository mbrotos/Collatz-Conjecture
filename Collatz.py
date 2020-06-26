
def CollatzRecursive(n):
    if (n==1):
        return n
    elif (n % 2 == 0):
        n = n/2
        return CollatzRecursive(n)
    else:
        n = (3*n)+1
        return CollatzRecursive(n)

n = int(input("Input a positive integer: "))
print(CollatzRecursive(n))