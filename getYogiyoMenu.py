import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url="https://www.yogiyo.co.kr/mobile/#/348589/"

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
        menuTitles = self.driver.find_elements(By.CLASS_NAME, "panel.panel-default.ng-scope")
        time.sleep(1.5)

        ### Click all of the menu title to get menus
        length = len(menuTitles)
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

        ### get menu from web page
        out = []
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
                        out.append(i)
                        menus.append(line)
        self.out=out
        self.menus=menus
        ### menus = list of menus, out = selenium module
        time.sleep(0.2)
        return menus, out

    def clickMenu(self, menuList, numList, countList):
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


if __name__=="__main__":
    a=getYogiyo()
    b, c=a.getInfo(url)
    a.clickMenu([], [1,2], [1, 2])

    print(b)




