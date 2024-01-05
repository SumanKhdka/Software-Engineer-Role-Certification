import requests


def getProductsinRange(category, minPrice, maxPrice):
    # Initialize variables
    total_items = 0
    current_page = 1

    while True:
        # Make HTTP GET request to the API
        url = f"https://jsonmock.hackerrank.com/api/inventory?category={category}&page={current_page}"
        response = requests.get(url)
        data = response.json()

        # Check if there are no more pages
        if current_page > data['total_pages']:
            break

        # Process items on the current page
        for item in data['data']:
            price = item['price']
            # Check if the item belongs to the specified price range
            if minPrice <= price <= maxPrice:
                total_items += 1

        # Move to the next page
        current_page += 1

    return total_items


# Example usage:
category = "Accessories"
minPrice = 800.0
maxPrice = 900.0

result = getProductsinRange(category, minPrice, maxPrice)
print(result)
