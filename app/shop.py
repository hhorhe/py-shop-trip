from app.utils import get_current_time


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer):
        current_time = get_current_time()
        print(f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity
            total_cost += cost

            if cost.is_integer():
                cost_str = f"{int(cost)}"
            else:
                cost_str = f"{cost:.1f}"
            print(f"{quantity} {product}s for {cost_str} dollars")

        if total_cost.is_integer():
            total_cost_str = f"{int(total_cost)}"
        else:
            total_cost_str = f"{total_cost:.1f}"
        print(f"Total cost is {total_cost_str} dollars")
        print("See you again!")
        print()
