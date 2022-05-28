import pytest
from Pages.RegistrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_SignUP(BaseTest):
    @pytest.mark.parametrize(" name, phoneNum, email, country, city, username, password",
                             dataProvider.get_data("LoginTest"))
    def test_doSignUp(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Test do SignUp Started")
        regPage = RegistrationPage(self.driver)
        regPage.fillForm(name, phoneNum, email, country, city, username, password)
        log.logger.info("Test do SignUp Finished")
        # driver.find_element_by_id("email").send_keys(username)
        # driver.find_element_by_id("pass").send_keys(password)
        # allure.attach(driver.get_screenshot_as_png(), name="testlogin", attachment_type=AttachmentType.PNG)
        # assert False
