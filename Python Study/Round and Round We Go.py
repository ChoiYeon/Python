#https://www.acmicpc.net/problem/6373

# 2023.11.20 코멘트
# 아마 기존 리스트에 첫 숫자를 곱한 값이 담기는 리스트에서 검색하는 과정이 문제인 것으로 보임.
# 리스트에 첫 숫자가 중복될 경우 판단에 오류가 생길 수 있음.
# 이에 따른 새로운 과정이 필요할 것 같음.
# 예를 들어 기존 숫자의 배열을 바꿔 곱한 리스트에서 시작점을 찾고 여러개일 경우 두번째 숫자를 찾은뒤 한칸 앞을 시작점으로 체크한다거나..
# 고민좀 해보자

# 2023.12.01 코멘트
# 아무리봐도 비효율적인 방식이라  문제 해결 방식을 바꿔보기로 함.
# 기존과 같이 시작점을 찾아 일일이 돌리는건 비효율적이라고 판단
# 순환수의 특성상 자릿수가 달라지면 순환수가 아닐거라고 판단하기 때문에
# 시작시 입력한 숫자의 배열을 지속적으로 바꾸며 곱한값이 순환수인지 체크해주는 함수 추가
# 그외에도 일부 코드 가독성 개선
# 참고 : https://blog.naver.com/jinhan814/222530418259
# 좋은 코드 감사합니다.

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
    return False



#키입력
while True :
    try:
        #초기 변수 설정
        #flag : 순환수인지 체크용 flag 변수 / True = 순환소수 False = 순환 소수아님.
        p = input().rstrip()
        nump, flag = int(p) , True

        #순환 체크
        for i in range(1, len(p)+1):
            #입력값의 첫 숫자가 0 일경우 곱한 값에도 0 추가  [int로 변형할 경우 앞에 0이 날아가기 때문에 추가]
            t = str(nump * i).zfill(len(p))
            # 만약 t의 길이가 p보다 크거나 Check 함수에서 False가 떨어진 경우 flag를 false으로 초기화
            if len(t) > len(p) or Check(p, t) == False : flag = False
        # flag가 false인 경우 뒤에 not 을 추가하여 문장 완성
        print(f'{p} is {"" if flag else"not "}cyclic')
    except:
        #무한루프 방지용
        break

# 기존 순환수 찾는 코드 시작 *************************************************************************************************
#     # 시작점 찾는 법 : 처음 상태의 리스트의 첫번째 숫자를 숫자를 곱한 뒤 리스트에서 찾으면 해당 부분을 시작 지점으로 판단
#     # start : 비교하는 리스트에서 동일한 숫자 체크용   
#      start = 0 
#      for j in range(len(tlist)):
#         if flist[0] == tlist[j] : 
#             start = j
#             break
#     # 시작점부터 순환 여부 체크하는 루프 -1이 아닌 경우 동일한 값이 없으므로 순환수가 아니라고 판단하여 falg true 변경 후 탈출
#     if start!=-1:
#         for k in range(len(flist)) :
#             #시작점 index 변수가 list의 크기를 넘어갔을 경우 0으로 초기화해주는 if문
#             if start >= len(tlist) :
#                 start = 0
#             #순환수 체크 if문 flist의 처음부터 끝까지 tlist의 시작점부터 반복하여 비교함.
#             if flist[k] == tlist[start]:
#                 start = start+1
#             else :
#                 flag = True
#                 break
#     else :
#         flag = True
# # 출력문 flag가 true일 경우 "not "을 추기하여 문장 완성
# print(f'{p} is {"" if flag==False else"not "}cyclic')
# 기존 순환수 찾는 코드 종료 ***************************************************************************************************

