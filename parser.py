from datetime import datetime
from selenium import webdriver

# chrome driver 경로
chrome_driver = 'C:\\Users\\admin\\PycharmProjects\\jasosel\\chromedriver_win32\\chromedriver'
driver = webdriver.Chrome(chrome_driver)
driver.implicitly_wait(3)

# 자소설닷컴 채용 페이지 접속
driver.get('https://jasoseol.com/recruit')
driver.implicitly_wait(5)

# 필터 클릭
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div[1]').click()

# it 인터넷 클릭 =>
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div[5]/span/i').click()

# 기업분류 0 대기업, 1 중견, 2 공공기관 3 기타
business_type_base = '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/'
business_type = ['div[1]','div[2]','div[3]','div[4']

# 원하는 기업분류 체크하기
wanted_business_type = [0, 1]
for bt in wanted_business_type:
    xpath = business_type_base + business_type[bt]
    driver.find_element_by_xpath(xpath).click()
    driver.implicitly_wait(2)

# 채용형태 0 신입, 1 경력, 2인턴, 3 계약직
division_type_base = '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/'
division_type = ['div[1]', 'div[2]', 'div[3]', 'div[4]']

# 원하는 채용형태 체크하기
wanted_division_type = [0, 2]
for dt in wanted_division_type:
    xpath = division_type_base + division_type[dt]
    driver.find_element_by_xpath(xpath).click()
    driver.implicitly_wait(2)


print(datetime.today().__str__()[:10].replace('-',''))
driver.quit()