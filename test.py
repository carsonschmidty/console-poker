def sort_hands(hands, players):
    player_hands = {}

    for x in range(players):
        player_hands["player " + str(1+x)] = [hands[0+x],hands[players+x]]

    return player_hands
hands=[[2,'red'],[3,'black'],[8,'red'],[7,'black'],[9,'red'],[2,'black'],[3,'red'],[5,'black']]
player_hands = sort_hands(hands, 4)
print(player_hands)