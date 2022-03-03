
from selenium import webdriver
import selenium
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
    class _Action():
        '''
            NOTICE:
            U can write your code here to add some custom Actions/Functions.
            "found_element" will express the element that Selenium returned via driver_wait()'s CSS selector.

            **IMPORTANT!** You should always return a List type object.
            => That makes the process can operate code multiple times easier.
        '''

        def CLICK(self): return ["found_element.click()"]

        def INPUT(self,  text: str, speed: int = 30):
            action_list = []
            for i in list(text):
                action_list.append(f"found_element.send_keys('{i}')")
                action_list.append(f"sleep(randint(0, {speed})/100)")
            return action_list

    Action = _Action()

    WAITING_TIMEOUT = 120
    FIND_FREQUENCY = 1

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    opt_arg = [" --start-maximized", "--disable-user-media-security",
               f"user-agent={user_agent}", "blink-settings=imagesEnabled=false"]
    for i in opt_arg:
        opt.add_argument(i)

    def __init__(self) -> None:

        self.driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=self.opt)

        #self.driver = webdriver.Chrome(service=Service("src/chromedriver.exe"), options=self.opt)

    def driver_wait(self, CSS_selector: str, expression: list = ["None"], waiting_timeout: int = WAITING_TIMEOUT, find_frequency: int = FIND_FREQUENCY):

        found_element = WebDriverWait(self.driver, waiting_timeout, find_frequency).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_selector)))
        for i in expression:
            eval(i)

        return found_element

    def get_into_meet(self, email: str = EMAIL, password: str = PASSWORD):

        # ^ MEET
        self.driver.get("https://meet.google.com/")

        # ^ LOGIN
        self.driver_wait(
            "#drawer > div > div.glue-header__container.glue-header__container--cta > div.primary-meet-cta.tbd > div > span:nth-child(1)", self.Action.CLICK())

        # ^ EMAIL
        self.driver_wait("#identifierId", self.Action.INPUT(email))
        self.driver_wait("#identifierNext > div > button > span",
                         self.Action.CLICK())

        # ^ PASSWORD
        self.driver_wait(
            "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", self.Action.INPUT(password))
        self.driver_wait("#passwordNext > div > button > span",
                         self.Action.CLICK())

        # ^ MEET CODE
        self.driver_wait("#i3", self.Action.INPUT("nkhhs"))
        self.driver_wait("#yDmH0d > c-wiz > div > div.S3RDod > div > div.Qcuypc > div.Ez8Iud > div > div.KOM0mb >    div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb > button > span",
                         self.Action.CLICK())

        # ^ ENTRY
        self.driver_wait("#yDmH0d > c-wiz > div > div > div:nth-child(9) > div.crqnQb > div > div > div.vgJExf > div > div > div.d7iDfe.NONs6c > div > div.Sla0Yd > div > div.XCoPyb > div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt.M9Bg4d > span", self.Action.CLICK())

        print("\nDONE")

    #! It might doesn't work. SAD

    def meet_setting_optimize(self):
        """
        #^ CLOSE DIALOG BOX

        self.driver_wait("#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.vdySc.pMgRYb.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > span", self.Action.CLICK())



        #^ SETTINGS
        self.driver_wait("#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.rceXCe > div > div.Nsfdxf > div > div.VfPpkd-xl07Ob-XxIAqe-OWXEXe-oYxtQd > div:nth-child(1) > span > button > div.VfPpkd-Bz112c-Jh9lGc", self.Action.CLICK())

        #^ LAYOUT
        self.driver_wait("body > div.VfPpkd-xl07Ob-XxIAqe.VfPpkd-xl07Ob.q6oraf.P77izf.txTes.OcVpRe.CIYi0d.jvUMfb.yOCuXd.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul > li:nth-child(3) > span.VfPpkd-StrnGf-rymPhb-b9t22c.O6qLGb", self.Action.CLICK())
        self.driver_wait("#c33", self.Action.CLICK())

        """
        pass

    def quit_meet(self):
        self.driver_wait(
            "#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.rceXCe > div > div.NHaLPe.CoOyx > span > button", self.Action.CLICK())

        self.driver.quit()

    def force_quit(self):
        self.driver.quit()


if __name__ == "__main__":

        m = MEET_driver()
        m.get_into_meet()

        while 1:
            if input() == "QUIT":
                break
            else:
                print("U IDIOT!")

        m.force_quit()

        input()
