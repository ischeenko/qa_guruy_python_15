import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.search_by_article import SearchByArticle

search_by_article = SearchByArticle()
@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Search by Article')
@allure.severity(Severity.MINOR)
def test_search_by_article():

    search_by_article.open()
    search_by_article.open_search_input('RTLADQ940501')
    search_by_article.close_popup()
    search_by_article.should_article('RTLADQ940501')
