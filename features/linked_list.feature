Feature: Singly-linked list
    Implement a linked list with typical features
    
    Scenario: make an empty list
        When I create the list
        Then it has a length of 0
    
    Scenario: add a value
        Given the number 1
        When I insert the number into the list
        And Pop the number off
        Then I see the output 1
    
    Scenario: add many values
        Given the following numbers
            | 1     |
            | 2     |
            | 3     |
        When I insert those numbers
        Then it has a length of 3
        And I Pop the numbers off
        Then I see the following outputs
            | 3     |
            | 2     |
            | 1     |
    
    Scenario: find a value
        Given the following numbers
            | 1     |
            | 2     |
            | 3     |
        When I insert those numbers
        And search for the number 4
        Then I get no output
        Later search for the number 2
        Then I see the output 2