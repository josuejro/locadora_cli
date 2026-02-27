def formatar_moeda(valor):
    """
    Recebe um número decimal e devolve um texto formatado como moeda.
    Exemplo: 1250.5 -> R$ 1.250,50
    """
    valor_formatado = f"{valor:,.2f}"
    
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")
    
    return f"R$ {valor_formatado}"

def calcular_multa_km(km_excedente):
    """Calcula a multa aplicando uma taxa fixa de R$ 2,50 por km."""
    taxa_por_km = 2.50
    return km_excedente * taxa_por_km

def calcular_multa_atraso(horas_atraso):
    """Calcula a multa aplicando R$ 30,00 por cada hora de atraso."""
    taxa_por_hora = 30.00
    return horas_atraso * taxa_por_hora