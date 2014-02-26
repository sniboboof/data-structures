Feature: A Stack
push values, pop values

    Scenario: Pushing items
        Given the values
            | numbs |
            | 1     |
            | 2     |
            | 3     |
        When the values are pushed
        Then the values are on the stack
        
    Scenario: Popping items
        Now a value is popped
        Then the popped value is 3
        And the node is gone from the stack