# apptestai
## 과제 I
### 1. Flask 기반으로 간단한 CRUD를 할 수 있는 API 서버를 만드세요(Version 1)
- Flask 기반으로 간단한 API서버를 만듭니다
- DB: 고객 ID, 고객명, 고객 생년월일, 고객에 대한 관리 메모를 가진 테이블을 만드세요 (MySQL)
- API서버: 해당 테이블에 대한 CRUD API 5개를 작성
    - 고객 정보 목록 조회 (paging 처리할 것)
    - 고객 정보 상세 조회 (고객 ID로 고객의 상세 정보 조회)
    - 고객 정보 생성(insert)
    - 고객 정보 변경(update)
    - 고객 정보 삭제(delete)
- 클라이언트: 해당 서버에 대한 API 호출은 Postman을 사용

**`crud_ver1에 구현하였습니다.`**

### 2. 자신이 만든 API 서버에 대하여 개선점을 기술하고, 개선 방향을 도출하세요


### 3. 개선 방향에 따라 version2를 만드세요.
**`crud_ver2에 구현하였습니다.`**

## 과제 II
### 1. Selenium을 사용해서, 다음을 과제를 수행하세요(Version 1).
- https://apptest.ai의 사이트에 대하여
- 첫 화면에서 상단 메뉴(Product, Pricing, Documents, FAQ&Blog, Contatct)를 차례대로 클릭해서 해당 화면으로 이동
- 이동이 완료되면, Contact 화면에서, "Get In Touch With Us" 부분의 각 항목에 임의의 값을 입력 후 "SEND" 버튼 클릭
- 이상의 것을 Selenium을 사용해서 코드로 자동처리해 주세요.

**`selenium/tesk1.py에 구현 하였습니다.`**

### 2. Version1의 내용을 발전시켜서, 다음의 요구사항을 구현해주세요(Version 2).
- https://apptest.ai의 사이트에서, Click 가능한 모든 요소(element)를 추출해주세요.
  - Element의 식별자(id, xpath, class 등 어떤 것이든 해당 element를 다른 element와 구별할 수 있는 식별자)
- 추출된 각 요소를 JSON 파일 형태로 저장하세요.
- JSON 파일을 읽어서, JSON 파일에 있는 element들을 순서대로 click하세요.
- 각 element들이 클릭될 때마다, 해당 화면에 대해서 스크린샷 이미지를 저장하세요.
- 이상의 코드를 어떠한 라이브러리/프레임웍을 사용해도 좋으니, Python 기반으로 작성해 주세요.

**`selenium/tesk2.py에 구현 하였습니다.`**
