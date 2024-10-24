def is_perfect_square(n):
    i=1
    while i*i<=n:
        if i**2== n:
            return True
        i+= 1
    return False
n=int(input())
print(is_perfect_square(n))