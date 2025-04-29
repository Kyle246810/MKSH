score=list()
score=int(input("score="))
while score>=0:
    scores.append(score)
    score = int(input('score='))
print('數列是:',score)
print('總分是:',sum(scores))