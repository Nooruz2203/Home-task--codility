def solution(A, B):
    go_up_count = 0
    s1 = []
    for i in range(0, len(A)):
        a = A[i]
        b = B[i]
        if b == 0:
            if not s1:
                go_up_count += 1
            else:
                while s1 and a > s1[-1]:
                    s1.pop()
                if not s1:
                    go_up_count += 1
        else:
            s1.append(a)

    return go_up_count + len(s1)

    