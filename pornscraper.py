from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher as SM
import time

browser = webdriver.Chrome('/home/jakov/Documents/pornscraper/chromedriver')
preciznost = True
prag = 0.6 #mininmalna preciznost za sequence matcher

def xvideos(pojam):
    url = "https://xvideos.com"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="disclaimer-content"]/button').click()
    serch = browser.find_element_by_name('k')
    try: serch.click()
    except: print('Nebrem kliknuti')
    serch.send_keys(pojam + '\n')

    rezultati = browser.find_elements_by_class_name('thumb-under')

    for rezultat in rezultati:
        naslov = rezultat.find_element_by_tag_name('a').get_attribute('title')
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))

    return

def pornmd(pojam):
    url = "https://pornmd.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="searchBarFormWrapper"]/div/form/input')
    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe pornmd')


    reached_page_end = False
    last_height = browser.execute_script("return document.body.scrollHeight;")

    while not reached_page_end:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            curent_height = browser.execute_script("return document.body.scrollHeight;")
            if last_height == curent_height and browser.execute_script("return document.readyState;") == "complete":
                reached_page_end = True
            else:
                last_height = curent_height

    rezultati = browser.find_elements_by_class_name('video-title')

    for rezultat in rezultati:
        naslov = rezultat.find_element_by_tag_name('a').get_attribute('title')
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))

    return

def xnxx(pojam):
    url = "https://xnxx.com"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="disclaimer-content"]/button').click()
    serch = browser.find_element_by_xpath('//*[@id="k"]')
    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe xnxx')

    rezultati = browser.find_elements_by_tag_name('a')

    for rezultat in rezultati:
        naslov = rezultat.get_attribute('title')
        if naslov == None: continue

        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def xhamster(pojam):
    url = "https://xhamster.com"
    browser.get(url)

    browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/button').click()
    serch = browser.find_element_by_xpath('/html/body/div[1]/header/div/div/div[1]/form/input')

    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe xhamster')

    div = browser.find_element_by_tag_name('article')
    rezultati = div.find_elements_by_tag_name('a')

    for rezultat in rezultati:
        try:
            naslov = rezultat.text
        except:
            continue
        if naslov == None: continue
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def erome(pojam):
    url = "https://erome.com"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="home-box"]/a').click()
    browser.find_element_by_xpath('//*[@id="app-navbar-collapse"]/ul/li[1]/a').click()
    serch = browser.find_element_by_xpath('//*[@id="q"]')

    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe erome')

    rezultati = browser.find_elements_by_class_name('album-link')

    for rezultat in rezultati:
        naslov = rezultat.find_element_by_class_name('album-title').text
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def hqporner(pojam):
    url = "https://hqporner.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="searchInput"]')
    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe hqporner')

    rezultati = browser.find_elements_by_class_name('click-trigger')

    for rezultat in rezultati:
        naslov = rezultat.text
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def pornpics(pojam):
    url = "https://pornpics.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="search"]')
    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe pornpics.com')

    reached_page_end = False
    last_height = browser.execute_script("return document.body.scrollHeight;")

    while not reached_page_end:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            curent_height = browser.execute_script("return document.body.scrollHeight;")
            if last_height == curent_height and browser.execute_script("return document.readyState;") == "complete":
                reached_page_end = True
            else:
                last_height = curent_height

    rezultati = browser.find_elements_by_class_name('rel-link')

    for rezultat in rezultati:
        naslov = rezultat.get_attribute('title')
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def imagefap(pojam):
    url = "https://imagefap.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('/html/body/center/table[1]/tbody/tr[1]/td[2]/form/table/tbody/tr/td[1]/input[1]')
    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe imagefap.com')

    rezultati = browser.find_elements_by_tag_name('a')

    for rezultat in rezultati:
        try:
            naslov = rezultat.get_attribute('title')
        except:
            continue
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def pornmdslike(pojam):
    url = "https://pornmd.com"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="searchBarFormWrapper"]/div/form/a').click()
    browser.find_element_by_xpath('//*[@id="searchBarFormWrapper"]/div/form/ul[1]/li[2]').click()
    serch = browser.find_element_by_xpath('//*[@id="searchBarFormWrapper"]/div/form/input')
    try:
        serch.click()
        serch.send_keys(pojam)
        browser.find_element_by_xpath('//*[@id="searchBarFormWrapper"]/div/form/button').click()
    except:
        print('Nekaj jebe pornmd')

    reached_page_end = False
    last_height = browser.execute_script("return document.body.scrollHeight;")

    while not reached_page_end:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            curent_height = browser.execute_script("return document.body.scrollHeight;")
            if last_height == curent_height and browser.execute_script("return document.readyState;") == "complete":
                reached_page_end = True
            else:
                last_height = curent_height

    rezultati = browser.find_elements_by_class_name('img-block')

    for rezultat in rezultati:
        naslov = rezultat.find_element_by_tag_name('a').get_attribute('title')
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))

    return

def spankbang(pojam):
    url = "https://spankbang.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="body-html"]/header/ul/li[2]/form/input')

    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe spankbang')

    rezultati = browser.find_elements_by_class_name('n')

    for rezultat in rezultati:
        naslov = rezultat.text
        if naslov == None: continue
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.get_attribute('href'))

    return

def redgifs(pojam):
    url = "https://redgifs.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="root"]/div/div/header/div[1]/form/div/div/input')

    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe redgifs')

    rezultati = browser.find_elements_by_tag_name('img')

    for rezultat in rezultati:
        try: naslov = rezultat.get_attribute('alt')
        except: continue
        print(naslov)
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " from redgifs.com")
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " from redgifs.com")

    return

def homemoviestube(pojam):
    url = "https://homemoviestube.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="searchform-field-white"]')

    try:
        serch.click()
        serch.send_keys(pojam + '\n')
    except:
        print('Nekaj jebe homemoviestube')

    rezultati = browser.find_elements_by_class_name('film-title')

    for rezultat in rezultati:
        naslov = rezultat.find_element_by_tag_name('a').text
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " -> " + rezultat.find_element_by_tag_name('a').get_attribute('href'))

    return

def porngiphy(pojam):
    url = "https://porngipfy.com/"
    browser.get(url)

    serch = browser.find_element_by_class_name('field')

    #try:
    serch.click()
    serch.send_keys(pojam + '\n')
    #except:
    #    print('Nekaj jebe porngiphy')

    rezultati = browser.find_elements_by_tag_name('img')

    for rezultat in rezultati:
        naslov = rezultat.get_attribute('alt')
        if pojam.lower() in naslov.lower() and preciznost:
            print(naslov + " from porngiphy.com")
        elif not preciznost and SM(None, pojam.lower(), naslov.lower()).ratio() > prag:
            print(naslov + " from porngiphy.com")

    return

def main():
    upis = input("Unesite pojam za pretrazivanje: ")
    upis2 = input("Video ili slike? (upisi 'v' ili 's')")
    upis3 = input("Show only exact matches? (y/n)")

    if upis3 == "n":
        global preciznost
        preciznost = False

    if upis2 == "v":
        hqporner(upis) #linkovi delaju
        erome(upis) #linkovi delaju
        xhamster(upis) #linkovi delaju
        xnxx(upis) #linkovi delaju
        pornmd(upis) #linkovi delaju
        xvideos(upis) #linkovi delaju
        spankbang(upis) #linkovi delaju
        homemoviestube(upis) #linkovi delaju

    elif upis2 == "s":
        pornpics(upis) #linkovi delaju
        pornmdslike(upis) #linkovi delaju
        imagefap(upis) #nekaj jebe
        porngiphy(upis) #popupi guze
        #redgifs(upis)
    else:
        print("Try again")
        main()

    return

if __name__ == '__main__':
    main()
