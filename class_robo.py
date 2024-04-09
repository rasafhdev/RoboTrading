import pandas as pd
import plotly.graph_objects as go
import easygui
import os
import numpy as np
from time import sleep
import random


class RoboTrading:
    def __init__(self, file_path):
        self.file_path = file_path


    def system_messages(self, message):
        self.message = message
        sleep(3)
        if not os.name == 'nt':
            os.system('clear')
        else:
            os.system('cls')
        return print(f'Runing module ---> {message}')

    def creat_dataframe(self):
        self.df = pd.read_csv(self.file_path)
        print(self.df.head())
    
    def candlestick_view(self):
        self.price = self.df['Close'].values
        fig = go.Figure(
            # O Parametro data candlestick é uma lista
            data= [
                go.Candlestick(
                    x = self.df['Date'],
                    open = self.df['Open'],
                    high = self.df['High'],
                    low = self.df['Low'],
                    close = self.df['Close'],
                )
            ],
        )
        fig.show()

    def q_learning_configure(self):
        print('\nQ-Learning hyperparameters have been configured.')
        self.episodes_num = 1000
        self.alfa = 0.1
        self.gama = 0.00
        self.epsilon = 0.1

    def negociation_ambient(self, initial_balance):
        self.initial_balance = initial_balance

        while not self.initial_balance.isnumeric():
            print('Não é numero')
            self.initial_balance = input('Valor inicial: ')
            continue

        self.stocks = ['Buy', 'Sell', 'Keep']
        self.quantity_initial_sotcks = 0

    def exec_stock(self, state, stock, balance, num_stocks, price):

        # Ação comprar
        if stock == 0:
            if balance >= price:
                num_stocks += 1
                balance -= price

        # Ação vender
        elif stock == 1:
            if num_stocks > 0:
                num_stocks -= 1
                balance += price

        self.profit = balance + num_stocks * price - self.initial_balance

        return (balance, num_stocks, self.profit)

class TraningRobo(RoboTrading):
    def __init__(self, file_path):
        super().__init__(file_path)

    def exec_training(self):
        print('Initializing Table Q...')
        self.table_q = np.zeros(len(self.price), len(self.stocks))

        print('Initializing Training')
        for _ in range(self.episodes_num):
            
            self.balance = self.initial_balance
            num_stocks = self.quantity_initial_sotcks
            
            for i, price in enumerate(self.price[:-1]):

                state = i

                if np.random() < self.epsilon:
                    stock = random.choice(len(self.stocks))
                else:
                    stock = np.argmax(self.table_q[self.state])
                
                self.balance, num_stocks, self.profit = self.exec_stock(state, stock, num_stocks, price)
