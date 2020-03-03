# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b