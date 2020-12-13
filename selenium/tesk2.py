import time
import platform
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
        some_tag = driver.find_element_by_xpath(xpath)
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        find_element = driver.find_element_by_xpath(xpath).click()
        
        if i == 'email' and platform.system() == 'Linux':
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            num+=1
        elif i == 'email' and platform.system() != 'Linux':
            num+=1
            pass

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