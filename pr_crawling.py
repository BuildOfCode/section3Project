from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('https://store.steampowered.com/tags/en/Story%20Rich?flavor=contenthub_toprated&offset=21')
driver.implicitly_wait(3)

li = []
time.sleep(15)
games = driver.find_element_by_xpath('//*[@class="facetedbrowse_FacetedBrowseItems_NO-IP"]/div[1]/div/div/div/div/a')
print(games.get_attribute("href"))


for i in range(0, 720):
    driver.get(f'https://store.steampowered.com/tags/en/Story%20Rich?flavor=contenthub_toprated&offset={i}')
    time.sleep(15)
    a = driver.find_element_by_xpath('//*[@class="facetedbrowse_FacetedBrowseItems_NO-IP"]/div[1]/div/div/div/div/a')
    b = a.get_attribute("href")
    li.append(b)

with open('gameslist.txt','w',encoding='UTF-8') as f:
    for name in li:
        f.write(name+'\n')
f.close()

