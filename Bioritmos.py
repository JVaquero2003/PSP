from datetime import date
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import math

def calcularBiorritmo(fechaNacimiento, fechaActual):
    dias = (fechaActual - fechaNacimiento).days

    fisico = 100 * math.sin(2 * math.pi * dias / 23)
    emocional = 100 * math.sin(2 * math.pi * dias / 28)
    intelectual = 100 * math.sin(2 * math.pi * dias / 33)

    return [fisico, emocional, intelectual]

def mostrarBiorritmos(biorritmos):
    print("Biorritmos para la fecha actual:")
    print("Fisico: %.2f" % biorritmos[0])
    print("Emocional: %.2f" % biorritmos[1])
    print("Intelectual: %2f" % biorritmos[2])

def mostrarGraficoBiorritmos(biorritmos):
    nombresCiclos = ["Fisico", "Emocional", "Intelectual"]

    colores = ["red", "green", "blue"]

    plt.bar(range(len(biorritmos)), biorritmos, color=colores)

    plt.xticks(range(len(biorritmos)), nombresCiclos)

    plt.show()

def main():

    fechaNacimiento = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")

    fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y").date()

    fechaActual = input("Introduce la fecha actual (dd/mm/aaaa): ")

    fechaActual = datetime.strptime(fechaActual, "%d/%m/%Y").date()

    biorritmos = calcularBiorritmo(fechaNacimiento, fechaActual)

    mostrarBiorritmos(biorritmos)

    mostrarGraficoBiorritmos(biorritmos)

main()