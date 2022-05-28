import time

from Pages.CarsBase import CarsBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
import pytest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Carwale(BaseTest):
    @pytest.mark.skip
    def test_gotoNewcar(self):
        log.logger.info("********Inside New Car Test***********")
        home = HomePage(self.driver)
        home.goToFindNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarTest"))
    def test_SelectCars(self, carBrand, carTitle):
        log.logger.info("********Inside Selected Car Test***********")
        home = HomePage(self.driver)
        car = CarsBase(self.driver)

        if carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCarTitle()

            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            # car.getCarNameandPrice()
        elif carBrand == "Honda":
            home.goToNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            # car.getCarNameandPrice()
        elif carBrand == "Toyota":
            home.goToNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            # car.getCarNameandPrice()
        elif carBrand == "Hyundai":
            home.goToNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            # car.getCarNameandPrice()

        time.sleep(5)

    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarTest"))
    def test_printcarNamesandPrices(self, carBrand, carTitle):
        log.logger.info("********Inside Selected Car Test***********")
        home = HomePage(self.driver)
        car = CarsBase(self.driver)

        if carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCarTitle()

            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            car.getCarNameandPrice()
        elif carBrand == "Honda":
            home.goToNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            car.getCarNameandPrice()
        elif carBrand == "Toyota":
            home.goToNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            car.getCarNameandPrice()
        elif carBrand == "Hyundai":
            home.goToNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car title is :" + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is Not Matching"
            car.getCarNameandPrice()

        time.sleep(5)
