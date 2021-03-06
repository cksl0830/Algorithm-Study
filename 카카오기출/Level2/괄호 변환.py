def solution(p):
    answer=''
    # 1단계
    if not p:
        return ''
    
    # 2단계
    u,v = divide(p)
    
    # 3단계
    if check(u):
        # 3-1
        return u + solution(v) 
    # 4단계 
    else:
        # 4-1
        answer += '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

# 문자열을 u와 v로 분리
def divide(p):
    left = 0
    right = 0
    for idx, w in enumerate(p):
        if w == '(':
            left += 1
        elif w == ')':
            right += 1
        if left == right:
            return p[:idx + 1], p[idx + 1:]

# 올바른 괄호 문자열인지 
def check(u):
    stack = []
    for w in u:
        if w == '(':
            stack.append(w)
        else:
            if not stack:
                return False
            stack.pop()
    return True
