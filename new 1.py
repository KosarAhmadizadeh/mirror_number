Number = int(input())
if (Number < 0):
    print("invalid input")
else:
    for i in range(1,Number+1):
        if (Number%i == 0):
            if (i%2!= 0):
                print(i)
p = str(Number)
q = p[ : :-1]
if p == q:
    print("Yes")
else:
    print("No")
    