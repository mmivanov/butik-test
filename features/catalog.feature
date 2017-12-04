Feature: Catalog
  Scenario: Open not empty catalog
    Given I am on page "http://stage.butik.ru/women/"
    When I click on link "Аксессуары"
    Then I see url "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/"
    Then I don't see "0 товаров" in ".f-clr-dkgr"

  Scenario: Open empty catalog
    Given I am on page "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/chekhly/chekhlya-dlya-noutbukov"
    Then I see "0 товаров" in ".f-clr-dkgr"
  
  Scenario: Open product card
    Given I am on page "https://stage.butik.ru/catalog/zhenshchinam/aksessuary/"


