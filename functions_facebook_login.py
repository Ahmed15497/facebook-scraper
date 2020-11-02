# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 02:27:12 2020

@author: ahmed
"""



from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from time import sleep
import json
from pathlib import Path






def init_driver(myConfigDriver):
    
    gecko_driver = myConfigDriver.GECKO_DRIVER
    load_image = myConfigDriver.LOAD_IMAGE
    user_agent = myConfigDriver.USER_AGENT
    is_headless = myConfigDriver.HEADLESS
    
    
    
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
    firefox_profile.set_preference("media.volume_scale", "0.0")
    firefox_profile.set_preference("dom.webnotifications.enabled", False)
    if not load_image:
        firefox_profile.set_preference('permissions.default.image', 2)
    
    if user_agent != None:
        firefox_profile.set_preference("general.useragent.override", user_agent)


    options = Options()
    options.headless = is_headless
    
        
        
    
    try:
        current_path = os.path.dirname(os.path.abspath(__file__))
    except:
        current_path = '.'



    driver = webdriver.Firefox(executable_path=  current_path + '/' + gecko_driver,
                               firefox_profile = firefox_profile,
                               options= options)
    
    
    return driver

"""
def get_url(url, driver, sleep_duration=5):
    driver.get(url)
    sleep(sleep_duration)
    # elimnate the pop ups   
    close_popup = driver.find_elements_by_css_selector('.-close_popup')
    
    if len(close_popup) > 0:
        for i in range(len(close_popup)):
            close_popup[i].click()
            
    return

 """
 


class FacebookLogin():
    
    def __init__(self, driver, myConfigurationWebsite, myAccount):
        self.driver = driver
        self.COOKIES_PATH = myConfigurationWebsite.COOKIES_PATH
        self.BASE_URL = myConfigurationWebsite.BASE_URL

    
    
    
    def facebook_login_cookies(self):
        driver = self.driver
        path_json = self.COOKIES_PATH
        BASE_URL = self.BASE_URL
        
        driver.get(BASE_URL)
        cookies = ''
        if Path(path_json).is_file():
            with open(path_json, 'r', encoding = 'utf8') as ck_file:
                cookies = ck_file.read()
        
        if cookies != '':
            cookies = json.loads(cookies)
            
        if len(cookies) > 0:
            for cookie in cookies:
                driver.add_cookie(cookie)
                
        sleep(5)
        
        driver.get(f"{BASE_URL}/settings")
        
        try :
            driver.find_element_by_id('email')
            # cookies are expired, we need to delete our cookies
            open(path_json,'w').truncate()
            return False
        except:
            driver.get(BASE_URL)
            print("I used cookies")
            return True
        
        return False
    
    def facebook_login_normal(self):
        
        driver = self.driver
        path_json = self.COOKIES_PATH
        BASE_URL = self.BASE_URL

        
        driver.get(BASE_URL)
        sleep(5)
        email_field = driver.find_element_by_name('email')
        email_field.clear()
        email_field.send_keys(self.myAccount.email)
        sleep(5)
        
        password_field = driver.find_element_by_name('pass')
        password_field.clear()
        password_field.send_keys(self.myAccount.password)
        sleep(5)
        
        login_button = driver.find_element_by_name('login')
        login_button.click()
        sleep(5)
        
        cookies_list = driver.get_cookies()
        ck_file = open(path_json,'w',encoding = 'utf8')
        ck_file.write(json.dumps( cookies_list ))
        ck_file.close()
        
        return
    
    def facebook_login(self):
        is_login = self.facebook_login_cookies()
        if is_login == False:
            self.facebook_login_normal()
        return



    
