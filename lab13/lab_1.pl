

directlyIn(katarina,olga).
directlyIn(olga,natasha).
directlyIn(natasha,irina).

in(X,Y):-directlyIn(X,Y).
in(X,Y):-directlyIn(X,Z),in(Z,Y).


tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([H|T],[A|B]):-tran(H,A),listtran(T,B).

/*
13.1b
% b. Yes it does. It uses FOL  and variables can be defined and used.

*/