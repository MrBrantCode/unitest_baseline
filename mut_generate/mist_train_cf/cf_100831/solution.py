"""
QUESTION:
Crea una función llamada `calcular_npv` que calcule el valor neto presente de una inversión en Bitcoin a largo plazo. La función debe recibir como parámetros el monto inicial de inversión, la tasa de crecimiento del mercado, la volatilidad del mercado, el riesgo asociado a la inversión, la tasa de inflación y la tasa de interés, y el periodo de tiempo en años. La función debe devolver el valor neto presente de la inversión.
"""

def calcular_npv(monto_inicial, tasa_crecimiento, volatilidad, riesgo, tasa_inflacion, tasa_interes, tiempo):
    npv = 0
    for t in range(1, tiempo+1):
        vi = monto_inicial / (1 + tasa_inflacion)**t
        vf = vi * (1 + tasa_crecimiento)**t * (1 + volatilidad)**t * (1 - riesgo)**t
        cf = (vf - vi) / vi
        npv += cf / (1 + tasa_interes)**t
    return -monto_inicial + npv