# facebook-scraper v1.0

The Facebook scraper is an automated data collection from the Facebook tool in which you can get the public Groups IDs named after a certain topic (eg. Machine learning) in addition to getting all the members' IDs given a group's ID.

This tool could help the companies to find their targeted future clients easily to contact them later for advertising.




Note: Firefox must be installed on your windows machine to be able to execute that code.

dependencies:

        python 3.x
        time
        re
        urllib
        selenium
        os
        json
        pathlib
    
    
To initialize the Firefox driver found in [./driver-firefox/geckodriver](https://github.com/Ahmed15497/facebook-scraper/blob/main/driver-firefox/geckodriver.exe):

        from config_vars import ConfigurationDriver
        from functions_facebook_login import init_driver
        myConfigDriver = ConfigurationDriver() 
        driver = init_driver(myConfigDriver)

        
    
For Facebook automated login:

        from config_vars import Account, ConfigurationWebsite
        myConfigurationWebsite = ConfigurationWebsite()
        myAccount = Account('example@gmail.com', 'myPassword')
        myFacebookLogin = FacebookLogin(driver, myConfigurationWebsite, myAccount).facebook_login()
        
        
To get the first 200 results of facebook groups' IDs that contain the word "Hello":

        from functions_facebook_group import SearchGroups
        search_topic = 'Hello'
        number_of_groups = 200
        groups_ids = SearchGroups(driver, myConfigurationWebsite).search_groups(search_topic, number_of_groups)
        
        
To get the first 250 results of facebook members' IDs that joind a specific group given its ID:

        from functions_facebook_group import GetMembersIDs
        group_id = '310137172726476'
        min_members = 250
        members_ids = GetMembersIDs(driver, myConfigurationWebsite).get_members_IDs(group_id, min_members = min_members)




        
    
Clone this repositiory and check [scrapper_example.py](https://github.com/Ahmed15497/facebook-scraper/blob/main/scraper_example.py) that illustrates an example that use all classes and methods.






