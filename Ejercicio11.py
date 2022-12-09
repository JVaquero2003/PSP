# Tenemos la siguiente tabla multidimensional, la cual almacena por cada una de sus filas el salario trimestral de
# cada uno de los empleados de la empresa.

# int salarios[][] = { {700, 900, 1300} , {1000, 950, 1080}, {1300, 930, 1200} }

#   A su vez, disponemos también de una tabla empleados, con los nombres de los trabajadores:

# String empleados[] = {Javier María, Antonio Muñoz, Isabel Allende}

#   Implementa un programa Python que muestre por pantalla lo siguiente:
#   Javier Marías -> 700 + 900 + 1300 = 2900€
#   Antonio Muñoz -> 1000 + 950 + 1080 = 3030€
#   Isabel Allende -> 1300 + 930 + 1200 = 3430€

salarios = [[700, 900, 1300], [1000, 950, 1080], [1300, 930, 1200]]
empleados = ["Javier María", "Antonio Muñoz", "Isabel Allende"]


def empleadosYsalarios(salarios, empleados):
    x = 0
    contador = 0
    for i in salarios:
        x = 0
        for j in i:
            x += j
        print(f"{empleados[contador]} -> {i[0]} + {i[1]} + {i[2]} = {x}")
        contador += 1


print(empleadosYsalarios(salarios, empleados))
