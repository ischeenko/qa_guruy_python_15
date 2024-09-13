import allure
from selene import browser, have, command, by, be


class SearchByFilterAndAddCart:
    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def search_and_input_searchbar(self, value):
        with allure.step('Вводим текст в поисковую строку'):
            browser.element('._input_1su1z_19').type(value)
            browser.element('._button_1su1z_11').click()

    def add_filter(self, value):
        with allure.step('Выбираем фильтр "Новинки" и смотрим товар'):
            browser.element('._content_pjvgk_16').click()
            browser.element('._marker_g6flk_21').click()
            browser.element(by.partial_text(value)).should(be.visible)

    def choose_product(self):
        with allure.step('Кликаем на карточку товара'):
            browser.element('#RTLACK621502').click()

    def close_pop_up(self):
        with allure.step('Закрываем поп-ап'):
            browser.element('.icon_40').click()

    def choose_size(self, value):
        with allure.step('Выбираем размер'):
            browser.element('._arrow_8karg_76').click()
            browser.element(by.partial_text(value)).should(be.visible).click()

    def add_to_cart(self):
        with allure.step('Добавляем в корзину'):
            browser.element('.x-button_48').perform(
                command.js.scroll_into_view).click()
            browser.element('.x-button_link_32').click()

    def should_product(self):
        with allure.step('Проверяем, что в корзине 1 товар'):
            browser.element('.ui-checkout-cart__products-count').should(
                have.text('1 '
                          'товар'))
