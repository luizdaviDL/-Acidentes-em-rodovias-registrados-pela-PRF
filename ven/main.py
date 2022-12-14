import flet as ft
import pandas as pd
import matplotlib.pyplot as plt

from flet import Text 
x = pd.read_excel(r"C:\Users\MICRO\Desktop\Trabalho de PROG 1\acidentes2021.xlsx") 

def main(page: ft.Page): 

    """ Contém o código principal da página do flet """

    page.title = "Acidentes em rodovias registrados pela PRF" # cria um título para a página
    titulo = Text(value='Sistema de visualização de dados',  size=40, color=ft.colors.BLACK) # cria um texto na página
    def button_clicked(e):

        """ Guarda a informação que será plotada após o pressionamento do botão """
        output_text.value = option_dropdown.value
        option_dropdown.value = ''
        s = [] # lista vazia
        plt.clf() # limpa o gráfico
        page.update()

        if output_text.value ==  "1 - Quais eram as classificações dos acidentes em sextas-feiras?":
            for v,j in zip(x['dia_semana'],x['classificacao_acidente']):
                if "sexta-feira" in v:
                    s.append(j) # guarda o que está na variável j na lista vazia
            plt.xlabel('Quantidade') # cria uma etiqueta para o eixo x
            plt.ylabel('Classificações dos acidentes') # cria uma etiqueta para o eixo y
            plt.title('Classificações dos acidentes em sextas-feiras') # cria um título para o gráfico

        if output_text.value ==  "2 - Quais eram os climas nos acidentes com tombamento?": 
            for v,j in zip(x['tipo_acidente'],x['condicao_metereologica']):
                if "Tombamento" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Climas nos acidentes')
            plt.title('Climas nos acidentes com tombamento')

        if output_text.value == "3 - Quais eram as classificações dos acidentes que ocorreram em pleno dia?":
            for v,j in zip(x['fase_dia'],x['classificacao_acidente']):
                if "Pleno dia" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')
            plt.title('Classificações dos acidentes que ocorreram em pleno dia')

        if output_text.value == "4 - Quais eram os gêneros dos condutores dos acidentes com vítimas fatais?":
            for v,j in zip(x['classificacao_acidente'],x['sexo']):
                if "Com Vítimas Fatais" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Gêneros')
            plt.title('Gêneros dos condutores dos acidentes com vítimas fatais')

        if output_text.value == "5 - Quais eram os dias da semana em que a causa do acidente foi intoxicação?":
            for v,j in zip(x['causa_acidente'],x['dia_semana']):
                if "Ingestão de álcool e/ou substâncias psicoativas pelo pedestre" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Dias da semana')
            plt.title('Dias da semana onde a causa do acidente foi intoxicação')

        if output_text.value == "6 - Quais eram os tipos de pista onde houve ultrapassagem indevida?":
            for v,j in zip(x['causa_acidente'],x['tipo_pista']):
                if "Ultrapassagem Indevida" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Tipos da pista')
            plt.title('Tipos de pista onde houve ultrapassagem indevida')

        if output_text.value == "7 - Quais eram os sentidos das vias onde houve freio brusco?":
            for v,j in zip(x['causa_acidente'],x['sentido_via']):
                if "Frear bruscamente" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Sentidos das vias')
            plt.title('Sentidos das vias onde houve freio brusco')

        if output_text.value == "8 - Quais eram as fases dos dias onde o condutor estava dormindo?":
            for v,j in zip(x['causa_acidente'],x['fase_dia']):
                if "Condutor Dormindo" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Fases dos dias')
            plt.title('Fases dos dias onde o condutor estava dormindo')

        if output_text.value == "9 - Quais eram as classificações dos acidentes onde houve tombamento?":
            for v,j in zip(x['tipo_acidente'],x['classificacao_acidente']):
                if "Tombamento" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')
            plt.title('Classificações dos acidentes com tombamento')

        if output_text.value == "10 - Quais eram as classificações dos acidentes onde havia problema com o freio?":
            for v,j in zip(x['causa_acidente'],x['classificacao_acidente']):
                if "Problema com o freio" in v:
                    s.append(j)
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')
            plt.title('Classificações dos acidentes onde havia problema com o freio')

        if output_text.value ==  "11 - Quais eram os tipos dos veículos que se acidentaram em via decrescente?":
            for v,j in zip(x['sentido_via'],x['tipo_veiculo']):
                if 'Decrescente' in v:
                    s.append(j)

            plt.title('Tipos dos veículos que se acidentaram em via decrescente')
            plt.ylabel('tipo de veículos', fontsize = 11)
            plt.xlabel('Qtd em vias decrescentes', fontsize = 11)

        if output_text.value == "12 - Quais eram as fases dos dias quando a causa foi reação tardia ou ineficiente?":
            for v,j in zip(x['causa_acidente'],x['fase_dia']):
                if 'Reação tardia ou ineficiente do condutor' in v: 
                    s.append(j) 
                            
            plt.title('Fases dos dias quando a causa foi reação tardia ou ineficiente')
            plt.xlabel('Fases do dia', fontsize = 11)
            plt.ylabel('Reação tardia ou ineficiente do condutor', fontsize = 11) 

        if output_text.value == '13 - Quais eram as condições meteorológicas dos acidentes onde houve uma colisão frontal?':
            for v,j in zip(x['tipo_acidente'],x['condicao_metereologica']):
                if 'Colisão frontal' in v: 
                    s.append(j)

            plt.title('Condições meteorológicas dos acidentes onde houve uma colisão frontal')
            plt.xlabel('Condições meteorológicas', fontsize = 11)
            plt.ylabel('Quantidade', fontsize = 11) 

        if output_text.value ==  '14 - Quais foram as condições dos condutores quando houve tombamento?':    
            for v,j in zip(x['tipo_acidente'],x['estado_fisico']):
                if 'Tombamento' in v: 
                    s.append(j)

            plt.title('Condições dos condutores quando houve tombamento')
            plt.ylabel('Condição dos motoristas', fontsize = 11)
            plt.xlabel('Qtd de tombamento', fontsize = 11) 
        
        if output_text.value == '15 - Quais os dias da semana que mais tiveram condutores dormindo?':
            for v,j in zip(x['causa_acidente'],x['dia_semana']):
                if 'Condutor Dormindo' in v: 
                    s.append(j)

            plt.title('Dias da semana que mais tiveram condutores dormindo')
            plt.ylabel('Dias da semana', fontsize = 11)
            plt.xlabel('Condutores dormindo', fontsize = 11) 
        
        if output_text.value == '16 - Quantos acidentes ocorreram por conta de uma reação tardia ou ineficiente do condutor?':
            for v,j in zip(x['causa_acidente'],x['tipo_acidente']):
                if 'Reação tardia ou ineficiente do condutor' in v: 
                    s.append(j)
            plt.rcParams.update({'figure.autolayout': True})
            page.update() 
            plt.title('Acidentes por conta de reação tardia ou ineficiente do condutor')
            plt.xlabel('Qtd de acidentes', fontsize = 11)
            plt.ylabel('Tipos de acidente', fontsize = 11)
            
        
        if output_text.value ==  '17 - Quais eram os climas nos acidentes com pista escorregadia?':
            for v,j in zip(x['causa_acidente'],x['condicao_metereologica']):
                if 'Pista Escorregadia' in v: 
                    s.append(j)

            plt.title('Climas nos acidentes com pista escorregadia')
            plt.xlabel('Qtd de acidentes', fontsize = 11)
            plt.ylabel('Clima', fontsize = 11) 

        if output_text.value ==  '18 - Quais eram as classificações dos acidentes em Rio de Janeiro?':
            for v,j in zip(x['uf'],x['classificacao_acidente']):
                if 'RJ' in v: 
                    s.append(j)

            plt.title('Classificação dos acidentes no Rio de Janeiro')
            plt.xlabel('Qtd de acidentes', fontsize = 11)
            plt.ylabel('Classificação dos acidentes', fontsize = 11) 

        if output_text.value ==  '19 - Quais eram as fases dos dias onde ocorreu chuva?':
            plt.rcParams.update({'figure.autolayout': True},)
            for v,j in zip(x['condicao_metereologica'],x['fase_dia']):
                if 'Chuva' in v: 
                    s.append(j)

            plt.title('Fases do dia onde ocorreu chuva')
            plt.ylabel('Fases do dia', fontsize = 11)
            plt.xlabel('Chuva', fontsize = 11) 

        if output_text.value ==  '20 - Quais eram as classificações dos acidentes onde ocorreu incêndio?':
            for v,j in zip(x['tipo_acidente'],x['classificacao_acidente']):
                if 'Incêndio' in v: 
                    s.append(j)

            plt.title('Classificações dos acidentes com incêndio')
            plt.ylabel('Classificações', fontsize = 11)
            plt.xlabel('Quantidade de Incêndios', fontsize = 11) 

        if output_text.value ==  "21 - Quais eram as classificações dos acidentes por dirigirem na contramão?":
            for v,j in zip(x['causa_acidente'],x['classificacao_acidente']):
                if "Transitar na contramão" in v:
                    s.append(j)
            plt.title('Classificações dos acidentes por dirigirem na contramão')
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')

        if output_text.value ==  "22- Quais os estados físicos das vitimas onde o condutor acessou a via sem observar a presença de outros veículos?":
            for v,j in zip(x['causa_acidente'],x['estado_fisico']):
                if "Acessar a via sem observar a presença dos outros veículos" in v:
                    s.append(j)
            plt.title('Estados físicos das vítimas dos acidentes em que o condutor acessou a via sem observar por outros veículos')
            plt.xlabel('Quantidade')
            plt.ylabel('Estados físicos')

        if output_text.value ==  "23 - Quais eram as fases dos dias nos acidentes em que o condutor ingeriu bebida alcoolica?":
            for v,j in zip(x['causa_acidente'],x['fase_dia']):
                if "Ingestão de álcool e/ou substâncias psicoativas pelo pedestre" in v:
                    s.append(j)
            plt.title('Fases dos dias nos acidentes em que o condutor ingeriu bebida alcoolica')
            plt.xlabel('Quantidade')
            plt.ylabel('Fases dos dias')
  
        if output_text.value ==  "24 - Quais eram os estados das vitimas por conta do condutor deixar de manter distância do veiculo da frente?":
            for v,j in zip(x['causa_acidente'],x['estado_fisico']):
                if "Condutor deixou de manter distância do veículo da frente" in v:
                    s.append(j)
            plt.title('Estados das vítimas dos acidentes em que o condutor não manteve distância do veículo da frente')
            plt.xlabel('Quantidade')
            plt.ylabel('Estados das vítimas')

        if output_text.value ==  "25 - Quais eram as classificações dos acidentes envolvendo motocicletas?":
            for v,j in zip(x['causa_acidente'],x['classificacao_acidente']):
                if "Trafegar com motocicleta (ou similar) entre as faixas" in v:
                    s.append(j)
            plt.title('Classificações dos acidentes envolvendo motocicletas')
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')

        if output_text.value ==  "26 - Quais eram as classificações dos acidentes ocorridos em dias chuvosos?":
            for v,j in zip(x['causa_acidente'],x['classificacao_acidente']):
                if "Chuva" in v:
                    s.append(j)
            plt.title('Classificações dos acidentes ocorridos em dias chuvosos')
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')

        if output_text.value ==  "27 - Quais eram as classificações dos acidentes em que o condutor estava dormindo?":
            for v,j in zip(x['causa_acidente'],x['classificacao_acidente']):
                if "Condutor Dormindo" in v:
                    s.append(j)
            plt.title('Classificações dos acidentes em que o condutor estava dormindo')
            plt.xlabel('Quantidade')
            plt.ylabel('Classificações dos acidentes')
       
        if output_text.value ==  "28 - Quais eram os estados físicos das vitimas por acidentes causados por conta da pista estar escorregadia?":
            for v,j in zip(x['causa_acidente'],x['estado_fisico']):
                if "Pista Escorregadia" in v:
                    s.append(j)
            plt.title('Estados físicos das vítimas por acidentes causados em pistas escorregadias')
            plt.xlabel('Quantidade')
            plt.ylabel('Estados físicos')
  
        if output_text.value ==  "29 - Quais eram os tipos de pista em que ocorreram acidentes por dirigirem na contramão?":
            for v,j in zip(x['causa_acidente'],x['tipo_pista']):
                if "Transitar na contramão" in v:
                    s.append(j)
            plt.title('Tipos de pista em que ocorreram acidentes por dirigirem na contramão')
            plt.xlabel('Quantidade')
            plt.ylabel('Tipos de pista')
       
        if output_text.value ==  "30 - Quais eram os tipos dos acidentes causados por frenagem brusca?":
            for v,j in zip(x['causa_acidente'],x['tipo_acidente']):
                if "Frear bruscamente" in v:
                    s.append(j)
            plt.title('Tipos de acidentes causados por frenagem brusca')
            plt.xlabel('Quantidade')
            plt.ylabel('Tipos de acidentes')
                    
        plt.hist(s, orientation= 'horizontal', bins = 25) # plota a informação da lista vazia em um gráfico de barras horizontais
        plt.show() # mostra o gráfico

        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Plotar", on_click=button_clicked) # contém as informações do botão, chama a função button_clicked
    option_dropdown = ft.Dropdown( # contém os componentes do dropdown
        width=910, # aumenta a largura do dropdown
        hint_text="Selecione a pergunta para plotar o gráfico", # acrescenta um texto no dropdown
        options=[ # contém as opções do dropdown
            ft.dropdown.Option("1 - Quais eram as classificações dos acidentes em sextas-feiras?"),
            ft.dropdown.Option("2 - Quais eram os climas nos acidentes com tombamento?"),
            ft.dropdown.Option("3 - Quais eram as classificações dos acidentes que ocorreram em pleno dia?"),
            ft.dropdown.Option("4 - Quais eram os gêneros dos condutores dos acidentes com vítimas fatais?"),
            ft.dropdown.Option("5 - Quais eram os dias da semana em que a causa do acidente foi intoxicação?"),
            ft.dropdown.Option("6 - Quais eram os tipos de pista onde houve ultrapassagem indevida?"),
            ft.dropdown.Option("7 - Quais eram os sentidos das vias onde houve freio brusco?"),
            ft.dropdown.Option("8 - Quais eram as fases dos dias onde o condutor estava dormindo?"),
            ft.dropdown.Option("9 - Quais eram as classificações dos acidentes onde houve tombamento?"),
            ft.dropdown.Option("10 - Quais eram as classificações dos acidentes onde havia problema com o freio?"),
            ft.dropdown.Option("11 - Quais eram os tipos dos veículos que se acidentaram em via decrescente?"),
            ft.dropdown.Option("12 - Quais eram as fases dos dias quando a causa foi reação tardia ou ineficiente?"),
            ft.dropdown.Option("13 - Quais eram as condições meteorológicas dos acidentes onde houve uma colisão frontal?"),
            ft.dropdown.Option('14 - Quais foram as condições dos condutores quando houve tombamento?'),
            ft.dropdown.Option('15 - Quais os dias da semana que mais tiveram condutores dormindo?'),
            ft.dropdown.Option('16 - Quantos acidentes ocorreram por conta de uma reação tardia ou ineficiente do condutor?'),
            ft.dropdown.Option('17 - Quais eram os climas nos acidentes com pista escorregadia?'),
            ft.dropdown.Option('18 - Quais eram as classificações dos acidentes em Rio de Janeiro?'),
            ft.dropdown.Option('19 - Quais eram as fases dos dias onde ocorreu chuva?'),
            ft.dropdown.Option('20 - Quais eram as classificações dos acidentes onde ocorreu incêndio?'),
            ft.dropdown.Option("21 - Quais eram as classificações dos acidentes por dirigirem na contramão?"),
            ft.dropdown.Option("22- Quais os estados físicos das vitimas onde o condutor acessou a via sem observar a presença de outros veículos?"),
            ft.dropdown.Option("23 - Quais eram as fases dos dias nos acidentes em que o condutor ingeriu bebida alcoolica?"),
            ft.dropdown.Option("24 - Quais eram os estados das vitimas por conta do condutor deixar de manter distância do veiculo da frente?"),
            ft.dropdown.Option("25 - Quais eram as classificações dos acidentes envolvendo motocicletas?"),
            ft.dropdown.Option("26 - Quais eram as classificações dos acidentes ocorridos em dias chuvosos?"),
            ft.dropdown.Option("27 - Quais eram as classificações dos acidentes em que o condutor estava dormindo?"),
            ft.dropdown.Option("28 - Quais eram os estados físicos das vitimas por acidentes causados por conta da pista estar escorregadia?"),
            ft.dropdown.Option("29 - Quais eram os tipos de pista em que ocorreram acidentes por dirigirem na contramão?"),
            ft.dropdown.Option("30 - Quais eram os tipos dos acidentes causados por frenagem brusca?")
        ],
    )

    page.add(titulo, option_dropdown, submit_btn,output_text) # adiciona o título, o dropdown e o botão na página do flet

ft.app(target=main) # chama a função principal