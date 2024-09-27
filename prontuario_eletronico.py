class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class PacienteAdulto(Paciente):
    def __init__(self, nome, idade, ocupacao):
        super().__init__(nome, idade)
        self.ocupacao = ocupacao

    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}, Ocupação: {self.ocupacao}"

paciente1 = PacienteAdulto("Pedro Alves", 46, "Professor")
print(paciente1.exibir_informacoes())
