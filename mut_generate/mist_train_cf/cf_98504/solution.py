"""
QUESTION:
Desarrolla una función `calcular_npv` que calcule el valor neto presente de una inversión en Bitcoin a largo plazo, considerando variables como el crecimiento del mercado, volatilidad y riesgo. La función debe recibir como parámetros el monto inicial de inversión, la tasa de crecimiento del mercado, la volatilidad del mercado, el riesgo asociado a la inversión, la tasa de inflación y la tasa de interés, y el período de tiempo en años. La función debe regresar el valor neto presente de la inversión en Bitcoin.
"""

def calcular_npv(monto_inicial, tasa_crecimiento, volatilidad, riesgo, tasa_inflacion, tasa_interes, tiempo):
    npv = 0
    for t in range(1, tiempo+1):
        vi = monto_inicial / (1 + tasa_inflacion)**t
        vf = vi * (1 + tasa_crecimiento)**t * (1 + volatilidad)**t * (1 - riesgo)**t
        cf = (vf - vi) / vi
        npv += cf / (1 + tasa_interes)**t
    return -monto_inicial + npv