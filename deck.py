from card import Card
import random as rd

class Deck:
    def __init__(self):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(Card( s , i , str_val))

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def show_values(self):
        for card in self.cards:
            print(card.point_val)
    
    def sacar_carta(self):
        carta_elegida = rd.choice(self.cards)
        # carta_valor = carta_elegida.point_val
        self.cards.remove(carta_elegida)  
        return carta_elegida