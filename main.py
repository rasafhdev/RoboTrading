from class_robo import Robozin
from class_robo import AnaliseDados
import easygui
import pandas as pd


if __name__ == '__main__':
    # Inicia-se com solicitando o usuário carregar o arquivo e cria um dataframe
    local_path = easygui.fileopenbox(default="*.csv", filetypes=["*.csv"])
    df = pd.read_csv(local_path)

    # Cria objetos
    analisador = AnaliseDados(local_path, df)
    robo = Robozin(local_path, df)

    # Fase de Analise
    analisador.mostra_dataset()
    # analisador.mostra_candlestisck()

    # Fase do Robo
    robo.config_qlearning()
    robo.ambiente_negociacao()
    robo.treina_robo()