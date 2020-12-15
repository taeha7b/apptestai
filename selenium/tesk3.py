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

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(driver_dir,options=options)
driver.get('https://apptest.ai')
driver.maximize_window()
time.sleep(1)
action = ActionChains(driver)

temp =[]
find_element = len(driver.find_elements_by_tag_name('a'))
for i in range(find_element):
    j = driver.find_elements_by_tag_name('a')[i]
    temp.append(j)

check = []
count = 1
for i in temp:
    try:
        name= i.text.replace(" ", "")
        link = i.get_attribute('href')
        print("텍스트:",name, "링크:",link)
       
        if link in check:
            continue
        elif name == 'contact@apptest.ai' and platform.system() == 'Linux':
            continue
        elif name == '.search-1{fill:#58468c;fill-rule:evenodd;}':
            continue

        check.append(count)
        check.append(link)
    

        if platform.system() == 'Linux':
            ActionChains(driver).move_to_element(i).perform()
            ActionChains(driver).key_down(Keys.CONTROL).click().perform()
        else:
            ActionChains(driver).move_to_element(i).perform()
            ActionChains(driver).key_down(Keys.COMMAND).click().perform()
        
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(5)
            driver.save_screenshot(f'./screenshot/screenshot{count}.png')
            count += 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
   
    except Exception as e:
        print(e)
        continue

driver.quit()
