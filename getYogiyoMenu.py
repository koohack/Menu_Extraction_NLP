import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import menu_ex

class getYogiyo():
    def __init__(self):
        ### driver setting
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.s = Service("chromedriver.exe")
        self.driver = selenium.webdriver.Chrome(service=self.s)

        self.out=[]
        self.menus=[]

    def getInfo(self, url):
        ### set url
        self.driver.get(url)

        ### get total menu title
        wait = WebDriverWait(self.driver, 5)
        menuTitles=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "panel.panel-default.ng-scope")))

        ### Click all of the menu title to get menus
        length = len(menuTitles)
        print(length)
        subXPathFront = "/html/body/div[6]/div[2]/div[1]/div[4]/div/div["
        subXPathBack = "]/div[1]/h4/a/span"
        out = []
        for i in range(length):
            if i == 0:
                continue
            else:
                titleNum = str(i + 1)
                fullXPath = subXPathFront + titleNum + subXPathBack
                title = self.driver.find_element(By.XPATH, fullXPath)
                out.append(title)
                title.click()
            if i==length-1:
                break

        ### get menu from web page
        out1 = []
        menus = []
        for item in menuTitles:
            menuName = item.find_elements(By.CLASS_NAME, "menu-text")
            for temp in menuName:
                names = temp.find_elements(By.CLASS_NAME, "menu-name.ng-binding")
                for i in names:
                    line = i.text
                    if not line:
                        continue
                    else:
                        out1.append(i)
                        menus.append(line)

        self.out=out1
        self.menus=menus
        time.sleep(0.2)

        ### menus = list of menus, out = selenium module
        return menus, out1

    def clickMenu(self, numList, countList):
        ### click the menu
        for i, index in enumerate(numList):
            temp=self.out[index]
            temp.click()

            ### Count the menu
            count=countList[i]
            if count > 1:
                plus=self.driver.find_element(By.CLASS_NAME, "plus")
                for _ in range(count-1):
                    plus.click()
            time.sleep(0.5)

            ### put menu to the cart
            btn=self.driver.find_element(By.CLASS_NAME, "btn-add-cart")
            btn.click()
            time.sleep(0.5)

        ### final order
        orderBtn=self.driver.find_element(By.CLASS_NAME, "btn.btn-lg.btn-ygy1.btn-block")
        orderBtn.click()

    def findMenus(self, str):
        string, token, replacer=menu_ex.ExtractMenu(str, self.menus)

        out=[]
        for r, menuName in replacer:
            for i, name in enumerate(self.menus):
                if name==menuName:
                    out.append(i)
                    break
        return out

    def getFinalResult(self):
        wait = WebDriverWait(self.driver, 5)
        finalMenus = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-group-item ng-scope")))

        out=[]
        for item in finalMenus:
            menuName=item.find_element(By.CLASS_NAME, "ng-blinding").text
            menuCost=item.find_element(By.CLASS_NAME,"order-price ng-binding").text
            out.append((menuName, menuCost))

        return out

    def closeDriver(self):
        #print(self.driver.page_source)
        a=self.driver.page_source
        self.driver.quit()
        return a

if __name__=="__main__":
    url = "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAiA-9uNBhBTEiwAN3IlNGGAGpgyNKd2BlArX4uVTrCSoKJ47RQoachcLeGUQ1oN-0RGQwNbHBoC0lgQAvD_BwE#/341607/"
    yogiyo=getYogiyo()
    menus, menusBlock=yogiyo.getInfo(url)

    str="돈부리 하나 카츠돈 두개 "
    position=yogiyo.findMenus(str)
    print(position)

    yogiyo.clickMenu(position, [1,1])
    time.sleep(1)
    a=yogiyo.closeDriver()

    f=open("t.html", "a", encoding="utf-8")
    t=a.split("\n")
    for item in t:
        f.write(item)




