# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
from dataclasses import dataclass
from typing import Dict, Iterable, Optional


@dataclass
class MinMaxObject:
    """
    A class to hold min and max keys.

    ...

    Attributes
    ----------
    min : str
        key of minimum value
    max : str
        key of maximum value
    """

    min: str
    max: str


def find_freq_from_list(lines: Iterable[str]) -> Optional[Dict]:
    """Find frequency of each string in a list.

    Args:
        lines (Iterable[str]): a collection of strings

    Returns:
      (Dict). a dictionary with the frequency of each string
      (None). none if input is empty
    """
    frequencies = {}
    for line in lines:
        if line not in frequencies.keys():
            frequencies[line] = 1
        elif line in frequencies.keys():
            frequencies[line] += 1

    if frequencies == {}:
        return None
    return frequencies


def get_min_max_freq_from_dict(dictionary: Dict) -> Optional[MinMaxObject]:
    """Find keys with min and max values from a dictionary.

    Args:a
      dictionary (Dict): a dictionary with string keys and integer values

    Returns:
      (Tuple[str, str]). A tuple of the min and max key
      (None). Returns none if input is empty
    """
    if len(dictionary.keys()) == 0:
        return None
    return MinMaxObject(max=max(dictionary, key=dictionary.get), min=min(dictionary, key=dictionary.get))


def hist_lib(filename: str) -> Optional[MinMaxObject]:
    """Find keys with min and max values from a file.

    Args:a
      filename (str): a file with lines

    Returns:
      (Tuple[str, str]). A tuple of the min and max key
    """
    with open(filename, "r") as file:
        histogram = find_freq_from_list(file)
    return get_min_max_freq_from_dict(histogram)
