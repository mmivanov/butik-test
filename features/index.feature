Feature: Butik main page
  Scenario: Check some text in search results
  Given I am on page "https://stage.butik.ru/"
    When I click on "ЖЕНЩИНАМ"
    Then I see url "https://stage.butik.ru/women/"
    Then I see text "Интернет-магазин" in ".header__center-box"
    When I click on "МУЖЧИНАМ"
    Then I see url "https://stage.butik.ru/men/"
