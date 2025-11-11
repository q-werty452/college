def add_dish(menu, name, price, difficulty):
    if difficulty < 1 or difficulty > 5:
        print("Сложность должна быть от 1 до 5")
        return
    menu[name] = {"цена": price, "сложность": difficulty}
    print(f"Блюдо {name} добавлено в меню")

def add_chef(chefs, name, skill_level):
    if skill_level < 1 or skill_level > 5:
        print("Уровень мастерства должен быть от 1 до 5")
        return
    chefs[name] = {"уровень": skill_level}
    print(f"Повар {name} добавлен")

def create_order(menu, chefs, orders, guest_name, dishes, chef_name):
    if chef_name not in chefs:
        print("Такого повара нет")
        return
    
    
    for dish in dishes:
        if dish not in menu:
            print(f"Блюдо {dish} отсутствует в меню")
            return
    
   
    chef_level = chefs[chef_name]["уровень"]
    for dish in dishes:
        if menu[dish]["сложность"] > chef_level:
            print(f"Повар {chef_name} не может приготовить {dish}")
            return
    
   
    order = {
        "гость": guest_name,
        "блюда": dishes,
        "повар": chef_name
    }
    orders.append(order)
    print("Заказ создан")

def calculate_order_total(menu, order):
    total = 0
    for dish in order["блюда"]:
        total += menu[dish]["цена"]
    return total


menu = {
    "Паста": {"цена": 400, "сложность": 3},
    "Стейк": {"цена": 900, "сложность": 5}
}

chefs = {
    "Айбек": {"уровень": 4},
    "Марина": {"уровень": 5}
}

orders = [
    {"гость": "Канат", "блюда": ["Паста", "Стейк"], "повар": "Марина"}
]


add_dish(menu, "Салат", 300, 2)
add_chef(chefs, "Иван", 3)
create_order(menu, chefs, orders, "Алия", ["Паста", "Салат"], "Айбек")


for order in orders:
    total = calculate_order_total(menu, order)
    print(f"Заказ для {order['гость']}: {total} рублей")