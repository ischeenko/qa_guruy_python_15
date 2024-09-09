import allure
from selene import browser, have, be, by


class ChangeTown:
    with allure.step('Открываем главнюу страницу'):
        def open(self):
            browser.open('/')

    with allure.step('Кликаем на стрелочку с названиаем города'):
        def click_geo(self):
            browser.element('._left_s9bjz_34').click()

    with allure.step('Подтверждаем, что выбираем другой город'):
        def close_pop_up(self):
            browser.element(by.partial_text('Выбрать')).click()

    with allure.step('Выбираем город из списка'):
        def choose_town(self, value):
            browser.element(by.partial_text(value)).click()

    with allure.step('Кликаем кнопку "Перейти"'):
        def choose_button(self):
            browser.element(by.partial_text('Перейти')).click()

    with allure.step('Проверям, что наша геопозиция изменилась на выбранный '
                     'город'):
        def should_town(self, value):
            browser.element('._left_s9bjz_34').should(have.text(f'г. {value}'))
