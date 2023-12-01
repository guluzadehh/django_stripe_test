def make_line_item(item) -> dict:
    return {
        "price_data": {
            "currency": "rub",
            "unit_amount_decimal": item.price * 100,
            "product_data": {
                "name": item.name,
                "description": item.description,
            },
        },
        "quantity": 1,
    }
