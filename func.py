# Aqu pra criar as funções e chamar como biblioteca no main.py

# função para retornar pro sobre-nos ou terminar
def retornopequeno():
    resposta = input("gostaria de saber algo mais? sim/não \n")
    if resposta == 'sim':
        return
    elif resposta == 'não':
        print(f'Obrigado por entrar em contato conosco!\n'
              f'Volte sempre!')
        exit()

#funcao para receber o dia do agendamento
def dia_por_extenso(numero):
    dias = {
        1: 'Segunda-feira',
        2: 'Terça-feira',
        3: 'Quarta-feira',
        4: 'Quinta-feira',
        5: 'Sexta-feira',
        6: 'Sábado',
        7: 'Domingo'
    }
    return dias[numero]

