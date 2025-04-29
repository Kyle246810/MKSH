total=0
score=int(input("score="))
print('如輸入完畢，請輸入負一')
while score>=0:
    total = total + score
    score = int(input("score="))
print('總分是:',total)

