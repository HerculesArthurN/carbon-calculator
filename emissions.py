def calcular_emissoes(km_por_semana: float, kwh_por_semana: float, refeicoes_carne: int) -> dict:
    """
    Calcula a pegada semanal de carbono com base nos dados fornecidos.
    """
    # Fatores de emissão aproximados
    fator_km = 0.21    # kg CO₂/km
    fator_kwh = 0.5    # kg CO₂/kWh
    fator_carne = 5.0  # kg CO₂/refeição

    emissao_km = km_por_semana * fator_km
    emissao_kwh = kwh_por_semana * fator_kwh
    emissao_carne = refeicoes_carne * fator_carne

    total = emissao_km + emissao_kwh + emissao_carne

    return {
        "transporte": emissao_km,
        "energia": emissao_kwh,
        "alimentacao": emissao_carne,
        "total": total
    }
