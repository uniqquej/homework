import baseball
import time


def main():
    while 1:
        n = int(input('자릿수 입력 :' ))
        if n>10:
            print('1~10 까지의 숫자를 넣어주세요')
        else:
            break
        
    start_time = time.time()
    baseball.baseball_game(n)
    end_time = time.time()
    print(f"코드 실행 시간 : {end_time-start_time:.5f}초")

main()