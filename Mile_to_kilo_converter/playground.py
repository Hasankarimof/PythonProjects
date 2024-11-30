

def add(*args):
    total = 0
    for num in args:
        total += num
    return total




print(add(2,3,4,5,6,7,8,9,10))
print(add(1, 2, 3))        # Output: 6
print(add(10, 20, 30, 40)) # Output: 100
print(add())