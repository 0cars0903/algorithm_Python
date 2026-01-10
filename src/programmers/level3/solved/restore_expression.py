# n진법을 10진법으로 변환 
def n_change(n, x): 
    answer = 0
    for i in range(len(x)):
        v = int(x[i])
        answer += (n**(len(x)-i-1)) * v
    return answer 

# 10진법을 n진법으로 변환 
def change_n(n, x): 
    answer = []
    
    while x >= n:
        v1 = x // n 
        v2 = x % n 
        x = v1
        answer.append(v2)
    answer.append(x)
    answer.reverse()

    ans = ''  
    for a in answer:
        ans += str(a)
    return ans
    
def solution(expressions):
    answer = []
    # Split 하여 리스트에 저장
    sen_X = [] # x가 포함된 식
    sen_V = [] # x가 포함되지 않은 식
    sen_n = [] # 최소 n진법을 구하기 위한 저장 리스트 

    for sen in expressions:
        sen_list = sen.split()
        if 'X' in sen_list:
            sen_X.append(sen_list)
            v0 = int(sen_list[0]) % 10 
            v2 = int(sen_list[2]) % 10 
            sen_n.append(max(v0,v2))
        else:
            sen_V.append(sen_list)
            v0 = int(sen_list[0]) % 10 
            v2 = int(sen_list[2]) % 10 
            v4 = int(sen_list[4]) % 10 
            sen_n.append(max(v0,v2,v4))
    
    pos_n = max(sen_n)+1 # 최소 n진법 

    n_list = {} # 각 진법마다 성립하는지 여부 저장 
    for i in range(pos_n,10):
        n_list[i] = 0

    for n in range(pos_n,10):
        sen_list = 0
        for sen in sen_V:
            if sen[1] == '+':
                left = n_change(n, sen[0]) + n_change(n, sen[2])
            elif sen[1] == '-':
                left = n_change(n, sen[0]) - n_change(n, sen[2])
            right = n_change(n, sen[4])
        
            if left == right: # 완전한 수식에서 좌변과 우변이 일치하면 성립함. 
                sen_list += 1 # 하나의 n진법에서 모든 수식이 성립하는지 검토 
                
        if sen_list == len(sen_V): # 모든 수식이 성립하면 
            n_list[n] = 1 # 성립 여부를 저장한다. 
            
    for sen in sen_X: # 구해야하는 수식에 대하여 
        pos_x = [] # 각 n 진법마다 계산 결과를 저장 
        for key in n_list.keys():
            if n_list[key] == 1:
                if sen[1] == '+':
                    left = n_change(key, sen[0]) + n_change(key, sen[2])
                elif sen[1] == '-':
                    left = n_change(key, sen[0]) - n_change(key, sen[2])
                right = change_n(key, left) # 10진법 기준의 수치를 n진법으로 변환 
                pos_x.append(right)
                
        if len(set(pos_x)) >= 2: # 여러 n진법 마다 값이 동일한지 검증 
            sen[-1] = '?' # 동일하지 않은 경우 
        else:
            sen[-1] = pos_x[0]

    answer_list = []
    for sen in sen_X:
        answer = ""
        for s in sen:
            answer += s + " "
        answer = answer[:-1]
        answer_list.append(answer)

    return answer_list