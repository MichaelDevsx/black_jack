from card import Card
from deck import Deck
from user import *



#1. CREAR MASO DE CARTAS
my_deck = Deck()
print('El juego esta iniciando, Dealer moviendo cartas \n')


#2. CREAR DEALER Y JUGADOR

dealer = Dealer('Kayla','Dealer','Vk')

player = Jugador('Michael','Player','Ch')

print(f'''
Jugadores se posicionan

{dealer.nickname} = {dealer.name} , {dealer.last_name}

{player.nickname} = {player.name} , {player.last_name}\n
''')

#3. DEALER DRAWS CARD Y JUGADOR DRAWS CARD 
print('----------------------------\n')
dealer.elegir_carta(my_deck)
player.elegir_carta(my_deck)
print(f'{dealer.nickname} reparte las cartas \n')
#4. Dealer y jugador show cards
print(f'{dealer.nickname} Muestra su carta')
dealer.show_hand('Dealer')
print('\n----------------------------\n')
print(f'{player.nickname} Muestra su carta')
player.show_hand('Jugador')
print(f'\nEl acumulativo de {dealer.name} es - > {dealer.contador}\n')
print(f'\nEl acumulativo de {player.name} es - > {player.contador}\n')

#5. DEALER DRAWS CARD (NO SE MUESTRA) Y JUGADOR DRAWS CARD

dealer.elegir_carta(my_deck)
player.elegir_carta(my_deck)

# #6 IMPRIME LA MANO DEL JUGADOR

# player.show_hand('Jugador')

#7 PREGUNTA POR SI QUIERE SACAR UNA MAS...

player.preguntar(my_deck)


#8 CHEQUEA QUE LA MANO DEL DEALER SEA MENOR O MAYOR A 16 Y DRAWS (O NO ) CARD

dealer.mano_menor(my_deck)

print('\n----------------------------\n')

dealer.sumar_carta(my_deck)
print('\n----------------------------\n')
player.sumar_carta(my_deck)

print('\n----------------------------\n')
dealer.card_sum
player.card_sum


print(f'\nEl acumulativo de {dealer.name} es - > {dealer.contador}\n')
print(f'\nEl acumulativo de {player.name} es - > {player.contador}\n')
#9 COMPARA PUNTAJES
print('\n----------------------------\n')
game = Game()
game.check_points(dealer,player)