import sys

def tm(A, C, G, T):
    total = A + C + G + T 
    if  total <= 13: 
        return ((A+T)*2 + (G+C)*4)
    elif total > 13: 
        return (64.9 + 41*(G+C - 16.4)/(A+T+G+C))
    else:
        return 'ERROR'
print(tm(13, 12, 11, 10))