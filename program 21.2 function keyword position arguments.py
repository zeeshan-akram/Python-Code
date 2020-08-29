def arguments(first, last):
    print(f"Hi! {first} {last}")
    print("Calculating your total cost....")


def calc_cost(total_cost, shipping_cost, discount):
    final_cost = total_cost + shipping_cost - discount
    print(f"Your Final bill is: ${final_cost}")


arguments("Zeeshan", last="Akram")
calc_cost(total_cost=50, shipping_cost=10, discount=2)