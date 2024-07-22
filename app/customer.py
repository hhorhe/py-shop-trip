from app.car import Car


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_trip_cost(self, shop, fuel_price):
        distance_to_shop = self.calculate_distance(self.location, shop.location)
        fuel_cost_to_shop = self.car.fuel_cost(distance_to_shop, fuel_price)
        fuel_cost_back = self.car.fuel_cost(distance_to_shop, fuel_price)
        total_fuel_cost = fuel_cost_to_shop + fuel_cost_back
        total_product_cost = self.calculate_product_cost(shop.products)
        return total_fuel_cost + total_product_cost

    def calculate_distance(self, loc1, loc2):
        return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5

    def calculate_product_cost(self, shop_products):
        total_cost = 0
        for product, quantity in self.product_cart.items():
            if product in shop_products:
                total_cost += shop_products[product] * quantity
        return total_cost
