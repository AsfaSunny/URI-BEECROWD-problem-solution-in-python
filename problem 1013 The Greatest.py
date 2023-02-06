# 1st way:

import math

a, b, c = list(map(int,input().split()))

maior = (a + b + abs(a - b))  / 2
result = (maior + c + abs(maior - c))/2

print("%d eh o maior" %result)




# Alternative and easy way:

A, B, C = list(map(int,input().split()))

print("{} eh o maior".format(max(A, B, C)))
