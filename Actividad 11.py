propetarios ={}
print("\n Pago de impuesto vehicular")
cant_user = int(input("Cuantos usuarios desesea ingresar: "))
for i in range(cant_user):
    print(f"\n Propetiario #{i+1}")
    number_nit = int(input("Ingrese su numero de NIT: "))
    complet_name = input("Ingrese su nombre completo porfavor: ")
    number_contact = int(input("Ingrese su número de telefono: "))
    cantidad_vehiculos = int(input("Ingrese la cantidad de vehiculos que posee: "))
    vehiculos = {}
    for j in range(cantidad_vehiculos):
        print(f"\n Vehivulo {j+1}")
        placa = input("Ingrese el numero de placa: ")
        marca = input("Ingrese la marca de su vehiculo: ")
        modelo = int(input("Ingrese el modelo de su vehiculo (ej: corrolla): "))
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
    }
