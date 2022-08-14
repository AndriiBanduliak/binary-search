
from random import randint as r

a = list(range(0,101))
s = r(0,100)
print("s = ", s)

s_t = 0
e_d = len(a)
mid = e_d // 2

if s > mid:
    counter = mid
    for i in range(mid, len(a)+1):
        if i != s:
            counter +=1
        else:
            print("index s = ", counter)

if s < mid:
        counter = 0
        for i in range(0, mid +1):
            if i != s:
                counter +=1
            else:
                print("index s = ", counter)

if s == mid:
    print("index s = ", mid)

print("real index: ", a.index(s))
