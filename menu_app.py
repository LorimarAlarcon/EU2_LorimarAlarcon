def agregar_compras(compras, total_gastado):
    precio = float(input("Ingrese el monto de la compra: "))
    compras.append(precio)
    total_gastado += precio
    print(f"Compra agregada correctamente.")
    return total_gastado
def mostrar_compras(compras):
    if len(compras) == 0:
        print("No hay compras registradas.")
    else:
        for i, (precio) in enumerate(compras, start=1):
            print(f"{i}.- ${precio:.2f}")

def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total_gastado = agregar_compras(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta Luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
