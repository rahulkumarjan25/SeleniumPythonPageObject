from Pages.BasePage import BasePage
from Utilities import configReader


class CarsBase:

    def __init__(self, driver):
        self.driver=driver

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(configReader.readConfig("locators", "carsPageTitle_XPATH")).text

    def getCarNameandPrice(self):
        carNames=self.driver.find_elements_by_xpath(configReader.readConfig("locators","carsName_XPATH"))
        carsPrice=self.driver.find_elements_by_xpath(configReader.readConfig("locators","carsPrice_XPATH"))

        for i in range(1,len(carsPrice)):
            print((carNames[i].text + "--------Price are ----- "+carsPrice[i].text).encode('utf8'))

