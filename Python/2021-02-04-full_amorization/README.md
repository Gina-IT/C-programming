## 원리금균등상환 계산하기

핸드폰을 할부로 구매할 경우 할부 이자가 붙어 월 요금을 납입하게 되는데  
이때 원리금균등상환방식으로 납입하게 된다.  
  
원리금균등상환방식은 매달 납입하는 총 금액은 같지만,  
단말기의 월별 할부 원금이나 이자가 다르다.  
초기에 가장 많은 이자를 납입하며 점차 이자를 적게 납입한다.  
  
따라서 특정 시기까지 얼만큼의 이자를 내는지,   
잔여 할부금이 얼마인지 알기 어렵기 때문에 원리금균등상환 계산기를 이용한다.  
  
------
  
### 변수들
1. 입력 받을 값
    - fee: 단말기 원금
    - interest_percentage: 연 이자율(%)
    - months: 할부개월수
    - date: 요금정보를 알고 싶은 기간
    (ex. 24개월 할부 중 12개월까지의 이자 및 잔여금 알고 싶을 때 date=12)

2. 월불입금 계산
    - interest_y: 연 이자율(소수)
    - interest_m: 월 이자율(소수)
    - bill_month: 월 납부금(월 할부원금 + 월 이자)
    - bill_total: 총 납부금(할부원금 + 총이자)

3. 월 이자 및 할부원금 계산
    - interest: 월 이자 금액
    - sum_interest: 현재까지 납부한 총 이자
    - fee_month: 월 할부원금
    - fee_left: 단말기 잔여 할부금
    - month: 납입 회차(개월 수)
  
------
  
### 값 입력받기

**참고**  
▶ input으로 값을 입력받으면 문자형으로 자료형이 저장되기 때문에,  
나중에 값을 계산하기 위해서는 int()나 float()을 이용하여 정수형이나 실수형으로 변환해주어야 함  
▶ 변환된 자료형으로 변수를 저장하기 위해, 변환한 자료형을 해당 변수에 다시 저장해야함 (ex. a= int(a))  
▶ 값이 잘못 입력되면 제대로 입력될 때 까지 다시 입력받아야 하므로 while문을 이용하여 핸들링  
<br/>
1. 단말기 할부 원금 
```python
fee = input('단말기 원금: ')   

while not fee.isdecimal():     # 단말기 원금이 숫자가 아니면 다시 입력받음
    print('금액이 정확하지 않습니다.')      
    fee= input('단말기 원금: ')
print(fee)

fee= int(fee)        
```
<br/>
2. 할부 이자율(%)
```python
interest_percentage = input('연이율(%): ')
a,_,b= interest_percentage.partition('.')		# '.'을 기준으로 문자열을 분리해 자연수는 a변수에 소수점 아래는 b 변수에 저장

if not interest_percentage.isdecimal():     # 할부 이자율이 숫자가 아니면 다시 입력받음
    while not (a== '' or a.isdecimal()) and (b== '' or b.isdecimal()):  	# 자연수나 소수점 아래 부분이 숫자가 아니거나 공백이면 다시 입력받음
        print('이율이 정확하지 않습니다.')
        interest_percentage = input('연이율(%): ')
        a,_,b= interest_percentage.partition('.')
print(interest_percentage)

interest_percentage= float(interest_percentage)
interest_y= interest_percentage/100		# %로 입력받은 값을 계산에 이용하기 위해 100으로 나누어 줌
```
<br/>
3. 할부 개월 수
```python
months = input('할부 개월: ')

while not months.isdecimal():      # 할부 개월이 숫자가 아니면 다시 입력받음
    print('할부개월이 정확하지 않습니다.')
    months = input('할부 개월: ')
print(months)

months= int(months)     # 계산을 위해 int형으로 바꿔줌
```
<br/>
4. 요금 정보를 알고싶은 기간 
```python
date =  input('알고 싶은 기간(없을 경우 0 입력): ')
while (not date.isdecimal()):      # 알고 싶은 기간이 숫자가 아니면 다시 입력받음
    print('기간이 정확하지 않습니다.')
    date = input('알고 싶은 기간: ')

date= int(date)
if date > months:        # 입력기간이 할부 개월보다 길면 다시 입력받음
    print('입력기간이 할부 개월보다 깁니다.')
    date = input('알고 싶은 기간: ')
print(date)
```
  
------
  
### 월불입금 공식을 이용하여 월 납입금 및 총 납입금 계산

월불입금(월 납부금) = 대출원금 * 연이자율 / 12 * (1 + 연이자율/12)^기간 / ((1 + 연이자율/12)^기간 -1)  

**참고**
▶ 파이썬 계산에서 거듭제곱은 `**`로 계산함  

```python
interest_m = interest_y/12

bill_month =int(fee * interest_m * ( 1 + interest_m)**months / ((1 + interest_m)**months -1))   
bill_total = bill_month * months        
```
  
------
  
### while문을 사용하여 월별 요금 계산

```python
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
```
  
------
  
### Result

<img src="/Python/2021-02-04-full_amorization/_img/result.png">  