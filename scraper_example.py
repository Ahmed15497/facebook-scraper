# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 02:28:14 2020

@author: ahmed
"""

from config_vars import Account, ConfigurationDriver, ConfigurationWebsite
from functions_facebook_login import init_driver, FacebookLogin
from functions_facebook_group import GetMembersIDs, SearchGroups


# Creating configuration objects that contain important paths
myConfigDriver = ConfigurationDriver() 
myConfigurationWebsite = ConfigurationWebsite()
driver = init_driver(myConfigDriver)


# Input your facebook email and password that the driver will login with them
email = input('Email:')
password = input('Password:')

# Facebook Login (if it is not the first time the driver will use cookies that is saved in this directory under the name of facebook_cookies.json)
myAccount = Account(email, password)
myFacebookLogin = FacebookLogin(driver, myConfigurationWebsite, myAccount).facebook_login()


# groups_ids will return a list of the first 200 facebook groups' IDs that contains the word Machine learning
search_topic = 'Machine learning'
number_of_groups = 200
groups_ids = SearchGroups(driver, myConfigurationWebsite).search_groups(search_topic, number_of_groups)

# members_ids will return a list of the first 250 facebook members' IDs that are in this group ID
group_id = '310137172726476'
min_members = 250
members_ids = GetMembersIDs(driver, myConfigurationWebsite).get_members_IDs(group_id, min_members = min_members)






