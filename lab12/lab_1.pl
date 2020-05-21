%% Exercise 1.4

%% Butch is a killer
killer(butch).

%% Mia and Marsellus are married
married(mia,marsellus).

%% Zed is dead
dead(zed).

%% Marsellus kills someone if that someone footmassages mia
kills(marsellus,x):-	footmassages(x,mia).

%% Mia loves someone if that someone is a good dancer
loves(mia,x):-	goodDancer(x).

%% Jules eats something if that something is nutritious or delicious
eats(jules,x):-	nutritious(x); 
eats(jules,x):-	tasty(x).

/*
facts -  butch is a killer, they are married, and zed is dead. 
the last three are rules.
*/

%% Exercise 1.5
wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

/*
wizard(ron). = true
prolog can find ron

witch(ron). = ERROR
prolog canot find witch()

wizard(hermione). = false
false returned because prolog cannot find herminone in wizard

witch(hermione). = ERROR
prolog canot find witch()

wizard(harry). = true
prolog can finds Harry

witch(Y). = Error
prolog canot find witch()

*/