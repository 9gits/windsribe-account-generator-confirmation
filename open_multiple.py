from selenium import webdriver
import time
import undetected_chromedriver.v2 as uc

from mail_check import mail,mail_confirmation,write_confirmation
from windscribe_input import input_windsribe 

import global_value as g

path = "./chromedriver.exe"
url1 = "https://temp-mail.org/?data1=disposableemail_p.2.bestbuytable.cta_t.2_l.en_pid.9441_fpid.6921"
url2 = "https://windscribe.com/signup"
account_url = "https://windscribe.com/myaccount?hello"
filepath = "./account.txt"

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')
#options.add_argument("--proxy-server=socks5://127.0.0.1:9150")

options_ws = uc.ChromeOptions()
#options_ws.add_argument('--headless')
options_ws.add_argument('--disable-gpu')



def open_browser(url):
    driver = webdriver.Chrome(executable_path=path,options=options)
    driver.get(url)
    
def main():
    #open_browser(url1)
    driver_mail = uc.Chrome(executable_path=path,options=options)
    driver_mail.get(url1)

    #open_browser(url2)
    driver_windscribe = uc.Chrome(executable_path=path,options=options_ws)
    driver_windscribe.get(url2)

    #get mail-address
    mail(driver_mail)
    print(g.mail_address)

    #input windsribe-form
    if input_windsribe(driver_windscribe) == -1 :
        driver_mail.close()

    #confirmation mail
    if mail_confirmation(driver_mail) == -1 :
        write_confirmation(confirmation="confirmation fail")
        driver_windscribe.close()
        driver_mail.close()

    #wait
    time.sleep(5)

    #close browser
    driver_mail.close()
    driver_windscribe.close()


if __name__ == '__main__':
    main()
