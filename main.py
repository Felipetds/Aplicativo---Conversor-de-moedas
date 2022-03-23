from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):

    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["imagem1"].window = Image(source="logo.png")
        self.root.ids["caixa_1"].window = TextInput()
        self.root.ids["caixa_2"].window = TextInput()
        self.root.ids["caixa_3"].window = TextInput()
        self.root.ids["botao"].window = Button(text='Pesquisar', font_size=14)



    def process_1(self):
        text_1 = self.root.ids.caixa_1.text
        return (text_1)

    def process_2(self):
        text_2 = self.root.ids.caixa_2.text
        return (text_2)

    def process_3(self):
        valor_usuario = self.root.ids.caixa_3.text
        return (valor_usuario)

    def cotacao(self):
        text_1 = self.root.ids.caixa_1.text
        text_2 = self.root.ids.caixa_2.text
        valor_usuario = valor_usuario = self.root.ids.caixa_3.text

        print(text_1)
        print(text_2)
        print(valor_usuario)

        link = f"https://economia.awesomeapi.com.br/last/{str(text_1)}-{str(text_2)}"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()


        a = (str(text_1) + str(text_2))
        dados = dic_requisicao[a]
        print(dic_requisicao)
        print(a)

        bid = dados["bid"]
        bid = float(bid)
        valor_usuario = float(valor_usuario)
        valor_final = valor_usuario * bid
        valor_final = "%.2f" %valor_final
        valor_final = f"Resultado da converção: " + str(valor_final)

        self.root.ids["resultado"].text = f"{valor_final}"

    #def conversao(self):

    #    moeda_1
    #    moeda_2
    #    valor_usuario

    #    valor_final = valor_usuario * moeda_2

    #    self.root.ids["resultado"].text = f"{valor_final}"

MeuAplicativo().run()
