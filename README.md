# eFriendPy
python을 이용하여 한국투자증권 Open API (eFriend expert)를 사용하는 예제 코드입니다.  
__사용전 반드시 아래 주의사항을 읽어주세요.__


# 주의사항  
- 이 코드는 아무런 제약없이 자유롭게 사용/수정 가능합니다.  
- 이 코드는 어디까지나 예제 코드입니다. 동작에 불완전한 부분이나 버그가 있을 수 있습니다. 
- __이 코드의 제작자(pjueon)는 이 코드에 대해서 어떤 것도 보장하지 않습니다. 코드 사용중 생긴(ex> 버그, 사용자의 실수, 투자로 인한 손실 등) 어떠한 종류의 피해에 대해서도 책임지지 않습니다.__  


## 실행환경 관련  
- eFriend expert는 Windows 환경에서만 사용이 가능합니다. 
- __32비트 Python만 사용이 가능합니다.__
- 한국투자증권 홈페이지에서 Open API 사용신청 후, eFreind expert 프로그램이 설치되어 있어야만 합니다.


## 사용 라이브러리/프레임워크  
- PyQt5
- pandas
- yfinance (미국 주식 가격 조회를 위함)
- pandas_datareader 
- requests (slack 사용하지 않을 경우 생략 가능)

## 파일 설명
- eFriendPy/Core.py : eFriend expert에서 제공하는 공식 API에 대한 wrapper class인 StandardAPIWrapper 클래스가 정의되어 있습니다.  
공식 API와 관련된 자세한 내용은 eFriend expert 공식 메뉴얼 및 eFriend viewer를 참고하세요.  
- eFriendPy/API.py : StandardAPIWrapper 클래스를 사용하여 고수준 API를 구현한 예제 코드입니다. 
- api_sample.py : eFriendPy/API.py 파일에서 정의한 고수준 API를 사용하는 간단한 예제입니다.
- slack.py, SlackLogger.py : api 사용중 로그 메시지를 slack으로 받기 위한 코드입니다 (옵션). 


## 프로그램 실행 방법  
1. eFreind expert 프로그램 실행 후 로그인한다.   
2. eFriendPy/Core.py, eFriendPy/API.py, api_sample.py 등을 참고하여 원하는 프로그램을 작성한다.
3. __관리자권한으로__ 작성한 코드를 실행한다.  
