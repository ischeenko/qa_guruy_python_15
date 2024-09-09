import allure
from selene import browser, be, have, command


class SearchByArticle:
    with allure.step('Открываем главную страницу'):
        def open(self):
            browser.open('/')

    with allure.step('В поисковую строку вводим артикул'):
        def open_search_input(self, value):
            browser.element('._input_1su1z_19').type(value)
            browser.element('._button_1su1z_11').click()

    with allure.step('Закрываем поп-ап'):
        def close_popup(self):
            browser.element('.d-modal__close-button').click()

    with allure.step('Сверям артикул'):
        def should_article(self, value):
            browser.element('._title_ujgyh_37').perform(
                command.js.scroll_into_view).should(have.text('О товаре'))
            browser.element('.ui-product-description-attribute-sku').should(
                have.text(value))
