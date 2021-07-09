# Calculo-salario-semanal
Calcular salario semanal teniendo en cuenta si se hicieron horas extras.

En una empresa se requiere calcular el salario semanal de cada uno de los obreros que
laboran en ella. El salario se obtiene de la siguiente forma:
• Si el obrero trabaja 20 horas o menos se le paga Valor de la hora ganada por hora
• Si trabaja entre de 21 horas y 40 horas se le paga al doble del valor de la hora
pagada por hora y Las primeras 20 horas valor de la hora.
• Si trabaja más de 40 horas se le pagara al triple del valor de la hora pagada por
hora, las primeras 20 horas se pagan a valor la hora, las siguientes 20 horas al
doble del valor de la hora.
Usted se asignó como programador para realizar dos funciones, la primera funcion debe
recibir los códigos de los trabajadores como llave y el valor de la hora a pagar y el número
de horas trabajadas por semana y debe calcular valor a pagar a la semana por trabajador.
Esta función debe retornar el mejor salario del empleado.
La segunda función debe recibir el diccionario cargado, ya con los datos de los empleados
(código trabajador(Key), valor de la hora a trabajar, número de horas trabajadas por
semana y valor total a pagar (Valor calculado según requerimiento) por empleado:
Ejemplo los resultados como se muestra a continuación :
Ejemplo: para tres (3) trabajadores 
• Entrada
Empleados={}
Empleados[111]=(10,10000,0)
Empleados[222]=(22,10000,0)
Empleados[333]=(52,10000,0)
Sueldo = CalculoNomina(Empleado)
imprimir(Empleados)
print('El mejor sueldo es ${:5,}'.format(Sueldo))

• Salida
Codigo  Horas   Valor hora  Valor a pagar
111      10       10,000      100,000
222      22       10,000      240,000
333      52       10,000      960,000
El mejor sueldo es $960,000
