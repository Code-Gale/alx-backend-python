#!/usr/bin/env python3
''' type-annotated func for multiplier '''


import typing


def make_multiplier(multiplier: float) -> typing.callable:
    '''returns a function that multiplies a float by multiplier'''
    def multiply(n: float) -> float:
        '''returns product of n and multiplier'''
        return n * multiplier
    return multiply