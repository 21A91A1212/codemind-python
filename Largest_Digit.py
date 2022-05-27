n=int(input())
Max=0
while n:
    rem=n%10
    if Max<rem:
        Max=rem
    n=n//10
print(Max)