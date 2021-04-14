#
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
count = 0
while count < 6700:

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    print(count)

    driver.get("https://ardes.bg/komponenti/video-karti")
    search = driver.find_element_by_name("q")
    search.send_keys ("radeon rx 6700 xt ")
    search.send_keys (Keys.RETURN)
    time.sleep(5)

    driver.get("https://www.jarcomputers.com")
    search = driver.find_element_by_name("q")
    search.send_keys ("radeon rx 6700 xt")
    search.send_keys (Keys.RETURN)
    time.sleep(1)

    driver.get("https://plasico.bg")
    search = driver.find_element_by_name("search")
    search.send_keys ("radeon rx 6700 xt")
    search.send_keys (Keys.RETURN)
    time.sleep(1)

    driver.get("http://www.mostbg.com/most/PriceList.aspx")
    search = driver.find_element_by_name("tbSearch")
    search.send_keys ("radeon rx 6700 xt")
    search.send_keys (Keys.RETURN)
    time.sleep(1)

    driver.get("https://www.emag.bg/homepage?ref=emag_CMP-27257_stock-busters-16-19-03-2021")
    search = driver.find_element_by_name("query")
    search.send_keys ("radeon rx 6700 xt")
    search.send_keys (Keys.RETURN)
    time.sleep(5)

    driver.get("https://www.vario.bg/komponenti-video-karta")
    time.sleep(1)

    driver.get("https://plesio.bg")
    search = driver.find_element_by_name("keyword")
    search.send_keys ("radeon rx 6700 xt")
    search.send_keys (Keys.RETURN)
    time.sleep(1)

#    driver.get("https://gplay.bg")
#   search = driver.find_element_by_class("ng-pristine ng-valid ng-empty ng-valid-minlength ng-touched")
#   search.send_keys ("radeon rx 6700")
#   search.send_keys (Keys.RETURN)
#   time.sleep(2)

    driver.get("https://www.vali.bg/bg/catalog#!?category=388&s=price_desc")
#   search = driver.find_element_by_name("ng-pristine ng-valid ng-empty ng-valid-minlength ng-touched")
#   search.send_keys ("radeon rx 6700")
#   search.send_keys (Keys.RETURN)
    time.sleep(15)

    driver.get("https://www.pazaruvaj.com")
    search = driver.find_element_by_name("st")
    search.send_keys ("radeon rx 6700 xt ")
    search.send_keys (Keys.RETURN)
    time.sleep(5)
    count = count + 1

driver.quit()
