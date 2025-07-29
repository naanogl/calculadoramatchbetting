def calcular_dinero_real(importe, cuota_a_favor, cuota_exchange, comision):
    mejor_lay = 0
    mejor_diferencia = float('inf')
    mejor_ganancia_casa = 0
    mejor_ganancia_exchange = 0

    for lay in [x / 100 for x in range(1, int(importe * 200) + 1)]:
        ganancia_casa = importe * (cuota_a_favor - 1) - lay * (cuota_exchange - 1)
        ganancia_exchange = lay * (1 - comision) - importe
        diferencia = abs(ganancia_casa - ganancia_exchange)

        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_lay = lay
            mejor_ganancia_casa = ganancia_casa
            mejor_ganancia_exchange = ganancia_exchange

    riesgo = mejor_lay * (cuota_exchange - 1)
    beneficio_promedio = (mejor_ganancia_casa + mejor_ganancia_exchange) / 2
    porcentaje_valor = 100 + (beneficio_promedio / importe) * 100

    if porcentaje_valor >= 98:
        clasificacion = "🟢 Excelente"
    elif porcentaje_valor >= 95:
        clasificacion = "🟢 Muy Bueno"
    elif porcentaje_valor >= 90:
        clasificacion = "🟠 Regular (Busca cuotas mas bajas y mas parejas)"
    else:
        clasificacion = "🔴 Malo (Busca cuotas mas bajas y mas parejas)"

    return {
        "tipo": "real",
        "importe": importe,
        "cuota_a_favor": cuota_a_favor,
        "cuota_exchange": cuota_exchange,
        "comision": comision,
        "lay": mejor_lay,
        "riesgo": riesgo,
        "ganancia_casa": mejor_ganancia_casa,
        "ganancia_exchange": mejor_ganancia_exchange,
        "diferencia": mejor_diferencia,
        "porcentaje_valor": porcentaje_valor,
        "clasificacion": clasificacion
    }


def calcular_freebet(importe, cuota_a_favor, cuota_exchange, comision):
    mejor_lay = 0
    mejor_diferencia = float('inf')
    mejor_ganancia_casa = 0
    mejor_ganancia_exchange = 0

    for lay in [x / 100 for x in range(1, int(importe * 200) + 1)]:
        ganancia_casa = (cuota_a_favor - 1) * importe - lay * (cuota_exchange - 1)
        ganancia_exchange = lay * (1 - comision)
        diferencia = abs(ganancia_casa - ganancia_exchange)

        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_lay = lay
            mejor_ganancia_casa = ganancia_casa
            mejor_ganancia_exchange = ganancia_exchange

    riesgo = mejor_lay * (cuota_exchange - 1)
    beneficio_promedio = (mejor_ganancia_casa + mejor_ganancia_exchange) / 2
    porcentaje_valor = (beneficio_promedio / importe) * 100

    if porcentaje_valor >= 75:
        clasificacion = "🟢 Excelente"
    elif porcentaje_valor >= 70:
        clasificacion = "🟢 Muy Bueno"
    elif porcentaje_valor >= 65:
        clasificacion = "🟠 Regular (Busca cuotas mas altas y mas parejas)"
    else:
        clasificacion = "🔴 Malo (Busca cuotas mas altas y mas parejas)"

    return {
        "tipo": "freebet",
        "importe": importe,
        "cuota_a_favor": cuota_a_favor,
        "cuota_exchange": cuota_exchange,
        "comision": comision,
        "lay": mejor_lay,
        "riesgo": riesgo,
        "ganancia_casa": mejor_ganancia_casa,
        "ganancia_exchange": mejor_ganancia_exchange,
        "diferencia": mejor_diferencia,
        "porcentaje_valor": porcentaje_valor,
        "clasificacion": clasificacion
    }


def calcular_reembolso(importe, cuota_a_favor, cuota_exchange, comision, cantidad_reembolso, porcentaje_uso_freebet=0.75):
    mejor_lay = 0
    mejor_diferencia = float('inf')
    mejor_ganancia_casa = 0
    mejor_ganancia_exchange = 0

    valor_freebet = cantidad_reembolso * porcentaje_uso_freebet

    for lay in [x / 100 for x in range(1, int(importe * 200) + 1)]:
        riesgo = lay * (cuota_exchange - 1)
        ganancia_casa = (cuota_a_favor - 1) * importe - riesgo
        ganancia_exchange = lay * (1 - comision) + valor_freebet - importe
        diferencia = abs(ganancia_casa - ganancia_exchange)

        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_lay = lay
            mejor_ganancia_casa = ganancia_casa
            mejor_ganancia_exchange = ganancia_exchange

    riesgo_final = mejor_lay * (cuota_exchange - 1)
    beneficio_promedio = (mejor_ganancia_casa + mejor_ganancia_exchange) / 2
    porcentaje_valor = (100 + (beneficio_promedio / importe) * 100) - 100

    if porcentaje_valor >= 50:
        clasificacion = "🟢 Excelente"
    elif porcentaje_valor >= 45:
        clasificacion = "🟢 Muy Bueno"
    elif porcentaje_valor >= 40:
        clasificacion = "🟠 Regular (Busca cuotas mas altas y mas parejas)"
    else:
        clasificacion = "🔴 Malo (Busca cuotas mas altas y mas parejas)"

    return {
        "tipo": "reembolso",
        "importe": importe,
        "cuota_a_favor": cuota_a_favor,
        "cuota_exchange": cuota_exchange,
        "comision": comision,
        "cantidad_reembolso": cantidad_reembolso,
        "porcentaje_uso_freebet": porcentaje_uso_freebet,
        "lay": mejor_lay,
        "riesgo": riesgo_final,
        "ganancia_casa": mejor_ganancia_casa,
        "ganancia_exchange": mejor_ganancia_exchange,
        "diferencia": mejor_diferencia,
        "porcentaje_valor": porcentaje_valor,
        "clasificacion": clasificacion
    }


def calcular_rollover(importe, bono, porcentaje_retencion, rollover, cuota_a_favor, cuota_exchange, comision):
    mejor_lay = 0
    mejor_diferencia = float('inf')
    mejor_ganancia_casa = 0
    mejor_ganancia_exchange = 0

    beneficio_apuesta = importe * (cuota_a_favor - 1)
    beneficio_rollover = rollover * (porcentaje_retencion / 100)
    beneficio_casa_base = beneficio_apuesta + beneficio_rollover

    # Aquí aumentamos el rango máximo porque se puede apostar lay sobre importe + rollover
    max_lay = int((importe + rollover) * 300)

    for lay in [x / 100 for x in range(1, max_lay + 1)]:
        riesgo = lay * (cuota_exchange - 1)

        ganancia_casa = beneficio_casa_base - riesgo
        ganancia_exchange = lay * (1 - comision) - importe
        diferencia = abs(ganancia_casa - ganancia_exchange)

        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_lay = lay
            mejor_ganancia_casa = ganancia_casa
            mejor_ganancia_exchange = ganancia_exchange

    riesgo = mejor_lay * (cuota_exchange - 1)
    beneficio_promedio = (mejor_ganancia_casa + mejor_ganancia_exchange) / 2
    porcentaje_valor = 100 + (beneficio_promedio / importe) * 100

    if porcentaje_valor >= 98:
        clasificacion = "🟢 Excelente"
    elif porcentaje_valor >= 95:
        clasificacion = "🟢 Muy Bueno"
    elif porcentaje_valor >= 90:
        clasificacion = "🟠 Regular"
    else:
        clasificacion = "🔴 Malo"

    return {
        "tipo": "rollover",
        "importe": importe,
        "bono": bono,
        "rollover": rollover,
        "porcentaje_retencion": porcentaje_retencion,
        "cuota_a_favor": cuota_a_favor,
        "cuota_exchange": cuota_exchange,
        "comision": comision,
        "lay": mejor_lay,
        "riesgo": riesgo,
        "ganancia_casa": mejor_ganancia_casa,
        "ganancia_exchange": mejor_ganancia_exchange,
        "diferencia": mejor_diferencia,
        "porcentaje_valor": porcentaje_valor,
        "clasificacion": clasificacion
    }




def mostrar_resultados(r):
    print(f"\n=== Resultados para apuesta tipo '{r['tipo']}' ===")
    print(f"A favor (Back): {r['importe']:.2f} € a cuota {r['cuota_a_favor']}")
    print(f"En contra (Lay): {r['lay']:.2f} € a cuota {r['cuota_exchange']} (riesgo: {r['riesgo']:.2f} €)\n")
    print("Casa de apuestas\tExchange\tTotal")

    if r['tipo'] == "real":
        print(f"Si ganas en la Casa de apuestas\t{r['importe']*(r['cuota_a_favor'] -1):.2f}€\t\t{-r['riesgo']:.2f}€"
              f"\t\t{r['ganancia_casa']:.2f}€")
        print(f"Si ganas en el Exchange\t\t{-r['importe']:.2f}€\t\t{r['lay']*(1 - r['comision']):.2f}€"
              f"\t\t{r['ganancia_exchange']:.2f}€")
    elif r['tipo'] == "freebet":
        print(f"Si ganas en la Casa de apuestas\t{(r['cuota_a_favor'] -1)*r['importe']:.2f}€\t\t{-r['riesgo']:.2f}€"
              f"\t\t{r['ganancia_casa']:.2f}€")
        print(f"Si ganas en el Exchange\t\t0.00€\t\t\t{r['lay']*(1 - r['comision']):.2f}€"
              f"\t\t{r['ganancia_exchange']:.2f}€")
    elif r['tipo'] == "reembolso":
        valor_freebet = r['cantidad_reembolso'] * r['porcentaje_uso_freebet']
        print(f"Si ganas en la Casa de apuestas\t{r['importe']*(r['cuota_a_favor'] -1):.2f}€\t\t{-r['riesgo']:.2f}€"
              f"\t\t{r['ganancia_casa']:.2f}€")
        print(f"Si ganas en el Exchange\t\t{-r['importe']:.2f}€\t\t{r['lay']*(1 - r['comision']):.2f}€ + freebet "
              f"({valor_freebet:.2f}€)\t{r['ganancia_exchange']:.2f}€")
    elif r['tipo'] == "rollover":
        print(f"Si ganas en la Casa de apuestas\t{r['ganancia_casa']:.2f}€\t\t{-r['riesgo']:.2f}€"
              f"\t\t{r['ganancia_casa'] - r['riesgo']:.2f}€")
        print(f"Si ganas en el Exchange\t\t{-r['importe']:.2f}€\t\t{r['ganancia_exchange'] + r['importe']:.2f}€"
              f"\t\t{r['ganancia_exchange']:.2f}€")

    print(f"\n📊 Diferencia entre escenarios: {r['diferencia']:.4f} €")
    print(f"📈 Porcentaje de valor del cruce: {r['porcentaje_valor']:.2f} %")
    print(f"🔍 Evaluación del cruce: {r['clasificacion']}")
    

# EJEMPLO DE USO:

#res = calcular_dinero_real(10, 1.55, 1.6, 0.02)
#mostrar_resultados(res)

#res = calcular_freebet(10, 7.5, 8.2, 0.02)
#mostrar_resultados(res)

res = calcular_reembolso(10, 7.5, 8.2, 0.02, cantidad_reembolso=10, porcentaje_uso_freebet=0.7)
mostrar_resultados(res)

#res = calcular_rollover(100, 100, 95, 600, 3.5, 3.9, 0.02)
#mostrar_resultados(res)
