import random
from datetime import datetime
    
def baseball_game(n):

    numbers = set()
    cnt = 0

    while len(numbers) < n:
        numbers.add(random.randint(0,9))
    random_numbers = list(numbers)
    random.shuffle(random_numbers)
    #print(random_numbers)
                    
    while 1:
        while 1:
            my = input('숫자 입력 (exit = 종료 ) : ')
            if len(my) > n:
                print(f'{n}자리 수를 입력해주세요')
            
            else:
                count = 0
                for i in range(len(my)-1):
                    if my[i] in my[i+1:]:
                        count += 1
                if count > 0:
                    print('중복된 숫자 입력 금지')
                else:
                    break
        
        if my == 'exit':
            break
    
        strike = 0
        ball = 0
        out = 0
        cnt += 1

        for i in range(n):
        
            if int(my[i])==random_numbers[i]:
                strike += 1

            elif int(my[i]) in random_numbers:
                ball += 1
            
            else:
                out += 1
    
        if strike == n:
            print(datetime.now())
            print(f'{cnt}번 도전')
            break
        
        print(f'{strike}S {ball}B {out}O')
        print()

