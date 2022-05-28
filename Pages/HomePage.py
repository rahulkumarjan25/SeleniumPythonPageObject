from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def goToNewCars(self):
        self.moveToElement("newCars_XPATH")
        self.click("findNewCars_XPATH")

        return NewCarsPage(self.driver)

    def goToCompareCars(self):
        self.click("compareCars_XPATH")
