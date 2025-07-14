
menu = {'Pizza Margarita': 8.99, 
        'Hamburguesa Clásica': 5.99, 
        'Ensalada César': 7.5, 
        'Agua Mineral': 1.5}

def place_order(selected_food, money):
    try:
        if selected_food not in menu: 
            raise ValueError("El alimento seleccionado no está en el menú")
        if menu[selected_food] > money: 
            raise ValueError("No se disponen de suficientes fondos para realizar el pedido")     
        total_price = menu[selected_food]
        print(f"Pedido realizado con éxito. Alimento seleccionado: {selected_food}, Total a pagar: {total_price}€")
    except ValueError as err:
        print(f"Error en el pedido: {err}")


# Imprimir el menú
def imprimir_menu():
    print()
    for elem in menu:
            print(f'{elem}: {menu[elem]}')


# Prueba 1
imprimir_menu()
selected_food = 'Pizza Margarita'
money = 10
place_order(selected_food, money) # Pedido realizado con éxito. Alimento seleccionado: Pizza Margarita, Total a pagar: 8.99€

# Prueba 2
imprimir_menu()
selected_food = 'Pizza Margarita'
money = 2
place_order(selected_food, money) # ValueError: No se disponen de suficientes fondos para realizar el pedido

# Prueba 3
imprimir_menu()
selected_food = 'Sandwich mixto'
money = 10
place_order(selected_food, money) # ValueError: El alimento seleccionado no está en el menú
