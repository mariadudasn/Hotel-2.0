from classes import*
import os

def main():
    contID = 0
    hotel = Hotel( "Luxe Palace Hotel","Avenida das Estrelas, 123", "12.345.678/0001-90")

    quartoLuxe = DeluxeQuarto(4, 7000)
    quartoMaster = APMaster(4, 3000)
    quartoSimples = APSimples (4, 1000)
    quartoScasal = APSimplesCasal(4, 1500)
    quartoDuplo = APDuplo (4, 2500)
    quartoDcasal = APDuploCasal (4, 3000)

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---MENU INICIAL---")
            print("01 - CADASTRAR CLIENTE")
            print("02 - DISPONIBILIDADE DE QUARTOS")
            print("03 - RESERVAR QUARTO")
            print("04 - CANCELAR RESERVA")
            print("05 - LISTAR CLIENTES")
            print("06 - LISTAR RESERVAS")
            print("00 - SAIR")
            print("--------")
            print("")

            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("---CADASTRO DE CLIENTE---")
                    print("INFORME OS SEUS DADOS")
                    contID += 1
                    id = contID
                    nome = input("Nome - ")
                    cpf = int(input("CPF - "))
                    tel = int(input("Telefone - "))                    

                    hotel.cadastrarCliente(id, nome, cpf, tel)

                case 2:
                    os.system("cls")
                    print("---DISPONIBILIDADE DE QUARTOS---")
                    print(f"Quantidade de quartos DELUXE: {quartoLuxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos MASTER: {quartoMaster.getQtdQuarto()}")
                    print(f"Quantidade de quartos Simples: {quartoSimples.getQtdQuarto()}")
                    print(f"Quantidade de quartos Simples Casal: {quartoScasal.getQtdQuarto()}")
                    print(f"Quantidade de quartos Duplo: {quartoDuplo.getQtdQuarto()}")
                    print(f"Quantidade de quartos Duplo Casal: {quartoDcasal.getQtdQuarto()}")
                    os.system("pause")

                case 3:
                    os.system("cls")
                    print("---DISPONIBILIDADE DE QUARTOS---")
                    print("---DISPONIBILIDADE DE QUARTOS---")
                    print(f"Quantidade de quartos DELUXE: {quartoLuxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos MASTER: {quartoMaster.getQtdQuarto()}")
                    print(f"Quantidade de quartos Simples: {quartoSimples.getQtdQuarto()}")
                    print(f"Quantidade de quartos Simples Casal: {quartoScasal.getQtdQuarto()}")
                    print(f"Quantidade de quartos Duplo: {quartoDuplo.getQtdQuarto()}")
                    print(f"Quantidade de quartos Duplo Casal: {quartoDcasal.getQtdQuarto()}")
                    print("------")
                    print(" ")
                    print("---QUAL QUARTO DESEJA RESERVAR?---")
                    print("01 - DELUXE")
                    print("02 - MASTER")
                    print("03 - SIMPLES")
                    print("04 - SIMPLES CASAL")
                    print("05 - DUPLO")
                    print("06 - DUPLO CASAL")

            
                case 4:
                    pass

                case 5:
                    os.system("cls")
                    print("---LISTA DE CLIENTES---")
                    hotel.listarClientes()
                    os.system("pause")
                
                case 6:
                    pass

                case 0:
                    print("SAINDO ...")
                    print("------")
                    sair = True

                case _:
                    print("Valor invalido")
                    print("------")
                    

        except Exception :
            print("Valor invalido")
            print(" ")