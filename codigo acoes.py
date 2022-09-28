from collections import deque


class dados_conta:
  def __init__(self):
    self.verificador_elemento = deque()
    self.pilha_reserva = deque()
    self.d = []

  def append_elemento(self,elemento):
      self.verificador_elemento.append(elemento)

  def pop_elemento(self):
      self.verificador_elemento.pop()

  def append_elemento_reserva(self, elemento):
    self.pilha_reserva.append(elemento)

  def pop_elemento_reserva(self):

    self.pilha_reserva.pop()

  def backup(self):
    if self.verificador_elemento[len(self.verificador_elemento)-1] == "C" and len(self.pilha_reserva) == 1:
      self.pop_elemento()
      self.d = []

    elif self.verificador_elemento[len(self.verificador_elemento)-1] == "C":
      self.pop_elemento()
      self.pop_elemento_reserva ()
      self.d = self.pilha_reserva[len(self.pilha_reserva)-1]

    elif self.verificador_elemento[len(self.verificador_elemento)-1] == "V":
      self.pop_elemento()
      self.d = fila.pilha_reserva[len(self.pilha_reserva)-1]
      conta.saldo_reserva.pop()
      conta.saldo = conta.saldo_reserva[len(conta.saldo_reserva)-1]

  def opcoes(self):
    resposta = str(input("BEM VINDO, DIGITE A TRANSAÇÃO QUE QUER REALIZAR.\n"
                         "1 - COMPRAR AÇÃO\n"
                         "2 - VENDER AÇÃO\n"
                         "3 - RETROCEDER AÇÃO\n"
                         "4 - TODAS AS SUAS AÇÕES/VALORES\n"
                         "5 - SAIR DO PROGRAMA\n"))

    if resposta == "1":
      conta.juntar_lista_append()
      fila.append_elemento("C")

    elif resposta == "2":
      if len(self.pilha_reserva) == 0 or len(self.d) == 0:
        print("AÇÃO NEGADA, VOCÊ NAO TEM AÇÕES PARA VENDER.")

      else:
        conta.escolher_operacao()
        fila.append_elemento("V")
        conta.saldo_reserva.append(conta.saldo)

    elif resposta == "3":
      if len(self.pilha_reserva) == 0 or len(self.verificador_elemento) == 0:
        print("AÇÃO NEGADA, NAO A O QUE RETROCEDER.")

      else:
        fila.backup()
        print ("TRANSAÇÃO EFETUADA COM SUCESSO.")
        conta.print_saldo()

    elif resposta == "4":
      self.acoes_valores()

    elif resposta == "5":
      print("OBRIGADO POR UTILIZAR O NOSSO PROGRAMA.")
      exit()

  def tamanho_10(self):
    if len(self.pilha_reserva) == 10:
      self.pilha_reserva.popleft()

    elif len(self.verificador_elemento) == 10:
      self.verificador_elemento.popleft()

  def acoes_valores(self):
    compra_acoes = 0
    valores_acoes = 0
    for x in range(len(self.d)):
      print(f"VOCÊ POSSUI {self.d[x][0]} ACÔES NO VALOR DE {self.d[x][1]:.2f}R$")
      compra_acoes += self.d[x][0]
      valores_acoes += self.d[x][1]

    print(f"NO TOTAL VOCÊ TEM {compra_acoes} AÇÔES NO VALOR TOTAL DE {valores_acoes:.2f}R$ \n"
          f"SEU SALDO ATUAL É {conta.saldo:.2f}R$")


class contas:
  def __init__(self):
    self.saldo = int(0)
    self.saldo_reserva = [0]

  def juntar_lista_append(self):
    try:
      compra, acao1 = input("DIGITE O VALOR E A QUANTIDADE DE AÇOES.").split(); compra = int(compra); acao1 = int(acao1)
      if acao1 <= 0 or compra <= 0:
        print("AÇÃO NEGADA, VALORES NEGATIVOS SAO INVALIDOS.")
      else:
        lista = [compra,acao1]
        fila.d.append(lista)
        fila.pilha_reserva.append(fila.d.copy())
        print ("TRANSAÇÃO EFETUADA COM SUCESSO.")
    except ValueError:
      print("NECESSÁRIO DIGITAR COMPRA E ACÕES.\n"
            "EX:30 50")

  def vender_acao_igual(self,venda,acao2):
    if fila.d[0][1] == acao2:
      valor1 = fila.d[0][0] * fila.d[0][1]
      valor2 = venda * acao2
      self.saldo = valor2 - valor1 + self.saldo
      fila.d.pop()
      self.ganhos (valor2 - valor1)

  def vender_acao_maior(self,venda,acao2):
    valor_acumulado = 0
    for x in range(len(fila.d)):
      if fila.d[0][1] > acao2:
        valor1 = fila.d[0][0] * acao2
        valor2 = venda * acao2
        fila.d[0][1] = fila.d[0][1] - acao2
        self.saldo = valor2 - valor1 + self.saldo

      elif fila.d[0][1] == acao2:
        valor1 = fila.d[0][0] * fila.d[0][1]
        valor2 = venda * acao2
        self.saldo = valor2 - valor1 + self.saldo
        fila.d.pop(0)

      else:
        valor = fila.d[0][1] * venda
        valor = valor - fila.d[0][0] * fila.d[0][1]
        self.saldo += valor
        valor_acumulado += valor
        acao2 = acao2 - fila.d[0][1]
        fila.d.pop(0)

    self.ganhos (valor_acumulado)

  def vender_acao_menor(self,venda,acao2):
    valor1 = fila.d[0][0] * acao2
    valor2 = venda * acao2
    fila.d[0][1] = fila.d[0][1] - acao2
    self.saldo = valor2 - valor1 + self.saldo
    self.ganhos(valor2-valor1)

  def escolher_operacao(self):
    try:
      venda, acao2 = str(input("DIGITE O VALOR E A QUANTIDADE DE AÇOES.")).split(); venda = int(venda); acao2 = int(acao2)
      if fila.d[0][1] > acao2:
        self.vender_acao_maior(venda,acao2)
        self.print_saldo()

      elif fila.d[0][1] == acao2:
        self.vender_acao_igual(venda,acao2)
        self.print_saldo ()

      elif fila.d[0][1] < acao2:
        soma = 0
        for x in range(len(fila.d)):
          soma += fila.d[x][1]
        if soma < acao2:
          print("AÇÃO NEGADA, VALOR DE AÇÕES MAIOR DO QUE O DISPONIVEL.")

        elif venda <= 0 or acao2 <= 0:
          print ("AÇÃO NEGADA, VALORES NEGATIVOS SAO INVALIDOS.")

        elif soma >= acao2:
          self.vender_acao_maior(venda,acao2)
          self.print_saldo()
    except ValueError:
      print("NECESSÁRIO DIGITAR VENDA E AÇÔES.\n"
            "EX:30 50")


  def print_saldo(self):
    if self.saldo > 0:
      print(f"SEU SALDO É DE {self.saldo:.2f}R$ PARABÉNS VOCÊ ESTÁ GANHANDO DINHEIRO. ")

    elif self.saldo == 0:
      print(f"SEU SALDO É DE {self.saldo:.2f}R$ POXA, AINDA NAO GANHOU NADA?")

    elif self.saldo < 0:
      print(f"SEU SALDO É DE {self.saldo:.2f}R$ VOCÊ ESTÁ PERDENDO, BORA MELHORAR NÉ.")

  def ganhos(self,valor):
    if valor > 0:
      print(f"NESSA TRANSAÇÃO VOCÊ OBTEVE UM LUCRO DE {valor:.2f}R$")

    elif valor == 0:
      print (f"NESSA TRANSAÇÃO VOCÊ NAO GANHOU NADA.")

    elif valor < 0:
      print(f"NESSA TRANSAÇÃO VOCE PERDEU UM TOTAL DE {valor:.2f}R$")

fila = dados_conta()
conta = contas()
while True:
  fila.opcoes()
  fila.tamanho_10()
