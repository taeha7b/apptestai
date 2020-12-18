import time
import platform
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
linux = '/home/kim/bin/chromedriver'
driver_dir = '/Users/taehakim/bin/chromedriver'
if platform.system() == 'Linux':
    driver_dir = linux

with open('./test.json', 'w', encoding='utf-8') as f:
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(driver_dir,options=options)
    driver.get('https://apptest.ai')
    driver.maximize_window()
    time.sleep(1)
    action = ActionChains(driver)
    count =0
    temp = dict()
    temp2= []
    
    find_element = len(driver.find_elements_by_tag_name('a'))
    for num in range(find_element):
        webelement = driver.find_elements_by_tag_name('a')[num]
        
        temp[f'webelement{count}'] = webelement.text
        count+=1
    json.dump(temp, f)
 

with open('./test.json', "r") as f:
    json_data = json.load(f)
    check = []
    count = 1
    for i in json_data.values():
        try:
            name = i

            if name in check:
                continue
            elif name == 'contact@apptest.ai' and platform.system() == 'Linux':
                continue
 
            check.append(name)
            elem = driver.find_element_by_partial_link_text(name)
            if platform.system() == 'Linux':
                ActionChains(driver).move_to_element(elem).perform()
                ActionChains(driver).key_down(Keys.CONTROL).click().perform()
            else:
                ActionChains(driver).move_to_element(elem).perform()
                ActionChains(driver).key_down(Keys.COMMAND).click().perform()

            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(3)
                driver.save_screenshot(f'./screenshot/screenshot{count}.png')
                count += 1
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(3)
        except Exception as e:
            print(e)
            continue

    driver.quit()
