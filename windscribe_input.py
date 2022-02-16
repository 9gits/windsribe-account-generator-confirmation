import time

import global_value as g

account_url = "https://windscribe.com/myaccount?hello"
filepath = "./account.txt"


class Account:
    def __init__(self):
        self.name = ''
        self.passowrd = ''

def input_windsribe(driver):
     #click_random_name
    random_nane_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div[2]/a[1]')
    random_nane_btn.click()

    #wait
    time.sleep(7)

    #click_random_password
    random_password_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div[2]/a[2]')
    random_password_btn.click()

    #wait
    time.sleep(10)

    #input mailaddress
    mail_address_form = driver.find_element_by_xpath('//*[@id="signup_email"]')
    mail_address_form.send_keys(g.mail_address)


    #get_account_information
    name_value = driver.find_element_by_xpath('//*[@id="username"]')
    Account.name = name_value.get_attribute('value')

    password_value = driver.find_element_by_xpath('//*[@id="pass1"]')
    Account.password = password_value.get_attribute('value')

    
    #click_create_account
    create_account_btn = driver.find_element_by_xpath('//*[@id="signup_button"]')
    create_account_btn.click()

    #wait
    time.sleep(8)

    #signup-anyway (by no-confirmation)
    #signup_anyway_btn = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/ul/li[1]/a')
    #signup_anyway_btn.click()

    #wait
    time.sleep(10)

    #check successful-creation
    cur_url = driver.current_url
    if cur_url == account_url:
        print("creation successful")
        #close browser
        #driver.close()

        #output information
        print(Account.name)
        print(Account.password)

        #write account information to txtfile
        write_account_information()
        return 0
    else:
        print("creation failed")
        #close browser
        driver.close()
        return -1

    

def write_account_information():
    #open file mode:'a'
    with open(filepath,'a') as file:
        print(Account.name,file=file)
        print(Account.password,file=file)
        #print('\n',file=file)