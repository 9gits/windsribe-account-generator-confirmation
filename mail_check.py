from asyncore import write
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ssl

import global_value as g


path = "./chromedriver.exe"
url = "https://temp-mail.org/?data1=disposableemail_p.2.bestbuytable.cta_t.2_l.en_pid.9441_fpid.6921"
account_url = "https://windscribe.com/myaccount?hello"
confirmation_url = "https://windscribe.com/signup/confirmemail/"
filepath = "./account.txt"

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

confirmation = "fail"

def mail(driver):
    #get mail-address
    time.sleep(3)
    while True:
        try:
            mail_address_field = driver.find_element_by_xpath('//*[@id="mail"]')
            g.mail_address = mail_address_field.get_attribute('value')
            if g.mail_address != "Loading." :
                break
            else :
                continue
        except:
            time.sleep(2)
    #print(mail_address)

    #wait
    time.sleep(5)


def mail_confirmation(driver):
    #//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/p[5]/a
    #https://windscribe.com/signup/confirmemail/
    #https://temp-mail.org/en/view/620bb5f06774da057d7b76d5
    #//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a

    #wait
    #print("*DEBUG* mail_confirmation")
    time.sleep(40)
    #print("*DEBUG* open mail")

    #open mail
    while True:
        try:
            open_mail_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a')
            open_mail_btn.click()
            break
        except:
            time.sleep(2)


    #wait
    #print("*DEBUG* opened mail")
    time.sleep(30)
    #print("*DEBUG* start confirmation mail")

    #click confirmation-button
    while True:
        try:
            confirmation_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/p[5]/a')
            confirmation_btn.click()
            break
        except:
            time.sleep(2)


    #check confirmation
    cur_url = driver.current_url
    if confirmation_url in cur_url:
        print("confirmation successful")
        confirmation = "success"
    else :
        print("confirmation failed")

    write_confirmation(confirmation)

    
def write_confirmation(confirmation):
    #open file mode:'a'
    with open(filepath,'a') as file:
        print(confirmation,file=file)
        print('\n',file=file)