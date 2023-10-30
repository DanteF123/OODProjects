import random
class Deck:
    def __init__(self):
        self.cards=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


class Player:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        self.hand=[]
        self.score=0
        self.bet=0

    def wager(self):
        amount=int(input(f"{self.name}, you have {self.money} how much will you bet?"))
        if amount<self.money:
            self.money-=amount
        else:
            amount=self.money
            self.money=0
        print(f"Your left over money is {self.money}")
        self.bet=amount
        return amount





class Dealer:
    def __init__(self):
        self.hand=[]
        self.score=0

class Game:
    def __init__(self):
        self.players=[]
        self.player_size=0


    def createPlayers(self):
        consent=input("Add a player? Y/N ")

        if consent=="Y":
            name=input("Name: ")
            money=int(input("Money: "))
            player=Player(name,money)
            self.players.append(player)
            self.player_size+=1
            self.createPlayers()

    def play(self):
        print("game begin")
        self.createPlayers()

        def begin():
            dealer = Dealer()
            deck=Deck()
            deck.shuffle()
            local_players=self.players.copy()

            print(f"local: {[x.name for x in local_players]}, glob{[x.name for x in self.players]}")
            def determine_winner(player,dealer):
                print(f"{player.name} your hand is {player.hand}, dealer hand is {dealer.hand}")
                if sum(dealer.hand)==21:
                    print("dealer has 21 you lose")
                    player.money-=player.bet

                elif sum(player.hand)==21:
                    print("you have 21 you win")
                    player.money+=player.bet*2

                elif sum(dealer.hand)>21:
                    print("dealer bust you win")
                    player.money += player.bet * 2

                elif sum(player.hand)>sum(dealer.hand):
                    print("you win")
                    player.money += player.bet*2

                elif sum(player.hand)==sum(dealer.hand):
                    player.money+=player.bet
                    print("tie")

                else:
                    print("you lost")
                    player.money-=player.bet

                if player.money<=0:
                    print("hi")
                    print([x.name for x in self.players])
                    self.players.remove(player)
                    print([x.name for x in self.players])

            def fold(Player):
                local_players.remove(Player)
                if Player.money<=0:
                    self.players.remove(Player)


            def check_hand(Player):
                if 11 in Player.hand:
                    if sum(Player.hand) > 21:
                        Player.hand[Player.hand.index(11)] = 1
                if sum(Player.hand) > 21:
                    print(f"{Player.name} you bust with hand {Player.hand}")
                    fold(Player)

                if sum(Player.hand)==21:
                    print(f"{Player.name} blackjack {Player.hand}")



            def check_dealer(Dealer):
                if 11 in Dealer.hand:
                    if sum(Dealer.hand) > 21:
                        Dealer.hand[Dealer.hand.index(11)] = 1



            def hit(Player):
                x=input(f"{Player.hand} {Player.name}, hit? Y/N ")
                if x=="Y":
                    Player.hand.append(deck.deal())
                    check_hand(player)
                    if sum(Player.hand)<21:
                        hit(Player)
                return Player.hand


            for player in local_players:

                player.wager()
                player.hand=[]
                player.hand.append(deck.deal())
                player.hand.append(deck.deal())
                print(f"{player.name}, your hand is {player.hand}")

            dealer.hand.append(deck.deal())
            print(f"\nDealer hand is {dealer.hand}")


            #first round of player decisions
            temp = local_players.copy()
            for player in temp:
                hit(player)

            #Dealer hand
            while sum(dealer.hand)<17:
                dealer.hand.append(deck.deal())
                check_dealer(dealer)
                print(dealer.hand)

            ##who won
            for player in local_players:
                determine_winner(player,dealer)


            if len(self.players)>0:
                if input("play again? Y/N ")=="Y":
                    begin()

        begin()

game=Game()
game.play()