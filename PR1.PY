#A card is drawn at random from a deck of well-shuffled cards. Find the probability of it being
#neither a king nor a spade.
Tcards=52
Kings=4
Spades=13
Spade_King=1

NonSpades=Tcards-(Spades+Kings-Spade_King)
Prob=NonSpades/Tcards
print(Prob)