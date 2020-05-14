## 가위!바위!보! 게임 

*"랜덤 함수를 이용하여 가위바위보 게임하기"*   

-----------

**참고**  
1. 가위= 0, 바위= 1, 보= 2  
2. while 무한 루프를 이용하여 사용자가 종료하고 싶을 때 종료할 수 있도록 구현  

### Code   

```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define WIN 1
#define LOSS 0

int main()
{
	int i, num, in, Win_Loss;
	srand(time(NULL));     // 난수 초기화 
	char answer;
 	
	while(1)     // 반복문 무한 루프 
	{
		num= rand() % 3;     // 3개의 난수, 0에서 시작 
		printf("!!! 자 시작 합니다 !!!\n\n");
		printf("가위!바위!보! (가위=0, 바위=1, 보=2): ");
		scanf("%d", &in);
		
		if(in<0 || in >2)     //입력값이 0보다 작거나 2보다 크면 
		{
			printf("잘못입력하였습니다.\n\n");
			continue;      // 아래 코드 무시하고 다시 실행 
		} 
		
		if (num == 2){     // 컴퓨터 랜덤 숫자가 2(보)이면 
			if ( in == 0)       // 사용자의 입력 값이 0(가위)일 때 
				Win_Loss= WIN;     // 이김 
			else   
				Win_Loss= LOSS;
		}
		else {
			if (num == in-1)     // 랜덤 수가 입력값 -1이면 
				Win_Loss= WIN;     // 이김  ( 랜덤 수=0 =가위, 입력 값=1 =바위/ 랜덤 수 =1 = 바위, 입력 값= 2= 보) 
			else
				Win_Loss= LOSS;
		}
		printf ("컴퓨터: %d, YOU: %d\n\n", num, in);      
		
		if (num == in)
			printf("비겼습니다.\n------------------------------\n\n");
		else if(Win_Loss == WIN)
			printf("당신이 이겼습니다.\n------------------------------\n\n");
		else
			printf("컴퓨터가 이겼습니다.\n------------------------------\n\n");
			
		printf("게임을 계속 하시겠습니까? (Yes= y, No= n)\n");    //게임을 계속할 지 물어봄 
		scanf("%s", &answer);
		printf("------------------------------\n\n");
		
		if(answer == 'y')     // 대답이 y(Yes)이면 
			continue;     // 아래 코드 무시하고 다시 while문 실행 
		else if(answer == 'n')     // 대답이 n(No) 이면 
			break;      // while문 벗어남 
	}
}
```  

-----------

### Result  

<img src= "/2020-05-15-RockScissorPaper/_img/result.JPG" alt="Rock Sicssor Paper game play">
