class Contrato:
    def __init__(self, id_contrato, cpf_cliente, placa_carro, data_retirada, data_devolucao_prevista, km_inicial, limite_km, valor_provisorio, seguro_e_extras, status):
        self.id_contrato = id_contrato
        self.cpf_cliente = cpf_cliente
        self.placa_carro = placa_carro
        self.data_retirada = data_retirada
        self.data_devolucao_prevista = data_devolucao_prevista
        self.km_inicial = km_inicial
        self.limite_km = limite_km
        self.valor_provisorio = valor_provisorio
        self.seguro_e_extras = seguro_e_extras
        self.status = status