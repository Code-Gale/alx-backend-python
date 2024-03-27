#!/usr/bin/env python3
''' type-annotated func for to_kv '''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns tuple with k and v'''
    return (k, v * v)
