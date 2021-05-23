from typing import List, Union


def load_data(file: str) -> List[str]:
    """Generates a list of links from a .txt file."""
    with open(file) as f:
        content = [line.rstrip() for line in f]
    return content


def in_stock_list(links: list, in_stock_checker) -> List[List[Union[str, bool]]]:
    """Returns whether products are in stock from a list of links of products."""
    output = []
    for link in links:
        output.append(in_stock_checker(link))
    return output
