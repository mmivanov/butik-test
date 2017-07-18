Feature: Catalog
  Scenario: Open empty catalog
    Given I am on page "http://stage.butik.ru/"
    When I click on "АКСЕССУАРЫ"
    Then I see url "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/"
    Then I don't see "0 товаров" in ".products-count__counter"

  Scenario: Open empty catalog
    Given I am on page "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/chekhly/chekhlya-dlya-noutbukov"
    Then I see "0 товаров" in ".products-count__counter"
  
  Scenario: Open product card
    Given I am on page "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/"


