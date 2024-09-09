from selene import browser, have, command, by, be
import allure


class CheckHeader:
    with allure.step('Открываем главную страницу'):
        def open(self):
            browser.open('/')
    with allure.step('Проверяем хедер на соответствие дизайну'):
        def should_have_exacts_texts_numbers(
                self,
                ideas,
                news,
                clothes,
                shoes,
                accessories,
                brands,
                premium,
                sport,
                resale,
                beauty,
                house,
                sale):
            browser.element('._menuWrapper_i3n1m_94').all(
                '._root_1416b_2').should(have.exact_texts([
                f'{ideas}\n'
                f'{news}\n'
                f'{clothes}\n'
                f'{shoes}\n'
                f'{accessories}\n'
                f'{brands}\n'
                f'{premium}\n'
                f'{sport}\n'
                f'{resale}\n'
                f'{beauty}\n'
                f'{house}\n'
                f'{sale}']))
