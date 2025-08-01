propetarios ={}
print("\n Pago de impuesto vehicular")
cant_user = int(input("Cuantos usuarios desesea ingresar: "))
for i in range(cant_user):
    print(f"\n Propetiario #{i+1}")
    number_nit = int(input("Ingrese su numero de NIT: "))
    while number_nit in propetarios:
        print(f"El numero de nit {number_nit} ya existe")
        number_nit = int(input("Vuelva a ingresar su numero de NIT: "))
    complet_name = input("Ingrese su nombre completo porfavor: ")
    while True:
        number_contact = int(input("Ingrese su número de teléfono: "))
        encontrado = False
        for datos in propetarios.values():
            if "Telefono" in datos and datos["Telefono"] == number_contact:
                print(f"El númerode telefono  {number_contact} ya fue registrado.")
                encontrado = True
                break
        if not encontrado:
            break
    cantidad_vehiculos = int(input("Ingrese la cantidad de vehiculos que posee: "))
    vehiculos = {}
    for j in range(cantidad_vehiculos):
        print(f"\n Vehiculo {j+1}")
        placa = input("Ingrese el numero de placa: ")
        marca = input("Ingrese la marca de su vehiculo: ")
        modelo = input("Ingrese el modelo de su vehiculo (ej: corrolla): ")
        anio = int(input("Ingrese el año de su vehiculo: "))
        estado_impuesto = input("Ingrese si a pagado su impuesto (si/no): ")
        vehiculos[placa] = {
            "Marca": marca,
            "Modelo": modelo,
            "Año": anio,
            "Impuesto": estado_impuesto
        }
    propetarios[number_nit] = {
        "Nombre": complet_name,
        "Telefono":number_contact,
        "Cantidad de vehiculos": cantidad_vehiculos,
        "Vehiculos": vehiculos,
    }
for number_nit,datos in propetarios.items():
    print(f"\n Numero de NIT: {number_nit}")
    print(f"Nombre: {datos['Nombre']}")
    print(f"Telefono: {datos['Telefono']}")
    print(f"Cantidad de vehiculos: {datos['Cantidad de vehiculos']}")
    for placa, carr in datos['Vehiculos'].items():
        print(f"\n Numero de placa{placa} ")
        print(f"Marca: {carr['Marca']}")
        print(f" Modelo: {carr['Modelo']}")
        print(f" Año: {carr['Año']}")
        print(f" Estado de su impuesto: {carr['Impuesto']}")