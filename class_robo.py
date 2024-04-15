import plotly.graph_objects as go
import numpy as np
from time import sleep
import random


class AnaliseDados:
    def __init__(self, local_path, df):
        self.localpath = local_path
        self.df = df
        return

    def mostra_dataset(self):
        print(self.df.head())

    # Aqui é usado a biblioteca 'Go', é necessário usar uma variavel que
    # chama a classe Figure, dentro da classe Figure, é necessário colocar os dados "data", que é uma lista de agumentos junto com a classe Candlestick

    def mostra_candlestisck(self):
        figura = go.Figure(
            data= [
                go.Candlestick(
                    x = self.df['Date'],
                    open = self.df['Open'],
                    high = self.df['High'],
                    low  = self.df['Low'],
                    close = self.df['Close']
                )
            ]
        )
        figura.show()

class Robozin(AnaliseDados):
    
    def __init__(self, local_path, df):
        super().__init__(local_path, df)

    def config_qlearning(self):
        self.num_epsodios = 1000
        self.alfa = 0.1
        self.gama = 0.99
        self.epsilon = 0.1

    def ambiente_negociacao(self):
        self.precos = self.df['Close'].values
        self.saldo_inicial = 0
        self.acoes = ['Comprar', 'Vender,' 'Manter']
        self.num_acoes_inicial = 0

        while True:
            self.saldo_inicial = input('Digite seu saldo inicial: ')
            try:
                if self.saldo_inicial.isnumeric():
                    self.saldo_inicial = int(self.saldo_inicial)
                    break
            except ValueError:
                print('Valor deve ser numerico! ')
                continue

        # print(self.saldo_inicial)
        # return self.saldo_inicial
    
    def executar_acao(self, estado, acao, saldo, num_acoes, preco):

        if acao == 0:
            if saldo >= preco:
                num_acoes += 1
                saldo -= preco
        
        elif acao == 1:
            if num_acoes > 0:
                num_acoes -= 1
                saldo += preco

        self.lucro = saldo + num_acoes * preco - self.saldo_inicial

        return(saldo, num_acoes, self.lucro)

    def treina_robo(self):
        q_tabela = np.zeros((len(self.precos), len(self.acoes)))
        for _ in range(self.num_epsodios):

        # Define o saldo
            saldo = self.saldo_inicial
    
        # Define o número de ações
            num_acoes = self.num_acoes_inicial

        for i, preco in enumerate(self.precos[:-1]):
            estado = i

        # Escolher a ação usando a política epsilon-greedy
            if np.random.random() < self.epsilon:
                acao = random.choice(range(len(self.acoes)))
            else:
                acao = np.argmax(q_tabela[estado])

        # Executar a ação e obter a recompensa e o próximo estado
            saldo, num_acoes, lucro = self.executar_acao(estado, acao, saldo, num_acoes, preco)
            prox_estado = i + 1

        # Atualizar a tabela Q
            q_tabela[estado][acao] += self.alfa * (lucro + self.gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

