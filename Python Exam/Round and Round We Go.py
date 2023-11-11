#https://www.acmicpc.net/problem/6373

#아마 기존 리스트에 첫 숫자를 곱한 값이 담기는 리스트에서 검색하는 과정이 문제인 것으로 보임.
#리스트에 첫 숫자가 중복될 경우 판단에 오류가 생길 수 있음.
#이에 따른 새로운 과정이 필요할 것 같음.
#예를 들어 기존 숫자의 배열을 바꿔 곱한 리스트에서 f

#키입력
p = input()
nump = int(p)
flist = list(p)
#print(len(flist))
#초기 변수 설정
#flag : 순환수인지 체크용 flag 변수 / True = 순환소수 아님 False = 순환 소수임.
#start : 비교하는 리스트에서 동일한 숫자 체크용 
flag = False

start = 0 

#순환 체크
for i in range(1, len(flist)+1):
    
    #입력받은 값에 곱해주는 부분
    res = nump*i
    #곱한 값의 List에 저장
    tlist = list(map(str, str(res)))
    #입력값의 첫 숫자가 0 일경우 곱한 값에도 0 추가  [int로 변형할 경우 앞에 0이 날아가기 때문에 추가]
    if flist[0] == "0" and start==0 : 
        tlist.insert(0,"0")
    start = -1
    # 시작점 찾는 루프 
    # 시작점 찾는 법 : 처음 상태의 리스트의 첫번째 숫자를 숫자를 곱한 뒤 리스트에서 찾으면 해당 부분을 시작 지점으로 판단
    for j in range(len(tlist)):
        if flist[0] == tlist[j] : 
            start = j
            break
    # 시작점부터 순환 여부 체크하는 루프 -1이 아닌 경우 동일한 값이 없으므로 순환수가 아니라고 판단하여 falg true 변경 후 탈출
    if start!=-1:
        for k in range(len(flist)) :
            #시작점 index 변수가 list의 크기를 넘어갔을 경우 0으로 초기화해주는 if문
            if start >= len(tlist) :
                start = 0
            #순환수 체크 if문 flist의 처음부터 끝까지 tlist의 시작점부터 반복하여 비교함.
            if flist[k] == tlist[start]:
                start = start+1
            else :
                flag = True
                break
    else :
        flag = True
# 출력문 flag가 true일 경우 "not "을 추기하여 문장 완성
print(f'{p} is {"" if flag==False else"not "}cyclic')