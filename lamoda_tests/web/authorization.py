import os
import allure
from selene import browser, be, by, have
from dotenv import load_dotenv


class Authorization:
    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')
    def open_modal_window(self):
        with allure.step('Открываем модальное окно входа'):
            browser.element('.x-button').should(have.text('Войти')).click()
    def fill_email(self):
        with allure.step('Заполняем почту'):
            browser.element('.input-material__input[type="text"]').type(
                os.getenv('loginAuth'))
    def fill_password(self):
        with allure.step('Заполняем пароль'):
            browser.element('._iconShow_104pm_17').click()
            browser.element('.input-material__input[name="password"]').type(
                os.getenv('passAuth'))
    def submit(self):
        with allure.step('Кликаем кнопку войти'):
            browser.element('._submit_7r0bx_31').click()



    # browser.element('._text_1jcg6_41').wait_until(be.visible)
    # browser.element('._text_1jcg6_41').click()
    # browser.element('._dropdown_nmt8v_15').should(be.visible)
    # browser.element('._item_nmt8v_2').should(have.text('Выйти')).click()
