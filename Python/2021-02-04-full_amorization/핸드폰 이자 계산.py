print('핸드폰 할부 이자 계산 프로그램입니다.\n프로그램 이용을 위해 다음 수치들을 정확히 입력해주세요.')


# 단말기 할부 원금 입력받기
fee = input('단말기 원금: ')        # input으로 입력받으면 자료형이 문자형임
while not fee.isdecimal():     # 단말기 원금이 숫자가 아니면 다시 입력 받음
    print('금액이 정확하지 않습니다.')      
    fee= input('단말기 원금: ')
print(fee)
fee= int(fee)        # 계산을 위해 int형으로 바꿔줌


# 할부이자율 입력받기
interest_percentage = input('연이율(%): ')
a,_,b= interest_percentage.partition('.')
if not interest_percentage.isdecimal():     # 할부 이자율이 숫자가 아니면
    while not (a== '' or a.isdecimal()) and (b== '' or b.isdecimal()):  
        print('이율이 정확하지 않습니다.')
        interest_percentage = input('연이율(%): ')
        a,_,b= interest_percentage.partition('.')
print(interest_percentage)
interest_percentage= float(interest_percentage)
interest_y= interest_percentage/100


# 할부 개월 수 입력받기
months = input('할부 개월: ')
while not months.isdecimal():      # 할부 개월이 숫자가 아니면 다시 입력받음
    print('할부개월이 정확하지 않습니다.')
    months = input('할부 개월: ')
print(months)
months= int(months)     # 계산을 위해 int형으로 바꿔줌


# 요금 정보를 몇 개월차까지 알고싶은지, 알고싶은 기간 입력받기
date =  input('알고 싶은 기간(없을 경우 0 입력): ')
while (not date.isdecimal()):      # 알고 싶은 기간이 숫자가 아니면 다시 입력받음
    print('기간이 정확하지 않습니다.')
    date = input('알고 싶은 기간: ')

date= int(date)
if date > months:        # 입력기간이 할부 개월보다 길면 다시 입력받음
    print('입력기간이 할부 개월보다 깁니다.')
    date = input('알고 싶은 기간: ')
print(date)



# 월불입금
# 대출원금 * 이자율 / 12 * (1 + 이자율/12)**기간 / ((1 + 이자율/12)**기간 -1)
interest_m = interest_y/12

bill_month =int(fee * interest_m * ( 1 + interest_m)**months / ((1 + interest_m)**months -1))    # 월불입금
bill_total = bill_month * months        # 총 납부금 (원금 + 이자)


# 알고 싶은 기간이 입력되었으면 그 기간까지, 입력되지 않았으면 할부개월 까지 
if date:
    until = date
else:
    until = months 

sum_interest=0      # 총 할부이자
month = 1           # 납입 회차
fee_left= fee       # 단말기 할부 잔액
while month <= until :
    interest = int(fee_left * interest_m)
    sum_interest += interest

    if month == months:     # 납부 마지막 회차때 잔여 할부금이 할부 원금과 다르면
        fee_month = fee_left        # 마지막 달 할부원금을 잔여 할부금 전체로 함
        bill_month = fee_month + interest       # 월 할부 원금이 달라짐에 따라 월 청구금도 달라짐
    else:  
        fee_month = bill_month - interest     # 월 할부 원금 = 월 청구액 - 이자

    fee_left -= fee_month       # 다음달 할부 잔액 = 할부 잔액 - 월 할부 원금

    print('납입', month, '회차- ', '월 청구액: ', bill_month, '할부원금: ', fee_month, '할부이자: ', interest, '잔여할부금: ', fee_left)

    month += 1

print('총 할부이자: ', sum_interest, '총 납입금액: ', bill_total)