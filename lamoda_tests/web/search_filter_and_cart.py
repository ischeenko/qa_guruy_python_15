import allure
from selene import browser, have, command, by, be


class SearchByFilterAndAddCart:
    with allure.step('Открываем главную страницу'):
        def open(self):
            browser.open('/')

    with allure.step('Вводим текст в поисковую строку'):
        def search_and_input_searchbar(self, value):
            browser.element('._input_1su1z_19').type(value)
            browser.element('._button_1su1z_11').click()

    with allure.step('Выбираем фильтр "Новинки" и смотрим товар'):
        def add_filter(self, value):
            browser.element('._content_pjvgk_16').click()
            browser.element('._marker_g6flk_21').click()
            browser.element(by.partial_text(value)).should(be.visible)

    with allure.step('Кликаем на карточку товара'):
        def choose_product(self):
            browser.element('#RTLACK621502').click()

    with allure.step('Закрываем поп-ап'):
        def close_pop_up(self):
            browser.element('.icon_40').click()

    with allure.step('Выбираем размер'):
        def choose_size(self, value):
            browser.element('._arrow_8karg_76').click()
            browser.element(by.partial_text(value)).should(be.visible).click()

    with allure.step('Добавляем в корзину'):
        def add_to_cart(self):
            browser.element('.x-button_48').perform(
                command.js.scroll_into_view).click()
            browser.element('.x-button_link_32').click()

    with allure.step('Проверяем, что в корзине 1 товар'):
        def should_product(self):
            browser.element('.ui-checkout-cart__products-count').should(
                have.text('1 '
                          'товар'))
