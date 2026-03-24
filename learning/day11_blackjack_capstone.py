import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

while True:
    want_to_play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n':")).lower()
    if want_to_play == 'y':
        from art import logo
        import random
        print (logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_cards = random.sample(cards,2)
        dealer_cards = random.sample(cards,2)
        #player_score = 0
        #dealer_score = 0

        if player_cards[0] + player_cards[1] > 21:
            player_score = 1 + player_cards[1]
        else:
            player_score = sum(player_cards)

        if dealer_cards[0] + dealer_cards[1] > 21:
            dealer_score = 1 + dealer_cards[1]
        else:
            dealer_score = sum(dealer_cards)

        if player_score == 21 and dealer_score == 21:
            print(f'    Your hand: {player_cards}, Your score: {player_score}')
            print(f'    Dealer cards: {dealer_cards}')
            print(f'    Player and Dealer have Blackjack! You lose!')
        elif player_score == 21:
            print(f'    Your hand: {player_cards}, Your score: {player_score}')
            print(f'    Dealer first card: {dealer_cards[0]}')
            print(f'    Player has Blackjack! You win!')
        elif dealer_score == 21:
            print(f'    Your hand: {player_cards}, Your score: {player_score}')
            print(f'    Dealer cards: {dealer_cards}')
            print(f'    Dealer has Blackjack! You lose!')
        else:
            print(f'    Your cards: {player_cards}, current score: {player_score}')
            print(f'    Dealer first card: {dealer_cards[0]}')
            while player_score < 21:
                additional_hit = str(input("Type 'y' to get another card, type 'n' to pass:")).lower()
                if additional_hit == 'y':
                    player_cards.append(random.choice(cards))
                    player_score = sum(player_cards)

                    if player_score > 21:
                        for card in player_cards:
                            if card == 11:
                                player_score-=10
                    if player_score > 21:
                        print(f'    You Lose!')
                        print(f'    Your hand: {player_cards}, Your score: {player_score}')
                        break
                    else:
                        print(f'    Your cards: {player_cards}, current score: {player_score}')
                else:

                    break
            if player_score <= 21:
                while dealer_score <17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)

                if dealer_score > 21:
                    print(f'    You win!')
                    print(f'    Your hand: {player_cards}, Your score: {player_score}')
                    print(f'    Dealer hand: {dealer_cards}, Dealer score: {dealer_score}')
                elif dealer_score > player_score:
                    print(f'    You Lose!')
                    print(f'    Your hand: {player_cards}, Your score: {player_score}')
                    print(f'    Dealer hand: {dealer_cards}, Dealer score: {dealer_score}')
                elif dealer_score < player_score:
                    print(f'    You win!')
                    print(f'    Your hand: {player_cards}, Your score: {player_score}')
                    print(f'    Dealer hand: {dealer_cards}, Dealer score: {dealer_score}')
                elif dealer_score == player_score:
                    print(f'    Its a Draw!')
                    print(f'    Your hand: {player_cards}, Your score: {player_score}')
                    print(f'    Dealer hand: {dealer_cards}, Dealer score: {dealer_score}')
    else:
        print("\n" * 100)
        break