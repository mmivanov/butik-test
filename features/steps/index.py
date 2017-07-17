from behave import *


@given('I am on page {url}')
def open_url(context, url):
    context.browser.get(url)


@when('I click on "{link_text}"')
def link_click(context, link_text):
    link = context.browser.find_element_by_link_text(link_text)
    assert link, 'ссылка ' + link_text + ' не найдена'
    link.click()


@then('I see url {url}')
def assert_url(context, url):
    current_url = context.browser.current_url
    assert current_url == url, 'url страницы не соответствует ожидаемому'


@then('I see text "{text}"')
def find_text(context, text):
    page = context.browser.find_element_by_css_selector('body')
    page_text = page.text
    assert text in page_text, 'на странице не найден текст: ' + text