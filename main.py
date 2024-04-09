from class_robo import RoboTrading
from class_robo import TraningRobo
from class_robo import easygui

if __name__ == '__main__':

    attemps = 3
    while attemps > 0:

        # Inicia o programa solicitando o arquivo, somente arquivos .CSV
        file_path = easygui.fileopenbox(default="*.csv", filetypes=["*.csv"])

        if not file_path: # verificação
            print('File not selected, or an invalid file! Olny .CSV !')
            attemps -= 1
            continue

        # Cria objeto para o Robo
        robo = RoboTrading(file_path)

        # Cria o dataframe mostrando o 5 primeiros valoes 
        robo.system_messages('Principal Data')
        robo.creat_dataframe()

        # Abre o grafico de negocioação
        robo.system_messages('Open Candlesitick Viewer')
        robo.candlestick_view()

        # valor inicial
        robo.system_messages('Moutant Today')
        robo.negociation_ambient(input('\nValor inicial: '))
        break
