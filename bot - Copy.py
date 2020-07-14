from selenium import webdriver
from time import sleep

class btbot:
    def __init__(self,us,ps):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(us)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(ps)
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)

    def unf(self):
        self.driver.find_element_by_xpath("//a[@href=\"/__usnm__/\"]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[@href=\"/__usnm__/followers/\"]").click()
        sleep(3)
        followers=self._get_names()
        self.driver.find_element_by_xpath("//a[@href=\"/__usnm__/following/\"]").click()
        sleep(3)
        following=self._get_names()
        not_following=[names for names in following if names not in followers]
        print(not_following)
        

    def _get_names(self):
        sleep(5)
        sb=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        lh,ch=0,1
        while lh != ch:
            lh=ch
            sleep(2)
            ch=self.driver.execute_script(""" arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight;""",sb)
        li=sb.find_elements_by_tag_name('a')
        tt=[tt.text for tt in li if tt.text !='']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return tt
        
       
abc = btbot("__username__","__password__")
abc.unf()

