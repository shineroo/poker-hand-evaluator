# Gustas Bepirštis IFF-0/4

# Dictionary for calculating hand strength
card_dict = {	
	"2":2,
	"3":3,
	"4":4,
	"5":5,
	"6":6,
	"7":7,
	"8":8,
	"9":9,
	"T":10,
	"J":11,
	"Q":12,
	"K":13,
	"A":14
}

def get_high_card(hand):
	values = [card_dict[i[0]] for i in hand]	
	return max(values)

# Return an array showing how many pairs/sets/quads a hand has
def get_value_counts(hand):
	values = [card_dict[i[0]] for i in hand]	# array with the value of every card in hand (T, J, Q, K, A converted into numbers using a dictionary)
	value_counts = [0] * 14
	for v in values:
		value_counts[v - 1]+=1
	value_counts = [i for i in value_counts if i != 0]
	return value_counts

# Check if given hand contains 1 pair
def check_pair(hand):
	value_counts = get_value_counts(hand)
	if 2 in value_counts:
		return True
	else:
		return False

# Check if given hand contains 2 pairs
def check_two_pair(hand):
	value_counts = get_value_counts(hand)
	if sorted(value_counts) == [1, 2, 2]:
		return True
	else:
		return False

# Check if given hand contains 3 of a kind
def check_three_of_a_kind(hand):
	value_counts = get_value_counts(hand)
	if 3 in value_counts:
		return True
	else:
		return False

# Check if given hand contains a straight
def check_straight(hand):
	values = [card_dict[i[0]] for i in hand]	
	value_range = max(values) - min(values)
	if value_range == 4 and len(set(values)) == 5:	
		return True
	else:
		return False

# Check if given hand contains a flush
def check_flush(hand):	
	suits = [i[1] for i in hand]
	if len(set(suits)) == 1:
		return True
	else:
		return False

# Check if given hand contains a full house
def check_full_house(hand):
	value_counts = get_value_counts(hand)
	if sorted(value_counts) == [2, 3]:
		return True
	else:
		return False

# Check if given hand contains 4 of a kind
def check_four_of_a_kind(hand):
	value_counts = get_value_counts(hand)
	if sorted(value_counts) == [1, 4]:
		return True
	else:
		return False

# Check if given hand contains a straight flush
def check_straight_flush(hand):
	if check_flush(hand) == True and check_straight(hand) == True:
		return True
	else: 
		return False

# calculates the strength of the hand
def hand_strength(hand):
	if check_straight_flush(hand):
		return 9
	if check_four_of_a_kind(hand):
		return 8
	if check_full_house(hand):
		return 7
	if check_flush(hand):
		return 6
	if check_straight(hand):
		return 5
	if check_three_of_a_kind(hand):
		return 4
	if check_two_pair(hand):
		return 3
	if check_pair(hand):
		return 2
	return 1

# Prints the winner of the 2 hands provided in the text file
def play(lines):
	for line in lines:
		white_hand = line[0:14].split(' ')
		black_hand = line[15:29].split(' ')
		if hand_strength(white_hand) > hand_strength(black_hand):
			print("White wins.")
		elif hand_strength(white_hand) < hand_strength(black_hand):
			print("Black wins.")
		else:
			if get_high_card(white_hand) > get_high_card(black_hand):
				print("White wins.")
			elif get_high_card(white_hand) < get_high_card(black_hand):
				print("Black wins.")
			else:
				print("Tie.")

# Reads a given text file and returns all of its lines
def read_data(filepath):
	with open(filepath) as input:
		lines = input.readlines()
	return lines

play(read_data("Input.txt"))