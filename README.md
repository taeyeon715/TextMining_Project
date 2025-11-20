# 텍스트 마이닝 프로젝트

## 프로젝트 개요
이 프로젝트는 Selenium을 활용한 웹 크롤링 및 텍스트 마이닝 프로젝트입니다.
수험생들을 위한 커뮤니티인 네이버 카페 "수능날 만점 시험지를 휘날리며" 일명 "수만휘"에서 수시 합격 수기 게시판에 있는 데이터를 가져와 학교/학과 검색시 해당 학교/학과에 합격한 사람들의 실제 스펙과 후기를 더욱 생생히 담고자 한 프로젝트입니다.

## 파일 구성
- `textmining_crolling.py`: 기본 크롤링 스크립트
- `textmining_crolling_2.ipynb`: 크롤링 코드를 포함한 Jupyter Notebook
- `Textmining_코드설명.ipynb`: 프로젝트 코드 설명 노트북

## 사용 기술
- Python
- Selenium
- BeautifulSoup4
- Pandas
- Pyperclip

## 설치 방법
```bash
pip install selenium beautifulsoup4 pandas pyperclip
```

## 주요 기능
- 네이버 웹사이트 자동 로그인
- 웹 페이지 크롤링
- 데이터 추출 및 분석

## 사용 방법
1. ChromeDriver 설치
2. 필요한 패키지 설치
3. 로그인 정보 설정
4. 스크립트 실행

## 주의사항
- ChromeDriver 경로를 본인의 환경에 맞게 수정해야 합니다
- 로그인 정보는 보안을 위해 별도로 관리해야 합니다
- 웹 크롤링 시 해당 사이트의 robots.txt 및 이용약관을 준수해야 합니다

## 라이선스
이 프로젝트는 교육 목적으로 제작되었습니다.

