# Um jogo da velha funcional, não focado na otimização, mas sim em escrever o código inteiro em uma única linha (sem usar o comando 'exec()')
 
# Nome do projeto: Jogo da Velha em uma(1) linha - Python (sem exec)
# Linguagem: Python
# Utilizações: Listas, Vetores, Repetições, Lambda
# Autor: Rafael Lua - rafaellua13
 
 
(lambda vetor: [(lambda ln: [print("{}{}".format(vetor[x],vetor[x+9]), end = "") for x in range(0,9)])(0),(lambda lm: [ [(lambda ll:  [vetor.insert(19,0), vetor.pop(20),vetor[20].clear()] if any(ll)==True else None)(vetor[18]),(lambda lk: [vetor[20].append(0),(vetor.insert(18,[vetor[0] == vetor[1] == vetor[2],vetor[3] == vetor[4] == vetor[5],vetor[6] == vetor[7] == vetor[8],vetor[0] == vetor[3] == vetor[6],vetor[1] == vetor[4] == vetor[7],vetor[2] == vetor[5] == vetor[8],vetor[0] == vetor[4] == vetor[8],vetor[2] == vetor[4] == vetor[6],vetor[len(vetor)-1] == 9])),(vetor.pop(19)),vetor.append(vetor[len(vetor)-1]+1),vetor.pop(len(vetor)-2),(lambda lj: [(lambda lh,li: [print("\nNão existe xD"),vetor.append(vetor[len(vetor)-1]-1),vetor.pop(len(vetor)-2)] if lh not in li else  (lambda lg: [print("\nJa ocupado :)"),vetor.append(vetor[len(vetor)-1]-1),vetor.pop(len(vetor)-2)] if vetor[lg] > 9 else (lambda lf: [vetor.insert(lf,100),vetor.remove(lf+1)] if vetor[len(vetor)-1]%2 == 0 else [vetor.insert(lf,10),vetor.remove(lf+1)])(lg))(int(lh)-1))(input("\n\nDigite Posição: "),['1','2','3','4','5','6','7','8','9']),(lambda le: [(lambda ld: print("{}{}".format(ld,vetor[x+9]), end = ""))((lambda lc: "O" if lc == 100 else "X" if lc == 10 else lc)(vetor[x])) for x in range(0,9)])(print()) ] if any(lj) == False else None)(vetor[18]) ] if lk == 1 else [(lambda lb: [lb.pop(len(lb)-1),(lambda la: print("\nVelha x_x\n\n") if any(la) == False and vetor[len(vetor)-1] == 10 else print("\nFim :D\n\n"))(lb)])(vetor[18])] )(vetor[19])] for number in vetor[20]])(0)])([1,2,3,4,5,6,7,8,9," "," ","\n"," "," ","\n"," "," ","\n",[0],1,[0],0])
 
 
# A explicação do processo, assim como a versão original antes de convertida ao método Lambda, se encontram no arquivo: VersaoOriginalNaoLambda.py
 
# Abaixo se encontra a explicação dos diferentes setores do código de 1 linha:
 
 
##############################
# la - Mostrar final Velha ou Fim, dependendo do conteúdo do vetor[18] e da rodada em que o jogo se encontra;
 
# lb - Lambda destinada apenas para remover o último elemento do vetor[18] e executar 'la' logo em seguida;
 
# lc - Definir a marca que será impressa("X","O" ou o próprio número da casa);
 
# ld - juntar 'lc' com o print do tabuleiro, utilizando os espaços devidos também marcados no vetor;
 
# le - repetir 'ld' 9 vezes, 9 casas com marca 'lc' para formar o tabuleiro, a mesma lambda também executa um 'print()' para melhorar a estética;
 
# lf - definir se será adicionado 10 ou 100 dependendo do jogador na posição digitada pelo usuário, que será lido por 'lc' e transformado em 'X' ou 'O';
 
# lg - A partir do int digitado pelo jogador, verificar se a posição no tabuleiro já está ocupada e executar 'lf';
 
# lh - Valor digitado pelo jogador, será verificado sua existência nas possibilidades 'li', em seguida validar o valor utilizando 'lg' e 'lf';
 
# li - Parâmetro com as únicas possibilidades de escolha do jogador (0 a 9);
 
# lj - Verificar se as condições de parada do jogo (representadas no vetor 18) são falsas, se forem, executar 'lh' e 'li';
 
# lk - Caso o vetor[19] esteja 1, ou seja, possivel repetir, será atualizado no vetor[18] as condições de parada de acordo com as modificações no jogo, e aumentará um 0 no vetor[20] (o que garante a criação de um pseudo-while utilizando um for) repetindo o código para cada elemento presente (for x in vetor[20]). Também irá adicionar em vetor[21] uma unidade para controlar o número de rodadas, algo que será controlado caso a jogada seja inválida e utilizado em caso de Velha. Se o vetor[19] = 0, irá executar 'la' e 'lb';
 
# ll - Finalizar o loop(pseudo-while de 'lk') caso alguma das condições de parada de vetor[18] sejam cumpridas(alguém ter ganhado ou ter dado velha);
 
# lm - Juntar 'll' e 'lk' com a repetição do vetor[20];
 
# ln - Mostrar tabuleiro vazio inicial apenas para o começo do jogo;
 
# vetor - juntar 'lm' e 'ln', passando o valor do vetor que armazenará todas as "variáveis" utilizadas no jogo.

################################
 
 

