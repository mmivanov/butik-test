# -*- coding: utf-8 -*-
import time
from behave import *
from selenium.webdriver.common.keys import Keys


@then('I try to login correct')
def login_correct(context):
    login_value = str(context.config['auth']['login_correct'])
    password_value = str(context.config['auth']['password_correct'])
    login(context, login_value, password_value)


@then('I try to login incorrect')
def login_incorrect(context):
    login_value = str(context.config['auth']['login_incorrect'])
    password_value = str(context.config['auth']['password_incorrect'])
    login(context, login_value, password_value)


def login(context, login_value, password_value):
    form_selector = '.content__block .authorization__login-form'
    form = context.browser.find_element_by_css_selector(form_selector)
    login_field = context.browser.find_element_by_css_selector(form_selector + ' input[type=text]')
    password_field = context.browser.find_element_by_css_selector(form_selector + ' input[type=password]')

    login_field.send_keys(login_value)
    password_field.send_keys(password_value)
    password_field.send_keys(Keys.RETURN)
