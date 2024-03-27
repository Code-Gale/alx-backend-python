#!/usr/bin/env python3
''' type-annotated func for multiplier '''


def make_multiplier(multiplier: float) -> callable:
    '''returns a function that multiplies a float by multiplier'''
    def multiply(n: float) -> float:
        '''returns product of n and multiplier'''
        return n * multiplier
    return multiply