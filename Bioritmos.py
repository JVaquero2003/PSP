#  El programa debe pedir la fecha de nacimiento y la fecha actual, y debe calcular los
#  biorritmos para cada uno de los tres ciclos. El programa debe mostrar los valores de los
#  biorritmos para cada ciclo, y debe mostrar un diagrama de barras que muestre los valores
#  de los biorritmos para cada ciclo. El diagrama debe mostrar los valores de los biorritmos
#  para cada ciclo en una sola linea.


from datetime import date
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

def bioritmo(fechaNacimiento, fechaActual):
    # Calcula los biorritmos para una fecha dada
    # Devuelve una lista con los valores de los biorritmos para cada ciclo
    # Los valores de los biorritmos son números entre -100 y 100
    # Los valores negativos indican que el ciclo está en fase de baja
    # Los valores positivos indican que el ciclo está en fase de alta
    # Los valores cercanos a cero indican que el ciclo está en fase de equilibrio

    # Calcula los días transcurridos desde la fecha de nacimiento hasta la fecha actual
    diasTranscurridos = (fechaActual - fechaNacimiento).days

    # Calcula los valores de los biorritmos para cada ciclo
    # Los ciclos tienen una duración de 23, 28 y 33 días
    # Los valores de los biorritmos se calculan con una función seno

    # Ciclo fisico
    cicloFisico = 23
    valorFisico = diasTranscurridos % cicloFisico
    valorFisico = 100 * math.sin((2 * math.pi * valorFisico) / cicloFisico)
    
    # Ciclo emocional
    cicloEmocional = 28
    valorEmocional = diasTranscurridos % cicloEmocional
    valorEmocional = 100 * math.sin((2 * math.pi * valorEmocional) / cicloEmocional)

    # Ciclo intelectual
    cicloIntelectual = 33
    valorIntelectual = diasTranscurridos % cicloIntelectual
    valorIntelectual = 100 * math.sin((2 * math.pi * valorIntelectual) / cicloIntelectual)

    # Devuelve los valores de los biorritmos para cada ciclo
    return [valorFisico, valorEmocional, valorIntelectual]

def graficarBioritmos(fechaNacimiento, fechaActual):
    # Calcula los biorritmos para una fecha dada
    # Grafica los valores de los biorritmos para cada ciclo
    # Los valores de los biorritmos son números entre -100 y 100
    # Los valores negativos indican que el ciclo está en fase de baja
    # Los valores positivos indican que el ciclo está en fase de alta
    # Los valores cercanos a cero indican que el ciclo está en fase de equilibrio

    # Calcula los biorritmos para la fecha actual
    valoresActuales = bioritmo(fechaNacimiento, fechaActual)

    # Calcula los biorritmos para 100 días después de la fecha actual
    fechaFinal = fechaActual + timedelta(days=100)
    valoresFuturos = bioritmo(fechaNacimiento, fechaFinal)

    # Calcula los días transcurridos desde la fecha de nacimiento hasta la fecha final
    diasTranscurridos = (fechaFinal - fechaNacimiento).days

    # Crea una
    [...]

    plt.figure(1)

    # Crea
    [...]

    plt.subplot(311)
    plt.title('Biorritmos')
    plt.ylabel('Fisico')
    plt.plot(range(diasTranscurridos), valoresActuales[0], 'b', range(diasTranscurridos), valoresFuturos[0], 'r')
    
    # Crea
    [...]

    plt.subplot(312)
    plt.ylabel('Emocional')
    plt.plot(range(diasTranscurridos), valoresActuales[1], 'b', range(diasTranscurridos), valoresFuturos[1], 'r')

    # Crea
    [...]

    plt.subplot(313)
    plt.ylabel('Intelectual')
    plt.plot(range(diasTranscurridos), valoresActuales[2], 'b', range(diasTranscurridos), valoresFuturos[2], 'r')
    
    # Muestra el gráfico
    plt.show()

def main():
    # Pide la fecha de nacimiento
    fechaNacimiento = input('Fecha de nacimiento (dd/mm/aaaa): ')
    fechaNacimiento = datetime.strptime(fechaNacimiento, '%d/%m/%Y').date()

    # Pide la fecha actual
    fechaActual = input('Fecha actual (dd/mm/aaaa): ')
    fechaActual = datetime.strptime(fechaActual, '%d/%m/%Y').date()

    # Calcula los biorritmos para la fecha actual
    valoresActuales = bioritmo(fechaNacimiento, fechaActual)

    # Calcula los biorritmos para 100 días después de la fecha actual
    fechaFinal = fechaActual + timedelta(days=100)
    valoresFuturos = bioritmo(fechaNacimiento, fechaFinal)

    #
    [...]

    print('Biorritmos para la fecha actual:')
    print('Fisico: %.2f' % valoresActuales[0])
    print('Emocional: %.2f' % valoresActuales[1])
    print('Intelectual: %.2f' % valoresActuales[2])

    #
    [...]

    print('Biorritmos para 100 dias despues:')
    print('Fisico: %.2f' % valoresFuturos[0])
    print('Emocional: %.2f' % valoresFuturos[1])
    print('Intelectual: %.2f' % valoresFuturos[2])

    # Grafica los biorritmos
    graficarBioritmos(fechaNacimiento, fechaActual)

if __name__ == '__main__':
    main()