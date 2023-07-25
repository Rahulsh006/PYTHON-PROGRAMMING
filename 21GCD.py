def gcd(a, b):
    r = min(a, b)
    while r:
        if a % r == 0 and b % r == 0:
            break
        r -= 1
    return r

a = int(input (" enter the no 1 "))

b = int(input (" enter the no 2 "))

if(gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
	print('not found')


