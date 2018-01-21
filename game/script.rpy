 ######################################################
# Titulo: Exemplo de Escolhas com tempo limite (ATL)   #
# Autor: theking17                                     #
# Data: 21/01/2018                                     #
#                                                      #
 ######################################################

init python:
     #Definição de variavel global
     info = ""

     #Definição de uma função para atualizar variavel global
     def update_with_time_exceed(trans, st, at):
          global info
          info = "Tempo Esgotado"
          renpy.jump("good_ending")  

   #Definição de uma função para verificar se o tempo da animação expirou
   #Caso não tenha expirado, a variavel é preenchida conforme a opção escolhida
     def check_time(number):
          global info
          if(info != "Acabou o tempo"):
             if(number == 1):   
               info = "esquerda"
             else:
               info = "direita"
 
     #Importar todas as imagens da pasta Clock (Código do blog da Renpy BR)
     for file in renpy.list_files():
        if file.startswith('Clock/'):
            if file.endswith('.png'):
                name = "Clock " + file.replace('Clock/','').replace('/', ' ').replace('.png','') 
                renpy.image(name, Image(file))
                continue
            continue

define mc = Character('???', color="#4A4A4A")

image bg DarkCave = "Cave1.png"

label start:

    scene bg DarkCave

    mc "\"... Não tem saída.\""
    mc "{color=#aaa}\"A caverna, na qual estive preso pelas ultimas horas, me consome.\""
    mc "{color=#aaa}\"Um labirinto do qual não imaginava que faria parte até a manhã de hoje. Meus sentidos me enganam e vejo apenas as mesmas bifurcações uma após a outra...\" "
    mc "{color=#aaa}\"Não sei mais o que fazer, estou sinceramente no limite de minha consciência. \""
    mc "{color=#aaa}\"Eu... Só queria esquecer tudo e acordar em casa... \""    

    #Inicio da animação por ATL (sintaxe: show <nome_imagem>:)
    show Clock Clock1:
            #Abaixo a sequencia de passos que a animação deve seguir.
            #Notem que não é possível (ao menos nesta versão) utilizar estruturas de repetição dentro deste bloco.            
            "Clock Clock1"
            pause 0.09
            "Clock Clock2"
            pause 0.09
            "Clock Clock3"
            pause 0.09
            "Clock Clock4"
            pause 0.09
            "Clock Clock5"
            pause 0.09
            "Clock Clock6"
            pause 0.09
            "Clock Clock7"
            pause 0.09
            "Clock Clock8"
            pause 0.09
            "Clock Clock9"
            pause 0.09
            "Clock Clock10"
            pause 0.09
            "Clock Clock11"
            pause 0.09
            "Clock Clock12"
            pause 0.09
            "Clock Clock13"
            pause 0.09
            "Clock Clock14"
            pause 0.09
            "Clock Clock15"
            pause 0.09
            "Clock Clock16"
            pause 0.09
            "Clock Clock17"
            pause 0.09
            "Clock Clock18"
            pause 0.09
            "Clock Clock19"
            pause 0.09
            "Clock Clock20"
            pause 0.09
            "Clock Clock21"
            pause 0.09
            "Clock Clock22"
            pause 0.09
            "Clock Clock23"
            pause 0.09
            "Clock Clock24"
            pause 0.09
            "Clock Clock25"
            pause 0.09
            "Clock Clock26"
            pause 0.09
            "Clock Clock27"
            pause 0.09
            "Clock Clock28"
            pause 0.09
            "Clock Clock29"
            pause 0.09
            "Clock Clock30"
            pause 0.09
            "Clock Clock31"
            pause 0.09
            "Clock Clock32"
            pause 0.09
            "Clock Clock33"
            pause 0.09
            "Clock Clock34"
            pause 0.09
            "Clock Clock35"
            pause 0.09
            "Clock Clock36"
            pause 0.09
            "Clock Clock37"
            pause 0.09
            "Clock Clock38"
            pause 0.09
            "Clock Clock39"
            pause 0.09
            "Clock Clock40"
            pause 0.09
            "Clock Clock41"
            pause 0.09
            "Clock Clock42"
            pause 0.09
            "Clock Clock43"
            pause 0.09
            "Clock Clock44"
            pause 0.09
            "Clock Clock45"
            pause 0.09
            "Clock Clock46"
            pause 0.09
            "Clock Clock47"
            pause 0.09
            "Clock Clock48"
            pause 0.09
            "Clock Clock49"
            pause 0.09
            "Clock Clock50"
            pause 0.09
            "Clock Clock51"
            pause 0.09
            "Clock Clock52"
            pause 0.09
            "Clock Clock53"
            pause 0.09
            "Clock Clock54"
            pause 0.09
            "Clock Clock55"
            pause 0.09
            "Clock Clock56"
            pause 0.09
            "Clock Clock57"
            pause 0.09
            "Clock Clock58"
            pause 0.09
            "Clock Clock59"
            pause 0.09
            "Clock Clock60"
            pause 0.09
            "Clock Clock1"
            #Chamada de função para atualizar variavel global
            function update_with_time_exceed   #Função para atualizar variável global
    #Fim da animação

    #Menu de Escolhas 
    menu:
        "Seguir pelo caminho da esquerda.":
            #Verifica se o tempo da animação expirou
            python:
                check_time(1) 
        "Seguir pelo caminho da direita.":
            python:
                check_time(2) 

    pause 1.5 #Delay para esconder o relógio
    hide Clock Clock1 #Esconde o relógio
    $ global info
    if info == "Tempo Esgotado":
        jump bad_ending
    else:
        jump good_ending
   

label bad_ending:
    "" "E assim perdi a consciência. A fome e o cansaço me consumiram nas sombras daquela caverna. "    


label good_ending:    
    mc "{color=#aaa}\"Eu sigo em direção a bifurcação da [info].\" " 
    mc "{color=#aaa}\"E depois de muito tempo caminhando... Percebi...\" "
    mc "{color=#aaa}\"Que finalmente achava uma luz no fim do túnel.\""    





    
