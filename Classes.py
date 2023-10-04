class Hotel:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}
        self.reserva = {}

    def getClientes(self):
        return self.cliente

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel        
        self.cliente[self.id] = [self.nome, self.cpf, self.tel]

    def listarClientes(self):
        for chave,valor in self.cliente.items():
            print(f"ID:{chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")

    def reservarQuarto(self, id, reservar):
        self.id = id
        self.reservar = reservar

        match self.reserva:
            case 1:
                x = "Quarto Deluxe"
            case 2:
                x = "Quarto Master"
            case 3:
                x = "Quarto Simples"
            case 4:
                x = "Quarto Simples Casal"
            case 5:
                x = "Quarto Duplo"
            case 6:
                x = "Quarto Duplo Casal"
            case _:
                x = "Opção inválida"

        self.reserva[self.id] = x

    def listarReservas(self):
        for chave,valor in self.cliente.items():
            print(f"ID:{chave} - Quarto: {valor[0]}")




class Quarto:
    def __init__(self, qtd, valor):
        self.qtd = qtd
        self.valor = valor
        
    def getQtdQuarto(self):
        return self.qtd
    
    def setReservaQuarto(self, qtd):
        self.qtd = qtd
    
    def descricao(self):
        pass
    
class DeluxeQuarto(Quarto):
    def descricao(self):
        print ("AP Luxo \n \nDescrição: \n- Espaçoso e Acolhedor; \n- Cama de Qualidade Superior; \n- Área de Estar; \n-Varanda Privativa; \n-Decoração Sofisticada \n-Tecnologia Avançada; \n Serviço de Quarto 24 Horas. \n \nPreço da diária: R$7000,00")

class APMaster(Quarto):
    def descricao(self):
        print("AP MASTER \n \nDescrição: \n- Espaço Amplo; \n- Área de Estar;  \n- Decoração Elegante; \n- Cama Luxuosa; \n- Banheiro Privativo; \n- Comodidades de luxo; \n- Vista Privilegiada; \n- Serviço Personalizado. \n \nPreço da diária: R$3000,00.")

class APSimples(Quarto):
    def descricao(self):
        print ("AP Simples \n \nDescrição: \n- Espaço confortável; \n- Cama de solteiro \n- Mesa de trabalho \n-Banheiro privativo \n-Televisão \n-Serviço de limpeza diário. \n \nPreço da diária: R$1000,00")
        
class APSimplesCasal(Quarto):
    def descricao(self):
        print ("AP Simples Casal \n \nDescrição: \n- Espaço confortável; \n- Cama King \n- Mesa de trabalho \n-Banheiro privativo \n-Televisão \n-Serviço de limpeza diário. \n \nPreço da diária: R$1500,00")

class APDuplo(Quarto):
    def descricao(self):
        print("AP Duplo \n \nDescrição: \n- Camas Confortáveis; \n- Área de Estar;  \n- Banheiro Privativo; \n- Ar Condicionado ou Aquecimento; \n- TV e Wi-Fi; \n- Serviço de Quarto; \n- Vista. \n \nPreço da diária: R$2500,00.")

class APDuploCasal(Quarto):
    def descricao(self):
        print("AP Duplo Casal \n \nDescrição: \n- Espaço Amplo; \n- Área de Estar;  \n- Decoração Elegante; \n- Cama Luxuosa; \n- Banheiro Privativo; \n- Comodidades de luxo; \n- Vista Privilegiada; \n- Serviço Personalizado. \n \nPreço da diária: R$3000,00.")

  