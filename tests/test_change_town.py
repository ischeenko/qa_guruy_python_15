import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.change_town import ChangeTown

change_town = ChangeTown()
@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Change Town')
@allure.severity(Severity.MINOR)
def test_change_town():

    change_town.open()
    change_town.click_geo()
    # change_town.close_pop_up()
    change_town.choose_town('Казань')
    change_town.choose_button()
    change_town.should_town('Казань')
