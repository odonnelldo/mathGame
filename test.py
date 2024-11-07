import random

a1 = ""
a2 = ""
a3 = ""
a4 = ""
x = 7
y = 9

options = range(1,11)

def assignAnswer(answer1, answer2, answer3, answer4, x,y):
    listAns = [answer1, answer2, answer3, answer4]
    a_answer = str(x * y)
    possible_answer = []
    p = 1 
    while p < len(listAns): 
        possible_answer.append(str(random.choice(options)*random.choice(options)))
        p += 1
    possible_answer.append(a_answer)
    print(possible_answer)
    for item, indy in enumerate(listAns):
        tempans = random.choice(possible_answer)
        listAns[item] = tempans
        possible_answer.remove(tempans)
    
    answer1 = listAns[0]
    answer2 = listAns[1]
    answer3 = listAns[2]
    answer4 = listAns[3]
    print(listAns)
    print(possible_answer)
    return answer1, answer2, answer3, answer4

print(assignAnswer(a1,a2,a3,a4,x,y))
