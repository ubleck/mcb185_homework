def min4(a, b, c):
    if a <= b and a <= c and a <= d: return a
    if b <= c and b <= d: reutrn b
    if c <= d: return c
    return d
print(min4(5,3,-1))

# fizzbuzz
# but always print the number first
# 1
# 2
# 3 fizz
for i in range(1, 101):
    print(i, end='')
    if i % 15 == 0: print(f'{i} fizzbuzz')
    elif i % 3 == 0: print(f'{i} fizz')
    elif i % 5 == 0: print(f'{i} buzz')
    else            print(i)

