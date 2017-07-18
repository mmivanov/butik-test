# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.keys import Keys


@when('I open product card')
def open_product_card(context):
    product = context.browser.find_element_by_css_selector('a.product-card__text.u-url')
    context.browser.get(product.href)


@then('I see "{value}" in "{selector}"')
def text_exists(context, value, selector):
    text = context.browser.find_element_by_css_selector(selector).text
    assert value in text, 'на странице не найден текст: ' + value


@then('I don\'t see "{value}" in "{selector}"')
def login_correct(context, value, selector):
    text = context.browser.find_element_by_css_selector(selector).text
    assert value not in text, 'на странице найден текст: ' + value
