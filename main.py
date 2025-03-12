VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    
    score = 0
    face_cards_list = ['Jack', 'Queen', 'King']
    ace_counter = 0

    for card in hand:
        if card not in VALID_CARDS or len(hand) > 5:
            return 'Invalid'
        elif isinstance(card, int):
            score += card
        elif card in face_cards_list:
            score += 10
        elif card == 'Ace':
            ace_counter += 1

    for i in range(ace_counter):
        if(score > 10 or i < ace_counter - 1):
            score += 1
        else:
            score += 11

    result = None

    if score > 21:
        result = 'Bust'
    else:
        result =  score

    return result