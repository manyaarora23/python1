# ques 13 assignment
N = int(input())
i = 1
while N > 0:
    N -= i
    if N <= 0:
        print("Ramesh")
        break
    N -= 2 * i
    if N <= 0:
        print("Suresh")
        break
    
    i += 1
