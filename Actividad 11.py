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
        while True:
            placa = input("Ingrese el número de placa: ")
            repetida = False
            for datos in propetarios.values():
                for placa_existente in datos["Vehiculos"]:
                    if placa_existente == placa:
                        print(f"El numero de placa {placa} ya fue registrado.")
                        repetida = True
                        break
                if repetida:
                    break
            if not repetida:
                break
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
        print(f"\n Numero de placa {placa} ")
        print(f"Marca: {carr['Marca']}")
        print(f" Modelo: {carr['Modelo']}")
        print(f" Año: {carr['Año']}")
        print(f" Estado de su impuesto: {carr['Impuesto']}")

if propetarios:
    print("\n busqueda por identificacion")
    search_identification = int(input("Ingrese el numnero de identificacion  que desea buscar: "))
    if search_identification in propetarios:
        print(f"\n Se encontro el numero de identificacion {search_identification}")
        print(f"Nombre: {propetarios[search_identification]['Nombre']}")
        print(f"Telefono: {propetarios[search_identification]['Telefono']}")
        print(f"Vehiculos que posee: {propetarios[search_identification]['Cantidad de vehiculos']}")
    for placa, datos_vehiculo in propetarios[search_identification]['Vehiculos'].items():
        print(f"\nNumero de placa: {placa}")
        print(f"Marca: {datos_vehiculo['Marca']}")
        print(f"Modelo: {datos_vehiculo['Modelo']}")
        print(f"Año del vehiculo: {datos_vehiculo['Año']}")
        print(f"Impuesto: {datos_vehiculo['Impuesto']}")
    else:
        print("No se encontro ningun propietario con ese numero de identificacion")
else:
    print("Diciconario vacio")
