from typing import List


def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        