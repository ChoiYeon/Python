import sys
input = sys.stdin.readline

def Check(a, b):
    # a는 입력받은 수 , b는 i만큼 곱한 뒤의 수
    # t는 입력받은 수로 초기화
    t = a
    for i in range(len(a)):
        #a만큼 루프 반복
        if t == b: return True
        #만약 t가 b와 같다면 true 반환
        #아니라면 t
        t = t[1:] + t[0]
    return 0

while True:
    try:
        #입력받은 수의 우측 공백 제거
        s = input().rstrip()
        # n에는 입력받은 수리를 형변화 하여 저장
        # flag에는 1저장
        n, flag = int(s), True
        # 반복문 (1부터 입력받은 수의 길이 +1만큼)
        for i in range(1, len(s) + 1):
            # t는 n*i지만 t가 n의 길이와 다를경우 (맨앞0이 자동으로 지워졌을 경우)를 대비하여 zfill 함수를 사용해 0추가
            t = str(n * i).zfill(len(s))
            # 만약 t의 길이가 s보다 크거나 Check 함수에서 False가 떨어진 경우 flag를 false으로 초기화
            if len(t) > len(s) or not Check(s, t): flag = False
        # flag가 false인 경우 뒤에 not 을 추가하여 문장 완성
        print(f'{s} is {"" if flag else "not "}cyclic')
    except:
        break