def solution(m, musicinfos):
    
    answer = []
    
    for temp in musicinfos:
        info = temp.split(',')
        start = info[0].split(':')
        end = info[1].split(':')
        
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        
        code = change(info[3])
        code = code * (time // len(code)) + code[:time % len(code)]
        
        if change(m) in code:
            answer.append((info[2], time))

    if len(answer) == 0:
        return "(None)"
    
    else:
        answer.sort(key = lambda x: -x[1])
        return answer[0][0]
    
# #이 들어간 문자 바꾸기 
def change(code):
    code = code.replace('C#', 'c')
    code = code.replace('D#', 'd')
    code = code.replace('F#', 'f')
    code = code.replace('G#', 'g')
    code = code.replace('A#', 'a')
    return code
