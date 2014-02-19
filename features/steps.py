from lettuce import step
from lettuce import world

from linked_list import mystack

thelist = None

@step('I create the list')
def create_list(step):
    thelist = mystack()

@step('it has a length of (\d+)')
def test_length(step, expected):
    assert expected == thelist.size(), "got %d" % expected

@step('the number (\d+)')
def the_number(step, num):
    world.number = num

@step('I insert the number into the list')
def insert_number(step):
    thelist.insert(world.number)

@step('Pop the number off')
def pop_it_off(step):
    world.number = thelist.pop()

@step('I see the output (\d+)')
def test_int(step, expected):
    assert world.number == expected, "got %d" % expected

@step('Given the following numbers')
def many_numbers(step):