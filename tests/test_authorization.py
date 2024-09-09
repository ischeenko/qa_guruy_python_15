import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.authorization import Authorization

authorization = Authorization()

@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Authorization')
@allure.severity(Severity.MINOR)
def test_authorization():

    authorization.open()
    authorization.open_modal_window()
    authorization.fill_email()
    authorization.fill_password()
    authorization.submit()
