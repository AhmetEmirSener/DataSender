from selenium import webdriver
from time import sleep
import datetime
import smtplib
import os



msender = "sender@gmail.com"
mpass = "googlegmailpass"
mreceiver = "receiver@gmail.com"
mreceiver2 = "receiver2@gmail.com"
title = " "
content = " "
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
#//////////////////////////////////////

akmaxprice = 1005
akminfiyat = 210
buyminfiyat = 203
bretime = 60                # SECONDS
breetime = bretime / 60     # FOR SHOWING
refreshtime = 15

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--headless")
chrome_options = chromeOptions
driver = webdriver.Chrome(chrome_options)

driver.delete_all_cookies()
driver.implicitly_wait(15)
url =  "https://www.bynogame.com/tr/oyunlar/csgo/skin/ak-47-asiimov-field-tested"
driver.get(url)
while True:

    driver.get(url)
    ak_price = driver.find_element("xpath", "/html/body/div[10]/div[1]/div[2]/div[2]/div/div[3]/div/div/span").text
    ak_model = driver.find_element("xpath", "/html/body/div[10]/div[1]/div[2]/div[1]/div/span").text
    ak_price = ak_price.replace(",", ".")

    now = datetime.datetime.now()   # DATETIME
    icerik = f"\nTarih : {str(now)} \n----- BYNOGAME -----\n {ak_model} = {ak_price} \nBeklenen Fiyat = {str(akmaxprice)} "
    os.system('cls')
    print(icerik)

    # BURAYA SADECE MAX SELL KOYULACAK

    if float(ak_price) <= float(akmaxprice):
        try:
            print("Fiyat uygun...\nMaile giriş yapılıyor...")
            server.login(msender,mpass)
            print("Maile giriş başarılı...")
            sleep(1)
            print("Mail gönderiliyor...")
            icerik = f"{content}  \n  {str(url)}"
            server.sendmail(msender,mreceiver,content)      # FOR RECEIVER
            server.sendmail(msender,mreceiver2,content)     # FOR RECEIVER2
            print("Mail başarıyla gönderildi!")             # SUCCES
            print(f"{str(breetime)} dk bekleme süresi...")  # SLEEP TIME
            sleep(bretime)
            # beklem süresi timer ile yapılacak ve her saniyede rese kalan süreyi göstericek
        except Exception as e:
            print(e)
    else:
        print("Fiyat bekleniyor...")

    sleep(refreshtime)





