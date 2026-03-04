from utilidades.constantes import TAXA_KM_EXCEDENTE, TAXA_ATRASO_HORA

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
    """Calcula a multa aplicando a taxa por km excedente."""
    return km_excedente * TAXA_KM_EXCEDENTE

def calcular_multa_atraso(horas_atraso):
    """Calcula a multa aplicando a taxa por cada hora de atraso."""
    return horas_atraso * TAXA_ATRASO_HORA