class Cliente:
    def __init__(self, nome, data_nasc, cpf, cnh):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.cnh = cnh

    def __repr__(self):
        return f"Cliente(nome='{self.nome}', cpf='{self.cpf}')"
