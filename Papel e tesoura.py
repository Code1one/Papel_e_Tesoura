from random import randint
print('=_' * 25)
print(f'PEDRA, PAPEL E TESOURA.' )
print('=_' * 25)
ly=('Pedra',  'Papel',  'tesoura')
n1= randint(0, 2)
print("""Suas opções:
   [ 0 ] Pedra
   [ 1 ] Papel
   [ 2 ] Tesoura""")	 
player=int(input('Qual sua jogada?'    ))
print(f'O computador jogou {ly[n1]}' )
print(f'O jogador jogou {ly[player]}')
if n1 == 0:#Computador jogou pedra
	if player == 0:
		print('EMPATE')
	elif player == 1:
		print('Jogador ganhou')
	elif player == 2:
		print('Computador ganhou')
	else:
		print('Jogada invalida')
elif n1== 1: #Computador jogou papel.
      if player == 0:
      	print('Computador ganhou')
      elif player == 1:
      	print('Empate')
      elif player == 2: 
              print('Jogador ganhou')
      else:
       	print('Jogada invalida')
elif n1 == 2: #Computador jogou tesoura
      if player == 0:
      	print('Jogador ganhou')
      elif player == 1:
      	  print('Computador ganhou')
      elif player == 2:
      	  print('Empate')
      else:
      	print('Jogada invalida')  	  	        	        
   # 0 - pedra
   # 1- papel
   # 2 - tesoura		