import re

def validar_cpf(cpf):
    """Valida se o CPF tem exatamente 11 dígitos numéricos."""
    return bool(re.match(r'^\d{11}$', cpf))

def validar_cnh(cnh):
    """Valida se a CNH tem exatamente 11 dígitos numéricos."""
    return bool(re.match(r'^\d{11}$', cnh))
