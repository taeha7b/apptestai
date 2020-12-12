import time
import platform
import json
from selenium import webdriver


linux = '/home/kim/bin/chromedriver'
driver_dir = '/Users/taehakim/bin/chromedriver'
if platform.system() == 'Linux':
    driver_dir = linux

with open('./test.json', 'r') as f:
    json_data = json.load(f)
    driver = webdriver.Chrome(driver_dir)
    driver.maximize_window()
    driver.get('https://apptest.ai')
    time.sleep(1)
    num = 1
    for i in json_data:
        xpath = json_data[i]
        driver.find_element_by_xpath(xpath).click()
        if i == 'email':
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            num+=1

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(5)
            driver.save_screenshot(f'./screenshot/screenshot_{num}_{i}.png')
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            num+=1
        else:
            driver.save_screenshot(f'./screenshot/screenshot_{num}_{i}.png')
            num+=1
        if i == 'documents':
            driver.back()
            time.sleep(1)

driver.quit()