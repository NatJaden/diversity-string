def solution(N):
    result = []
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for k in range(26, 0, -1):
        if N % k == 0:
            repetitions = N // k
            result = letters[:k] * repetitions
            break
    
    return result