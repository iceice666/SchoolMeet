from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import randint
from time import sleep

global EMAIL, PASSWORD
EMAIL = "903@kmhjh.kh.edu.tw"
PASSWORD = "12345678"


class MEET_driver():
    MEET_States = "INIT"

    WAITING_TIMEOUT = 120
    FIND_FREQUENCY = 1

    CLICK = "found_element.click()"

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    opt_arg = [" --start-maximized", "--disable-user-media-security",
               f"user-agent={user_agent}", "blink-settings=imagesEnabled=false"]
    for i in opt_arg:
        opt.add_argument(i)

    driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=opt)

    def driver_wait(self, driver, element, expression="None", waiting_timeout=WAITING_TIMEOUT, find_frequency=FIND_FREQUENCY):

        found_element = WebDriverWait(driver, waiting_timeout, find_frequency).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        eval(expression)

        return found_element

    def driver_input(self, element, text):
        for i in list(text):
            element.send_keys(i)
            sleep(randint(0, 30)/100)

    def get_into_meet(self, email=EMAIL, password=PASSWORD):

        # ^ MEET
        self.driver.get("https://meet.google.com/")
        self.MEET_States = "ON WEBSITE"

        # ^ LOGIN
        self.driver_wait(
            self.driver, "#drawer > div > div.glue-header__container.glue-header__container--cta > div.primary-meet-cta.tbd > div > span:nth-child(1)", self.CLICK)

        # ^ EMAIL
        _element = self.driver_wait(self.driver, "#identifierId")
        self.driver_input(_element, email)
        self.driver_wait(self.driver, "#identifierNext > div > button > span",
                         self.CLICK)

        # ^ PASSWORD
        _element = self.driver_wait(
            self.driver, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        self.driver_input(_element, password)
        self.driver_wait(
            self.driver, "#passwordNext > div > button > span", self.CLICK)

        # ^ MEET CODE
        _element = self.driver_wait(self.driver, "#i3")
        self.driver_input(_element, "nkhhs")
        self.driver_wait(self.driver, "#yDmH0d > c-wiz > div > div.S3RDod > div > div.Qcuypc > div.Ez8Iud > div > div.KOM0mb >    div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb > button > span",
                         self.CLICK)

        # ^ ENTRY
        self.driver_wait(self.driver, "#yDmH0d > c-wiz > div > div > div:nth-child(9) > div.crqnQb > div > div > div.vgJExf > div > div > div.d7iDfe.NONs6c > div > div.Sla0Yd > div > div.XCoPyb > div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt.M9Bg4d > span", self.CLICK)

        print("\nDONE")
        self.MEET_States = f"Logged as {email} "

    def meet_setting_optimize(self):
        """
        #^ CLOSE DIALOG BOX

        self.driver_wait(self.driver,"#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.vdySc.pMgRYb.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > span", self.CLICK)



        #^ SETTINGS
        self.driver_wait(self.driver,"#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.rceXCe > div > div.Nsfdxf > div > div.VfPpkd-xl07Ob-XxIAqe-OWXEXe-oYxtQd > div:nth-child(1) > span > button > div.VfPpkd-Bz112c-Jh9lGc", self.CLICK)

        #^ LAYOUT
        self.driver_wait(self.driver,"body > div.VfPpkd-xl07Ob-XxIAqe.VfPpkd-xl07Ob.q6oraf.P77izf.txTes.OcVpRe.CIYi0d.jvUMfb.yOCuXd.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul > li:nth-child(3) > span.VfPpkd-StrnGf-rymPhb-b9t22c.O6qLGb", self.CLICK)
        self.driver_wait(self.driver,"#c33", self.CLICK)

        """
        pass

    def quit_meet(self):
        self.MEET_States = "QUITTING"
        self.driver_wait(
            self.driver, "#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.rceXCe > div > div.NHaLPe.CoOyx > span > button", self.CLICK)

        self.driver.quit()
        self.MEET_States = "OFFLINE"
    def force_quit(self):
        self.driver.quit()
        self.MEET_States = "OFFLINE"


if __name__ == "__main__":
    try:
        m = MEET_driver()
        m.get_into_meet()

        while 1:
            if input() == "QUIT":
                break
            else:
                print("U IDIOT!")

        m.force_quit()
    except Exception as e:
        print(e)

    input()
