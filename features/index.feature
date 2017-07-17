Feature: Butik main page
  Scenario: Check some text in search results
  Given I am on page https://stage.butik.ru/
    When I click on "Женщинам"
    Then I see url https://stage.butik.ru/women/
    Then I see text "Интернет-магазин"
    When I click on "Мужчинам"
    Then I see url https://stage.butik.ru/men/
