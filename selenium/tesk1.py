import time
import platform
from selenium import webdriver

linux = '/home/kim/bin/chromedriver'
driver_dir = '/Users/taehakim/bin/chromedriver'
if platform.system() == 'Linux':
    driver_dir = linux

driver = webdriver.Chrome(driver_dir)
driver.maximize_window()

driver.get('https://apptest.ai')
time.sleep(1)
mission = [
    '//*[@id="nav-menu-item-9566"]/a/span/span',
    '//*[@id="nav-menu-item-10038"]/a/span/span',
    '//*[@id="nav-menu-item-10030"]/a/span/span',
    '//*[@id="nav-menu-item-9691"]/a/span/span',
    '//*[@id="nav-menu-item-8787"]/a/span/span'
    ]

for xpath in mission:
    time.sleep(2)
    driver.find_element_by_xpath(xpath).click()
    if xpath == '//*[@id="nav-menu-item-10030"]/a/span/span':
        time.sleep(1)
        driver.back()
    elif xpath == '//*[@id="nav-menu-item-8787"]/a/span/span':
        elem = driver.find_element_by_xpath('//*[@id="wpcf7-f1216-p1183-o2"]/form/div[2]/div[1]/p/span/input')
        elem.send_keys('셀레니움 테스트1')
        elem = driver.find_element_by_xpath('//*[@id="wpcf7-f1216-p1183-o2"]/form/div[2]/div[2]/p/span/input')
        elem.send_keys('셀레니움 테스트2')
        elem = driver.find_element_by_xpath('//*[@id="wpcf7-f1216-p1183-o2"]/form/div[2]/div[3]/p/span/input')
        elem.send_keys('셀레니움 테스트3')
        elem = driver.find_element_by_xpath('//*[@id="wpcf7-f1216-p1183-o2"]/form/div[3]/p/span/textarea')
        elem.send_keys('셀레니움 테스트4')
        driver.find_element_by_xpath('//*[@id="wpcf7-f1216-p1183-o2"]/form/div[4]/div/p/input').click()
        time.sleep(1)

time.sleep(2)
driver.quit()