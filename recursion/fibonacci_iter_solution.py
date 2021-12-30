def iterative_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        prev1 = result[i - 1]
        prev2 = result[i - 2]
        result.append(prev1 + prev2)
    
    return result[n]


res = iterative_fib(7)


# iterative w/o an array
def fib_without_array(n):
    a = 0
    b = 1
    c = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

test = fib_without_array(7)


# fib colt variant
def fib_list(max_num):
    nums = []
    a, b = 0, 1
    while len(nums) < max_num:
        nums.append(b)
        a, b = b, a + b
    return nums

# with generator
def fib_gen(max_num):
    x = 0
    y = 1
    count = 0
    while count < max_num:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_gen(10):
    print(n)



