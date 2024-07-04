
def registro(listanombre,listadireccion,listahospital,listainsumos,listabono,listatotal):
    nombre=input("Ingrese Nombre y Apellido del Paciente: ")
    direccion=input("Indique direccion del Paciente: ")
    hospital=int(input("Indique dias de Hospitalizacion: ")) 
    totalH=hospital*90000
    hospitalizacion=print(f"Total Hospitalizacion: {totalH}")
    insumos=int(input("Total Insumos Medicos: "))
    bono=int(input("Bonificacion en %: "))
    totalB=(totalH+insumos)*0.70
    bonificacion=print(f"Total Bonificacion: {totalB}")
    total=(totalH+insumos)-totalB
    print(f"Total a Pagar: {total}")

    
    
    #listanombre.append(nombre)
    #listadireccion.append(direccion)
    #listahospital.append(hospital)
    #listainsumos.append(insumos)
    #listabono.append(bono)

def cobros(listanombre,listadireccion,listahospital,listainsumos,listabono,listatotal):
    print(f"Paciente {nombre}")
    print(f"Direccion{direccion}")
    print(f"Hospitalizacion{hospital}")
    print(f"Insumos{insumos}")
    print(f"Bonificacion{bono}")
    print(f"Total{total}")
