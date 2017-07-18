Feature: Login

  Scenario: Incorrect login
    Given I am on page "https://stage.butik.ru/login/"
    Then I try to login incorrect
    Then I see url "https://stage.butik.ru/login/"

  Scenario: Login
    Given I am on page "https://stage.butik.ru/login/"
    Then I try to login correct
    Then I don't see text "Неверный email или пароль" in ".authorization__errors"
