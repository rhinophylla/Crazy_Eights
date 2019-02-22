This is a python implementation of the classic children's card game, Crazy Eights.

To play the game, download the file "Crazy_Eight.py", and run on your python interpreter.

Complete rules for the game can be found at https://en.wikipedia.org/wiki/Crazy_Eights.

In this version of the game, it is you versus the computer!  You and the computer are each dealt
7 cards and a top card is turned face up.  The remaining cards in the deck become the stockpile.
You go first and you must match either the suit or the face value of the top card.  The card you play
becomes the new top card and the computer then takes a turn trying to match it.  Play continues alternating
between you and computer.  If a player cannot match the top card, they must draw from the stockpile until
they can do so.  In this game, 8s are wild and if a player plays an 8, they specify a suit that the next
played card must match.  Play continues until a player plays all their cards and they are declared the
winner.  If the stockpile runs out of cards before this happens, then the winner is determined using a point
method.  Points are tabulated for the computer and your hands and the player with the lowest point total wins.
8s are worth 50 points, court cards are worth 10 points, and all other cards (including aces) are worth their
pip value.

Enjoy the game!

I welcome any feedback on improving the play experience or the code.
