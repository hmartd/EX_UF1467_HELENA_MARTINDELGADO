
menu = {'Pizza Margarita': 8.99, 
        'Hamburguesa Clásica': 5.99, 
        'Ensalada César': 7.5, 
        'Agua Mineral': 1.5}

def place_order(selected_food, money):
    
    if selected_food not in menu:
        raise ValueError("El alimento seleccionado no está en el menú")
    if menu[selected_food] > money:
        raise ValueError("No se disponen de suficientes fondos para realizar el pedido")
    try:     
        total_price = menu[selected_food]
        print(f"Pedido realizado con éxito. Alimento seleccionado: {selected_food}, Total a pagar: {total_price}€")
    except:
        print("Error en el pedido: ValueError (asignado en las sentencias anteriores)")


# Imprimir el menú
for elem in menu:
        print(f'{elem}: {menu[elem]}')


# Prueba 1
selected_food = 'Pizza Margarita'
money = 10
place_order(selected_food, money) # Pedido realizado con éxito. Alimento seleccionado: Pizza Margarita, Total a pagar: 8.99€

# Prueba 2
selected_food = 'Pizza Margarita'
money = 2
place_order(selected_food, money) # ValueError: No se disponen de suficientes fondos para realizar el pedido

# Prueba 3
selected_food = 'Sandwich mixto'
money = 10
place_order(selected_food, money) # ValueError: El alimento seleccionado no está en el menú
