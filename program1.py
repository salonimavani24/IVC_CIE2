n = int(input())
temp = n
digits = len(str(n))
sum_val = 0

while temp > 0:
    sum_val += (temp % 10) ** digits
    temp //= 10

if sum_val == n:
    print("Armstrong")
else:
    print("Not Armstrong") 
