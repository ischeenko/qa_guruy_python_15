import allure
from selene import browser, be, have, command


class SearchByArticle:
    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def open_search_input(self, value):
        with allure.step('В поисковую строку вводим артикул'):
            browser.element('._input_1su1z_19').type(value)
            browser.element('._button_1su1z_11').click()

    def close_popup(self):
        with allure.step('Закрываем поп-ап'):
            browser.element('.d-modal__close-button').click()

    def should_article(self, value):
        with allure.step('Сверям артикул'):
            browser.element('._title_ujgyh_37').perform(
                command.js.scroll_into_view).should(have.text('О товаре'))
            browser.element('.ui-product-description-attribute-sku').should(
                have.text(value))
