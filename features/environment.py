# -*- coding: utf-8 -*-

from selenium import webdriver
import configparser


def before_all(context):
    try:
        config = configparser.ConfigParser()
        config.read('./config.ini')
        context.config = config
    except Exception:
        pass

    context.browser = webdriver.Chrome(str(context.config['browser']['driver']))
    context.browser.maximize_window()
    context.browser.implicitly_wait(int(context.config['browser']['implicity_wait']))
    context.sleep = 3


def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass
