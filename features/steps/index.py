# -*- coding: utf-8 -*-

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


@given('I am on page "{url}"')
def open_url(context, url):
    context.browser.get(url)


@when('I click on link "{link_text}"')
def link_click(context, link_text):
    link = context.browser.find_element_by_link_text(link_text)
    assert link, 'ссылка ' + link_text + ' не найдена'
    link.click()


@when('I above "{text}"')
def text_hover(context, text):
    element = context.browser.find_element_by_link_text(text)

@when('I push button with id "{button_id}"')
def button_click(context, button_id):
    button = context.browser.find_element_by_css_selector('#' + button_id)
    assert button, 'Button with id ' + button_id + ' not found'
    button.click()


@then('I see url "{url}"')
def assert_url(context, url):
    current_url = context.browser.current_url
    assert current_url == url, 'url страницы не соответствует ожидаемому'


@then('I see text "{text}" in "{selector}"')
def find_text(context, text, selector):
    page = WebDriverWait(context.browser, 120).until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    page_text = page.text
    assert text in page_text, 'на странице не найден текст: ' + text


@then('I don\'t see text "{text}" in "{selector}"')
def find_text(context, text, selector):
    page = WebDriverWait(context.browser, 120).until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    page_text = page.text
    assert text not in page_text, 'на странице найден текст: ' + text


@then('I input text "{text}" to field with name "{field_selector}"')
def input_text(context, text, field_selector):
    field = context.browser.find_element_by_css_selector(field_selector)
    field.send_keys(text)


@then('I submit form "{form_selector}"')
def submit_form(context, form_selector):
    form = context.browser.find_element_by_css_selector(form_selector)
    form.send_keys(Keys.RETURN)


def sleep(seconds):
    time.sleep(int(seconds))
