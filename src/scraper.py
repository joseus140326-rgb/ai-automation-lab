import pandas as pd

products = {
    "Product": [
        "Avocado",
        "Banana",
        "Milk",
        "Eggs",
        "Chicken Breast"
    ],
    "Price_USD": [
        1.49,
        0.59,
        4.99,
        6.49,
        12.99
    ]
}

df = pd.DataFrame(products)

df.to_csv("data/products.csv", index=False)

print(df)
print("Dataset created successfully")
