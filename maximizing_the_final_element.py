#!/bin/python3

import requests
import os

#
# Complete the 'getProductsInRange' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/inventory?category=<category>&page=<pageNumber>
#
# The function is expected to return an Integer value.
# The function accepts String category, Integer minPrice and Integer maxPrice as arguments.
#


def getProductsInRange(category, minPrice, maxPrice):
    # Initialize variables
    total_items = 0
    current_page = 1

    while True:
        # Make HTTP GET request to the API
        url = f"https://jsonmock.hackerrank.com/api/inventory?category={category}&page={current_page}"
        response = requests.get(url)
        data = response.json()

        # Process items on the current page
        for item in data['data']:
            price = item['price']
            # Check if the item belongs to the specified price range
            if minPrice <= price <= maxPrice:
                total_items += 1

        # Check if there are no more pages
        if current_page >= data['total_pages']:
            break

        # Move to the next page
        current_page += 1

    return total_items


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    category = input()

    minPrice = int(input().strip())

    maxPrice = int(input().strip())

    result = getProductsInRange(category, minPrice, maxPrice)

    fptr.write(str(result) + '\n')

    fptr.close()
