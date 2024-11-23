import math

def calculate_points(receipt):
    points = 0

    # Rule 1: Points for retailer name
    retailer = receipt.get("retailer", "")
    points += sum(1 for c in retailer if c.isalnum())

    # Rule 2: Round dollar amount
    total = float(receipt.get("total", 0))
    if total.is_integer():
        points += 50

    # Rule 3: Total is multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: Points for every two items
    items = receipt.get("items", [])
    points += (len(items) // 2) * 5

    # Rule 5: Length of item description
    for item in items:
        desc = item["shortDescription"].strip()
        if len(desc) % 3 == 0:
            price = float(item["price"])
            points += math.ceil(price * 0.2)

    # Rule 6: Odd purchase day
    purchase_date = receipt.get("purchaseDate", "01-01").split("-")
    day = int(purchase_date[-1])
    if day % 2 != 0:
        points += 6

    # Rule 7: Purchase time between 2:00 PM and 4:00 PM
    purchase_time = receipt.get("purchaseTime", "00:00").split(":")
    hour = int(purchase_time[0])
    if 14 <= hour < 16:
        points += 10

    return points
