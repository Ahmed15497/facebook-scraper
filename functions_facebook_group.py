# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:59:18 2020

@author: ahmed
"""

from time import sleep
import re
import urllib




class GetMembersIDs:
    def __init__(self, driver, myConfigurationWebsite):
        self.driver = driver
        self.BASE_URL = myConfigurationWebsite.BASE_URL
      

    
    def get_members(self, driver, count = 0):
        members = driver.find_elements_by_xpath('//div[@data-name="GroupProfileGridItem"]')[count:]
        BASE_URL = self.BASE_URL
        members_ids_list = []
        for member in members:
            member_id = member.find_elements_by_css_selector('a')[0].get_attribute('href')
          
            if 'profile.php' in member_id:
                member_id = re.findall(r'%s(\d+)' % 'id=', member_id)[0]
                #print('id')
                #continue
            else:
                member_id = member_id.partition("?")[0]
                member_id = member_id[member_id.index(f"{BASE_URL}/") + len(f"{BASE_URL}/"):]
                #print('no id just name')
            members_ids_list.append(member_id)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        return members_ids_list
    
    
    
    def get_members_IDs(self, group_id, min_members = 200):
        driver = self.driver
        BASE_URL = self.BASE_URL
        
        driver.get(f"{BASE_URL}/groups/{group_id}/members")
        group_grid = driver.find_elements_by_id('pagelet_group_members')[0]
        group_members_number = group_grid.find_elements_by_css_selector('span')[0].text
        group_members_number = int(group_members_number.replace(',', ''))
        if group_members_number < min_members:
            min_members = group_members_number 
    
        total_ids = []
        count = 0
        
        pageHeight = driver.execute_script("return document.body.scrollHeight")
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
    
        
        while (count < min_members and (totalScrolledHeight+15) < (pageHeight)):
            members_ids_list = self.get_members(driver, count = count)
            count +=  len(members_ids_list)
            total_ids.append(members_ids_list)
            pageHeight = driver.execute_script("return document.body.scrollHeight")
            totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
            
        return total_ids



##########################################################################
    

class SearchGroups:
    
    def __init__(self, driver, myConfigurationWebsite):
        self.driver = driver
        self.FACEBOOK_SEARCH = myConfigurationWebsite.FACEBOOK_SEARCH
        

    def insert_search(self, search):
        return self.FACEBOOK_SEARCH + search 
    
    def choose_public_groups(self, driver):
        group_types = driver.find_elements_by_xpath(".//div[@role='group']")[0]
        public_type = group_types.find_elements_by_xpath(".//input[@type='radio']")[1]
        driver.execute_script("arguments[0].click();", public_type)
        return
    
    
    
    
    def get_groups(self, driver, count = 0):
        groups = driver.find_elements_by_xpath('//div[@data-testid="browse-result-content"]')[count:]
        groups_ids_list = []
        for group in groups:
           group_link = group.find_elements_by_css_selector('a')[0].get_attribute('href')
           group_id = re.search('%s(.*)%s' % ('groups/', '/'), group_link).group(1)
           groups_ids_list.append(group_id)
    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        return groups_ids_list
    
    
    def get_groups_IDs(self, driver, min_groups = 200):
        total_ids = []
        count = 0
        
        pageHeight = driver.execute_script("return document.body.scrollHeight")
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
        #print(f'Page height: {pageHeight}, Scroll height: {totalScrolledHeight}')
        
        while (count < min_groups and (totalScrolledHeight+15) < (pageHeight)):
            groups_ids_list = self.get_groups(driver, count = count)
            count +=  len(groups_ids_list)
            total_ids.append(groups_ids_list)
            pageHeight = driver.execute_script("return document.body.scrollHeight")
            totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
    
    
        return total_ids
    
    
    
    def search_groups(self, search_string, min_groups = 200):
        driver = self.driver
        
        search_string = urllib.parse.quote_plus(search_string)
        search_url = self.insert_search(search_string)
        driver.get(search_url)
        sleep(2)
        self.choose_public_groups(driver)
        total_ids = self.get_groups_IDs(driver, min_groups)
        return total_ids
