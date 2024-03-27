#!/usr/bin/env python3
''' type-annotated func for sum_list '''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns sum of list of floats'''
    return sum(input_list)