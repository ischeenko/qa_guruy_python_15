import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.check_header import CheckHeader

check_header = CheckHeader()
@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Check Header')
@allure.severity(Severity.MINOR)
def test_header():

    check_header.open()
    check_header.should_have_exacts_texts_numbers('Идеи',
    'Новинки','Одежда','Обувь','Аксессуары',
    'Бренды','Premium','Спорт','Resale',
    'Красота','Дом','Sale%')
