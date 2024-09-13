import allure
from selene import browser, have, be, by


class ChangeTown:
    def open(self):
        with allure.step('Открываем главнюу страницу'):
            browser.open('/')

    def click_geo(self):
        with allure.step('Кликаем на стрелочку с названиаем города'):
            browser.element('._left_s9bjz_34').click()

    def close_pop_up(self):
        with allure.step('Подтверждаем, что выбираем другой город'):
            browser.element(by.partial_text('Выбрать')).click()

    def choose_town(self, value):
        with allure.step('Выбираем город из списка'):
            browser.element(by.partial_text(value)).click()

    def choose_button(self):
        with allure.step('Кликаем кнопку "Перейти"'):
            browser.element(by.partial_text('Перейти')).click()

    def should_town(self, value):
        with allure.step(
                'Проверям, что наша геопозиция изменилась на выбранный '
                'город'):
            browser.element('._left_s9bjz_34').should(have.text(f'г. {value}'))
