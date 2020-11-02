# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 02:11:53 2020

@author: ahmed
"""



class Account:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    


class ConfigurationDriver:
    def __init__(self):
        self.GECKO_DRIVER = 'driver-firefox\geckodriver.exe'
        self.LOAD_IMAGE = False
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
        self.HEADLESS = False
        
        
class ConfigurationWebsite:
    def __init__(self):
        self.BASE_URL = 'https://www.facebook.com' 
        self.COOKIES_PATH = 'facebook_cookies.json'
        self.FACEBOOK_SEARCH = 'https://www.facebook.com/search/groups/?q='
        self.GROUP_ID = 'quantumphysicsnews'
    
        
        