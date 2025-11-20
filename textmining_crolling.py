from selenium import webdriver

# Chrome 웹 드라이버 경로 설정
driver_path = 'C:/Users/dlxod/OneDrive/문서/★★이태연/광운대/3-1/텍스트마이닝/chromedriver.exe'

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome(driver_path)

# 웹사이트 접속
driver.get('https://cafe.naver.com/suhui')

# 게시글 목록 수집
post_elements = driver.find_elements_by_css_selector('.article-board m-tcol-c')

for post_element in post_elements:
    title = post_element.find_element_by_css_selector('.article-board m-tcol-c .article-board a.article-board m-tcol-c').text
    print(title)

# 웹 드라이버 종료
driver.quit()
