# Creo una lista con el precio en el que estaba bitcoin el primero de enero de cada año (en las keys) y el precio en el que cierra el 31 de diciembre (en los values)
precio_bitcoin = {
        4.58: 13.24, #2012
        13.24: 731.91, #2013
        731.91: 320.89, #2014 decremento
        320.89: 430.56, #2015
        430.56: 965.94, #2016
        965.94: 13885.99, #2017
        13885.99: 3694.68, #2018 decremento
        3694.68: 7161.73, #2019
        7161.73: 29036.19, #2020
    }
porcentaje_anual = []

# Funcion para calcular la media
def media(X):
    return sum(X) / len(X)

# Funcion con una formula para calcular el incremento porcentual anual del bitcoin
def incremento_porcentual(valor_inicial, valor_final):
    diferencia = float(valor_final - valor_inicial)

    resultado = float((valor_inicial % diferencia) * 100)
    return resultado


def run():
    year = 2012
    for valor_inicial, valor_final in precio_bitcoin.items():
        resultado = incremento_porcentual(valor_inicial, valor_final)
        print(f"El incremento porcentual de bitcoin en el año {year} fue de {resultado}")
        year += 1
        porcentaje_anual.append(resultado)
    media_anual = media(porcentaje_anual)
    print(f"El porcentaje promedio anual de rendimiento es de {media_anual}")


if __name__ == "__main__":
    run()