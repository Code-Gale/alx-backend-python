#!/usr/bin/env python3
''' type-annotated function sum_mixed_list '''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns sum of list of mixed floats and ints'''
    return sum(mxd_lst)
