# ques 11 assignment
N = int(input())
for i in range(N):
    SH, SM, EH, EM = map(int, input().split())
    if EM < SM:
        EM += 60
        EH -= 1
    duration_h = EH - SH
    duration_m = EM - SM
    print(duration_h, duration_m)
