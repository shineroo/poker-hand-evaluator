# poker-hand-evaluator
python school project

A poker deck contains 52 cards - each card has a suit which is one of clubs, diamonds, hearts, or spades
(denoted C, D, H, S in the input data). Each card also has a value which is one of 2, 3, 4, 5, 6, 7, 8, 9,
10, jack, queen, king, ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A). For scoring purposes, the suits
are unordered while the values are ordered as given above, with 2 being the lowest and ace the highest
value.
A poker hand consists of 5 cards dealt from the deck.

Input
The input file (which is to be put in the same directory and called "Input.txt") contains several lines, each containing the designation of 10 cards: the first 5 cards are
the hand for the player named ‘Black’ and the next 5 cards are the hand for the player named ‘White’.

Output
For each line of input, prints a line containing one of:
Black wins.
White wins.
Tie.

Sample Input
2H 3D 5S 9C KD 2C 3H 4S 8C AH
2H 4S 4C 2D 4H 2S 8S AS QS 3S
2H 3D 5S 9C KD 2C 3H 4S 8C KH
2H 3D 5S 9C KD 2D 3H 5C 9S KH

Sample Output
White wins.
Black wins.
Black wins.
Tie
