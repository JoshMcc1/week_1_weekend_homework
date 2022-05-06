import pdb


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, no_of_pets):
    pet_shop["admin"]["pets_sold"] += no_of_pets


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)

    return pets_by_breed


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

    return None


def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_to_remove):
    if cash_to_remove != None:
        customer["cash"] -= cash_to_remove
    else:
        return 0


def get_customer_pet_count(customer):
    total_pets = 0
    for pet in customer["pets"]:
        total_pets += 1
    return total_pets


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None or pet["price"] >= customer["cash"]:
        print("Invalid pet, or not enough funds")
    else:
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
