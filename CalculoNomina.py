def CalculoNomina(Empleados) -> float:
    MejorSueldo = 0.0
    for Codigo in Empleados:
        Vhora = Empleados[Codigo][1]
        Nhoras = Empleados[Codigo][0]
        if Nhoras <= 20:
            Tapagar = Nhoras * Vhora
            Empleados[Codigo] = (Nhoras,Vhora,Tapagar)
            if Tapagar > MejorSueldo:
                MejorSueldo = Tapagar
                
        else: 
            if Nhoras > 20 and Nhoras <= 40:
                Tapagar = (20 * Vhora) + (Nhoras - 20) * (2 * Vhora)
                Empleados[Codigo] = (Nhoras,Vhora,Tapagar)
                if Tapagar > MejorSueldo:
                    MejorSueldo = Tapagar
            else:
                Tapagar = (20 * Vhora) + (20 * (2 * Vhora)) + (Nhoras - 40) * (3 * Vhora)
                Empleados[Codigo] = (Nhoras,Vhora,Tapagar)
                if Tapagar > MejorSueldo:
                    MejorSueldo = Tapagar
    return (MejorSueldo)

def imprimir(Empleados):
    print('{:10}{:11}{:12}{:15}'.format('Codigo', 'Horas', 'Valor hora', 'Valor a pagar'))
    for Codigo in Empleados:
        print('{:}{:10}{:15,}{:15,}'.format(Codigo, Empleados[Codigo][0], Empleados[Codigo][1], Empleados[Codigo][2]))
        
#Prueba
Empleados={}
Empleados[111]=(10,10000,0)
Empleados[222]=(22,10000,0)
Empleados[333]=(52,10000,0)

Sueldo = CalculoNomina(Empleados)
imprimir(Empleados)
print('El mejor sueldo es ${:5,}'.format(Sueldo))
