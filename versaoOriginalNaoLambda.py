# Um jogo da velha criado para atender aos parâmetros Lambda, comentado com explicações do código e especificação dos setores 'l' usados no código de uma linha.
# O arquivo "Jogo1Linha" apresenta este mesmo código convertido ao Lambda em apenas 1 linha
 
# Nome do projeto: Jogo da velha - Versão original
# Linguagem: Python
# Utilizações: Listas, Vetores, Repetições
# Autor: Rafael Lua - rafaellua13
 
 
 
 
# Vetor com valores utilizados durante o código
    
     # vetor[0] a vetor[8] -> Tabuleiro
     # vetor[9] a vetor[17] -> Espaço após a casa do tabuleiro (quebra a linha)
     # vetor[18] -> todas as condições de parada do jogo
     # vetor[19] -> Variável que permitirá a repetição. Se estiver 0, uma das condições do vetor[18] foi cumprida e o jogo será finalizado.
     # vetor[20] -> Vetor que garante a Repetição estilo while, adicionando um 0 cada vez que for necessário
     # vetor[21] -> Um famoso 'cont', armazena o número da rodada
 
 
vetor = [1,2,3,4,5,6,7,8,9," "," ","\n"," "," ","\n"," "," ","\n",[0],1,[0],0]
 
 
# Mostrar o tabuleiro inicial
# Setor 'ln'
for x in range(0,9):
 print("{}{}".format(vetor[x],vetor[x+9]), end = "")
 
# Repetição estilo while, irá repetir enquanto existir um elemento no vetor[20]
# Setor 'lm'  
for number in vetor[20]:
 
 
 # Finalizar vetor caso alguma das condições do vetor[18] seja válida
 # Setor 'll'
 if any(vetor[18])==True:
   vetor.insert(19,0)  # Uma formação diferenciada para alterar valores de um vetor
   vetor.pop(20)       # Insert e Pop  são formas suportadas por lambda, por isso sua utilização
  
   vetor[20].clear()
 
 # Setor 'lk'
 if vetor[19] == 1:     # Se for possível repetir
   vetor[20].append(0)  # Garantir a continuidade do for adicionando um elemento em vetor[20]
 
 
 
   # Atualizando as novas condições do vetor[18] toda rodada, de forma a verificar se alguma delas se torna válida
   (vetor.insert(18,[vetor[0] == vetor[1] == vetor[2],vetor[3] == vetor[4] == vetor[5],vetor[6] == vetor[7] == vetor[8],vetor[0] == vetor[3] == vetor[6],vetor[1] == vetor[4] == vetor[7],vetor[2] == vetor[5] == vetor[8],vetor[0] == vetor[4] == vetor[8],vetor[2] == vetor[4] == vetor[6],vetor[len(vetor)-1] == 9]))
 
   (vetor.pop(19)) # Novamente, a forma de atualização somente com insert e pop
 
   vetor.append(vetor[len(vetor)-1]+1) # Alterar o número da rodada utilizando append e pop
   vetor.pop(len(vetor)-2)             
  
  
  
   # Setor 'lj'
   if any(vetor[18]) == False: # Se as condições de parada do jogo não foram cumpridas
 
    
     # Setor 'li'
     num = ['1','2','3','4','5','6','7','8','9'] # Possibilidades que o jogador pode digitar
    
     # Setor 'lh'
     var = input("\n\nDigite Posição: ")
    
     if var not in num: # Verificar se o valor digitado se encontra nas possibilidades oferecidas
 
       print("\nNão existe xD")
       vetor.append(vetor[len(vetor)-1]-1)
       vetor.pop(len(vetor)-2)
      
    
     else:
      
       # Setor 'lg'
       var = int(var)-1
 
       if vetor[var]>9: # Se a posição já estiver preenchida com 10 ou 100, estará ocupada
         print("\nJa ocupado :)")
         vetor.append(vetor[len(vetor)-1]-1)
         vetor.pop(len(vetor)-2)
 
       else:
        
         # Setor 'lf'
         if vetor[len(vetor)-1]%2 == 0: # Identificar o jogador com base na rodada, adicionar 100 ou 10 dependendo da rodada ser par ou impar
           vetor.insert(var,100)
           vetor.remove(var+1)
          
         else:
           vetor.insert(var,10)
           vetor.remove(var+1)
 
 
     # Setor 'le'
     print()
     for x in range(0,9): # Repetir 9 vezes e mostrar a marca correspondente aos valores adicionados por cada jogador
 
      # Setor 'ld'
      
       # Setor 'lc'
       if vetor[x] == 100:
         marca = "O"
       elif vetor[x] == 10:
         marca="X"
       else:
         marca = vetor[x]
 
       print("{}{}".format(marca,vetor[x+9]), end = "")
 

 else:
 
       # Setor 'lb'
       vetor[18].pop(len(vetor[18])-1)
      
 
       # Setor 'la'
 
       # Mostrar o fim do jogo. Velha ou Fim
       if any(vetor[18]) == False and vetor[len(vetor)-1] == 10:
         print("\nVelha x_x\n\n")
       else:
         print("\nFim :D\n\n")
  
 

