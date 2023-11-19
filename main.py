import json
import os

db_file_path = "local_database.json"

if not os.path.exists(db_file_path):
    with open(db_file_path, "w") as f:
        json.dump({}, f)

with open(db_file_path, "r") as f:
    local_data = json.load(f)

while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("Type 'exit' to end the program")

    user_input = input("Enter your choice: ")

    if user_input.lower() == 'exit':
        break

    if user_input == '1':
        data_to_add = {
            "BilledeURL": input("Enter Image URL: "),
            "Name": input("Enter Product Name: "),
            "Ribbon": input("Enter Ribbon Value: "),
            "Description": input("Enter Product Description: "),
            "Categories": input("Enter Product Categories: "),
            "SupermarketAddress": input("Enter Supermarket Address: "),
            "OriginalPrice": float(input("Enter Original Price: ")),
            "PriceNow": float(input("Enter Price Now: ")),
            "Inventory": int(input("Enter Inventory: ")),
        }
        local_data[len(local_data) + 1] = data_to_add

        print("Data added to the local database.")

    elif user_input == '2':

        name_to_remove = input("Enter the product name to remove: ")
        data_to_remove = {key: value for key, value in local_data.items() if value["Name"] == name_to_remove}
        for key in data_to_remove:
            del local_data[key]

        print("Data removed from the local database.")

    else:
        print("Invalid choice. Try again.")

    with open(db_file_path, "w") as f:
        json.dump(local_data, f)
