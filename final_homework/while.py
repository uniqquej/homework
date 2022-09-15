i = 0
while i < 5:
    txt = input()
    i += 1

    if txt == 'exit':
        break

    try:
        a = int(txt)
        print(a * 2)

    except ValueError:
        print(f'입력한 문자는 "{txt}" 입니다.')

    