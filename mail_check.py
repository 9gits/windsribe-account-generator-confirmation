import time

import global_value as g

confirmation_url = "https://windscribe.com/signup/confirmemail/"
filepath = "./account.txt"
confirmation = "fail"

def mail(driver):
    #get mail-address
    time.sleep(3)
    while True:
        try:
            mail_address_field = driver.find_element_by_xpath('//*[@id="mail"]')
            g.mail_address = mail_address_field.get_attribute('value')
            if "Loading" in g.mail_address :
                continue
            else :
                break
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
    print("*DEBUG* mail_confirmation")
    time.sleep(20)
    print("*DEBUG* open mail")
    #set screen
    set_screen(driver)

    time_start = time.time()
    time_end = 0

    #open mail
    while True:
        if time_end - time_start > 60 :
            return -1
        try:
            open_mail_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a')
            open_mail_btn.click()
            break
        except:
            time.sleep(2)
            time_end = time.time()


    #wait
    print("*DEBUG* opened mail")
    time.sleep(20)
    print("*DEBUG* start confirmation mail")
    #set screen
    set_screen(driver)

    time_start = time.time()
    time_end = 0

    #click confirmation-button
    while True:
        if time_end - time_start > 60 :
            return -1
        try:
            confirmation_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/p[5]/a')
            confirmation_btn.click()
            break
        except:
            time.sleep(2)
            time_end = time.time()


    #check confirmation
    cur_url = driver.current_url
    if confirmation_url in cur_url:
        print("confirmation successful")
        confirmation = "confirmation success"
    else :
        print("confirmation failed")

    write_confirmation(confirmation)

    
def write_confirmation(confirmation):
    #open file mode:'a'
    with open(filepath,'a') as file:
        print(confirmation,file=file)
        print('\n',file=file)

def scroll_down(self, speed):
    # get page height
    height = self.browser.execute_script("return document.body.scrollHeight")

    # scroll
    for i in range(1, height, speed):
        self.browser.execute_script("window.scrollTo(0, " + str(i) + ");")

def set_screen(driver):
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    print("set screen")
    time.sleep(5)