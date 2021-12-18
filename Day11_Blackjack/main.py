import random
import copy 

# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game():
	game_status = True

	print("let's play, good luck")
	player_cards = random.choices(cards, k=2)

	print(f"you've been dealt {get_nice_string(player_cards)} and have a score of {sum(player_cards)}")


	dealer_cards = random.choices(cards, k=2)
	print(f"the dealer's first card is {dealer_cards[0]}")

	while game_status:
		next_move = input("Hit or Hold? ")

		if next_move == "Hit":
			player_cards.append(random.choice(cards))

			# Assess for 11 if score > 21
			while  sum(player_cards) > 21 and 11 in player_cards:
				player_cards = replace_ace(player_cards)

			print(f"You're cards: {player_cards}, score = {sum(player_cards)}")

			if sum(player_cards) > 21:
				print("You Lose..")
				game_status = False
			elif sum(player_cards) == 21:
				print("You Win!")
				return
		else:
			game_status = False

	# Dealer to do their thing here (i.e. if less than 14, keep hitting)
	print(f"the dealer's second card is {dealer_cards[1]}")
	while sum(dealer_cards) < 17:
		dealer_cards.append(random.choice(cards))
		if sum(dealer_cards) > 21 and 11 in dealer_cards:
			dealer_cards = replace_ace(dealer_cards)

	print(f"the dealer has been dealt {get_nice_string(dealer_cards)} and has a score of {sum(dealer_cards)}")

	# Compare player vs deal score to determine winner
	if sum(dealer_cards) > 21:
		print("You Win!")
	elif sum(dealer_cards) == sum(player_cards):
		print("Draw")
	elif sum(dealer_cards) > sum(player_cards):
		print("You Lose..")
	else: print("You Win!")

def get_nice_string(list_or_iterator):
	return  ",  ".join( str(x) for x in list_or_iterator)

def replace_ace(card_list):
	updated_card_list = card_list

	for index, card in enumerate(card_list):
		if card == 11:
			updated_card_list[index] = 1
			return updated_card_list

	return updated_card_list

start_game()
