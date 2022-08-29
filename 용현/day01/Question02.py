#괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')'
# 문자로 닫혀야 한다는 뜻 입니다.

def solution(s):
    answer = True
    bracket = [] # 괄호를 담을 배열
    for i in s:
        if i == '(':
            bracket.append(i) # 열리는 괄호면 담는다.
        elif bracket != [] and i == ')': # 괄호를 담는 배열이 비어 있지 않고, 닫히는 괄호면 배열에서 열리는 괄호를 빼준다.
            bracket.pop()
        elif bracket == [] and i == ')': # 비어 있는 상태 에서 닫히는 괄호가 들어 오면 틀린 것 이므로 answer를 False로 바꾸고 반환
            answer = False
            return answer

    if bracket: # 최종적으로 배열안에 괄호가 남아 있으면 짝이 맞지 않으것이므로 False 반환
        answer = False
        return answer

    return answer