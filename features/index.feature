Feature: Butik main page
  Scenario: Check some text in search results
  Given I am on page "https://stage.butik.ru/"
    When I click on link "Женщинам"
    Then I see url "https://stage.butik.ru/women/"
    Then I see text "Универмаг в Москве" in ".store.fr"
    When I click on link "Мужчинам"
    Then I see url "https://stage.butik.ru/men/"
