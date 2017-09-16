In the centipede game, there is a small and a large pot on the table. The small
pot starts with 1 coin, the large pot starts with 4. Two players take turns- in
each players turn, they can choose to take the large pot and give the small pot
to the other player, or pass. If they pass, both pots double, and it's the next
player's turn. For the purposes of this project, if each player has passed for
a certain limit of turns, neither gets the pot.

The nash equilibrium of this game can be found using a technique called
"backwards induction". If it's the second player's final turn, their choice is
to either take the pot, or pass, but passing guarantees they will get nothing,
so they clearly must choose to take the large pot. However, on the first
players final turn, they know for certain that if they pass, the second player
will take the large pot- if they take the large pot now, they guarantee
themselves twice the payoff. But on the second player's penultimate turn, they
can double their payoff by taking the large pot instead of passing... and so on
and so on until the first player must take the pot on their first turn.

Human players rarely play the game this way, resulting in much larger payoffs
in practice. My hunch is that this is because they are using "mixed
strategies", where each turn they have a certain probability for each possible
move.

A mixed strategy for this game can be represented by an array of numbers 0-1,
where the nth number represents the probability that the player will take the
pot on their nth turn.

This project will generate random mixed strategies, play them against each
other, and generate new strategies based on the most successful ones, hopefully
evolving successful strategies with a higher payoff than the pure strategy at
the nash equilibrium.

Calling python3 centipede.py will generate a pool of 10 first-turn players with
random strategies, and a pool of 10 second-turn players with random strategies,
and run 10000 rounds of evolution with them, printing the scores for each
round. After all rounds are finished, it will print the surviving strategies.

To run the tests, you will need nostests. Run "nosetests tests.py". Hopefully
this will be very boring.
