from func import calc 

def main():
    prob = list(input('계산식을 입력해주세요(ex)1 + 2 + 3 : ').split())
    print('답 : ',calc(prob))
    
main()


