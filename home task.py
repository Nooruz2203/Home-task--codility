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

#     def solution(A, B):
    
#     downStack = [0] * len(A)
#     downSize = 0
    
#     upAlive = 0
    
#     for i in range(-1, -1*(len(A)+1), -1):
        
#         if B[i] is 0: 
#             downStack[downSize] = A[i]
#             downSize += 1
#         else: 
            
#             if downSize is 0: 
#                 upAlive += 1
#             else: 
                
#                 while A[i] > downStack[downSize-1]:
#                     downSize -= 1
#                     if downSize is 0:
#                         break
#                 if downSize is 0:
#                     upAlive += 1
    
#     return downSize+upAlive
