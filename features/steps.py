from lettuce import world
from lettuce import step

import actualstack

GLOBALSTACK = actualstack.jackstack()
GLOBALLIST = []


@step ('the values')
def many_values(step):
    for value in step.hashes:
        GLOBALLIST.append(value['numbs'])

@step ('the values are pushed')
def push_values(step):
    for item in GLOBALLIST:
        GLOBALSTACK.push(item)

@step ('the values are on the stack')
def assert_values(step):
    tempNode = GLOBALSTACK.head
    GLOBALLIST.reverse()
    for item in GLOBALLIST:
        assert item == tempNode.value, "I got %s" % str(item)
        tempNode = tempNode.fwdNode

@step ('a value is popped')
def pop_and_lock(step):
    world.number = GLOBALSTACK.pop()

@step ('the popped value is (\d+)')
def assert_popped(step, expected):
    assert world.number == expected, "I got %s" % str(expected)

@step ('the node is gone from the stack')
def assert_removal(step):
    assert GLOBALSTACK.head.value == '2', "I got %s" % str(GLOBALSTACK.head.value)