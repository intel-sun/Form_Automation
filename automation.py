from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



# - 1.open up the form url in chrome browser
form= webdriver.Chrome() #choose chrome
form.get('https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/viewform?edit_requested=true')
form.implicitly_wait(20)

time.sleep(30) #30 second time for the url to load fully

# - 2.filling the form
Name= "Sandra Nettey"
#store path of element into name
name_field= form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# put name into form field (fill form)
print("Element is visible? " + str(name_field.is_displayed()))
name_field.send_keys(Name)

#radio button selection by click
Gender=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span')
Gender.click

Email= "s.nettey.2002@gmail.com"
#store path of element into email
email_field=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# put email into form field (fill form)
email_field.send_keys(Email)

#next button click
nextButton=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
nextButton.click

#school of completion
schoolCompleted= "Accra Wesley Girls High School"
#store path of element into school completed
school_field=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# put school completed into form field (fill form)
school_field.send_keys(schoolCompleted)

#Address
Address= "North Kaneshie"
#store path of element into address
address_field=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
# put address into form field (fill form)
address_field.send_keys(Address)

#Phone Number
phone= "0557497068"
#store path of element 
phone_field=form.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
# put phone number into form field (fill form)
phone_field.send_keys(phone)

#Submit
Submit=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
Submit.click()

#Submit Confirmed
Submit_confirm=web.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div[2]/span/span')
Submit_confirm.click()

#Submit validation
confirmation_text=form.find_element_by_css_selector('.quantumWizButtonPaperbuttonLabel exportLabel')
print(confirmation_text.text)

if (confirmation_text.text)=="Thanks for submitting your contact info!":

    print("Test successful")
else:
    print("Test was not successful")