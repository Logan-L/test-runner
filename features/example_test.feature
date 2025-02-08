@allure.label.suite:ExampleSuite
Feature: Example feature

    @allure.label.parentSuite:ExampleParentSuite1
    Scenario: This is example test 1
        Given I have this
        When I do this
        Then I should see a pass

    @allure.label.parentSuite:ExampleParentSuite2
    Scenario: This is example test 2
        Given I have this
        When I do this
        Then I should see a failure