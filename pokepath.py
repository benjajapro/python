import os
os.system("cls")






flag = True
contador_productos = 0
revivir_contador = 0
descuento_valor = 0
descuento_revivir = 0 
suma_revivir = 0
valor = 0
try:
    while flag:
        articulos = int(input("Productos disponibles:\n 1.Pokeball $1000\n 2.Pocion $1500\n 3.Revivir $3000\n 4.Baya $500\n 5.Finalizar la compra\n"))
        
        if articulos == 1: 
            cantidad = int(input("ingrese cantidad de compra\n"))
            valor_articulos = 1000
            contador_productos = valor + 1
            valor = contador_productos + valor_articulos
            print("Has comprado pokeball")
        elif articulos ==2:
            cantidad = int(input("ingrese cantidad de compra\n"))
            valor_articulos = 1500
            contador_productos = valor + 1
            valor = contador_productos + valor_articulos
            print("Has comprado pocion")
        elif articulos ==3:
            cantidad = int(input("ingrese cantidad de compra\n"))
            valor_articulos = 3000
            contador_productos = valor + 1
            valor = contador_productos + valor_articulos
            revivir_contador = revivir_contador + cantidad
            print("Has comprado revivir")
        elif articulos ==4:
            cantidad = int(input("ingrese cantidad de compra\n"))
            valor_articulos = 500
            contador_productos = valor + 1
            valor = contador_productos + valor_articulos
            print("Has comprado baya")
        elif articulos ==5:
            flag = False 
            print("Vuelva pronto!")
        else:
            print("El valor numerico debe ser entre 1 y 5")
        comprar = int(input("Desea seguir comprando? 1.SI 2.NO"))
        if comprar ==1:
            flag = True
        elif comprar ==2:
            flag = False
            
        
        
        if valor > 5000:
            descuento_valor = 0.10
        # if valor > 10:
        #     descuento_valor = 1090
        
        
        
        
        
        
        
        if revivir_contador >=3:
            total_rev = revivir_contador * 3000
            descuento_revivir = total_rev * .15
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
except:
    print(f"El valor debe estar entre las 5 opciones")