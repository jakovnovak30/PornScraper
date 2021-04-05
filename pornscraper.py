from selenium import webdriver

browser = webdriver.Chrome('/home/jakov/Documents/pornscraper/chromedriver')

def pornhub(pojam):
    url = "https://pornhub.com"
    browser.get(url)

    serch = browser.find_element_by_xpath('//*[@id="searchInput"]')
    serch.click()
    serch.send_keys(pojam + '\n')

    rezultati = browser.find_element_by_xpath('//*[@id="videoSearchResult"]')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from pornhub.com")
    return

def xvideos(pojam):
    url = "https://xvideos.com"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="disclaimer-content"]/button').click()
    serch = browser.find_element_by_name('k')
    try: serch.click()
    except: print('Nebrem kliknuti')
    serch.send_keys(pojam + '\n')

    rezultati = browser.find_element_by_xpath('//*[@id="content"]')
    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from xvideos.com")
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

    rezultati = browser.find_element_by_xpath('//*[@id="listResultContainer"]/ul')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from pornmd.com")
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

    rezultati = browser.find_element_by_xpath('//*[@id="content-thumbs"]/div[4]')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from xnxx.com")
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

    rezultati = browser.find_element_by_xpath('/html/body/div[1]/main/div/article/div[4]')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from xhamster.com")

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

    rezultati = browser.find_element_by_xpath('//*[@id="main"]/div[2]')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from erome.com")

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

    rezultati = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div/section/div/div')

    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from hqporner.com")

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

    rezultati = browser.find_elements_by_class_name('ll-loaded')

    for rezultat in rezultati:
        naslov = rezultat.get_attribute('alt')
        if pojam.lower() in naslov.lower():
            print(naslov + " from pornpics.com")

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

    rezultati = browser.find_element_by_xpath('//*[@id="main"]/center/table/tbody/tr/td[2]/form/table/tbody/tr/td/table[2]/tbody')
    tekst = rezultati.text
    polje = tekst.split('\n')

    for naslov in polje:
        if pojam.lower() in naslov.lower():
            print(naslov + " from imagefap.com")

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

    rezultati = browser.find_elements_by_class_name('lazyload')

    for rezultat in rezultati:
        naslov = rezultat.get_attribute('alt')
        if pojam.lower() in naslov.lower():
            print(naslov + " from pornmd.com")

    return

def main():
    upis = input("Unesite pojam za pretrazivanje: ")
    upis2 = input("Video ili slike? (upisi 'v' ili 's')")

    if upis2 == "v":
        hqporner(upis)
        erome(upis)
        xhamster(upis)
        xnxx(upis)
        pornmd(upis)
        xvideos(upis)
        pornhub(upis)
    elif upis2 == "s":
        print("Work in progress...")
        pornpics(upis)
        pornmdslike(upis)
        imagefap(upis)
    else:
        print("Try again")
        main()

    return

if __name__ == '__main__':
    main()
