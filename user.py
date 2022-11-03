class Humano:
    def __init__(self,name,nickname,last_name):
        self.name = name
        self.nickname = nickname
        self.last_name = last_name
        self.contador = 0
        self.hand = []

    def elegir_carta(self,maso):
        carta_jugador = maso.sacar_carta()
        if carta_jugador.point_val == 11 or carta_jugador.point_val == 12 or carta_jugador.point_val == 13:
            carta_jugador.point_val = 10
            self.contador += carta_jugador.point_val
        elif carta_jugador.string_val == 'Ace' and self.contador < 15:
            carta_jugador.point_val = 10
            self.contador += carta_jugador.point_val
        else:
            self.contador += carta_jugador.point_val
        self.hand.append(carta_jugador) #agrega la nueva carta a la mano
    #imprime que carta salio


    def sumar_carta(self,maso):
        self.card_sum = 0
        for card in self.hand:
            card.string_val
            card.suit
            self.card_sum += card.point_val
            print(f'\nCartas del {self.nickname} -> {card.string_val} of {card.suit}\n')
        return self.card_sum #Suma del valor de las cartas FALTA AGREGAR CONDICION PARA As

    def show_hand(self,person):
        for card in self.hand:
            print('')
            return card.card_info()

class Dealer(Humano):
    def __init__(self,name,nickname,last_name):
        super().__init__(name,nickname,last_name)

    def mano_menor(self,maso):
        card_sum = 0
        for card in self.hand:
            card_sum += card.point_val
        if card_sum < 16:
            self.elegir_carta(maso)


class Jugador(Humano):
    def __init__(self,name,nickname,last_name):
        super().__init__(name,nickname,last_name)
    
    def preguntar(self,maso):
        respuesta = input('Quieres sacar una carta mas? Si/No: ')
        if respuesta.lower() == 'si':
            self.elegir_carta(maso)
        else:
            pass 


class Game:
    def __init__(self):
        self = self
    def check_points(self,dealer,jugador):
        if jugador.card_sum > 21:
            print('BUST, you lost')
        elif dealer.card_sum > 21:
            print('Dealer busted, you win')
            
        elif dealer.card_sum > jugador.card_sum:
            print(f'YOU LOST Dealer: {dealer.card_sum} | Player: {jugador.card_sum}')
        
        elif dealer.card_sum < jugador.card_sum:
            print(f'YOU WIN Dealer: {dealer.card_sum} | Player: {jugador.card_sum}')
            
        elif dealer.card_sum < jugador.card_sum and jugador.card_sum == 21: 
            print(f'YOU WIN BLACKJACK Dealer: {dealer.card_sum} | Player: {jugador.card_sum}')
        elif dealer.card_sum == jugador.card_sum:
            print(f'Its a draw! : {dealer.card_sum} | Player: {jugador.card_sum}')