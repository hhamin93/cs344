/*

1. bread  =  bread - true

2. ’Bread’  =  bread - false

8. food(X)  =  food(bread) - true
    x= bread

9. food(bread,X)  =  food(Y,sausage) - true
    x=sausage y=bread

14. meal(food(bread),X)  =  meal(X,drink(beer)) - false

*/

%% Exercise 2.2a
house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

/*
?-  magic(house_elf) -fails

?-  wizard(harry) - fails

?-  magic(wizard). - fails

?-  magic(’McGonagall’). - fails

?-  magic(Hermione). - Hermione = dobby - fails

% - searchs: 
% -  magic(X) -> house_elf(X) -> dobby, 
% -  magic(X) -> witch(X) -> hermione, 
% -  magic(X) -> witch(X) -> mcGonagall,  
% -  magic(X) -> witch(X) -> rita_skeeter

It does uses unification to give ablility to combine rules that overlap.

It uses resolution.
*/