
/*
ask(X,Y):-
	order(Y), related(X,Y).
ask(X,Y):-
	random(X).
askBread(X,Y):-
    order(Y), relatedBread(X,Y).
askMains(X,Y):-
    order(Y), relatedMains(X,Y).
askCheeses(X,Y):-
    order(Y), relatedCheeses(X,Y).
askVegs(X,Y):-
    order(Y), relatedVegs(X,Y).
askCookies(X,Y):-
    order(Y), relatedCookies(X,Y).
askAddons(X,Y):-
    order(Y), relatedAddons(X,Y).
askSauces(X,Y):-
    order(Y), relatedSauces(X,Y).

askBread(X,Y):-
	randomBread(X).
askMains(X):-
	randomMains(X).
askCheeses(X):-
	randomCheeses(X).
askVegs(X):-
	randomVegs(X).
askSauces(X):-
	randomSauces(X).
askCookies(X):-
	randomCookies(X).
askAddons(X):-
	randomAddons(X).
*/



/*
relatedBread(X,Y) :- bread(L), member(X,L), member(Y, L).
relatedMains(X,Y):- mains(L),member(X,L),member(Y,L).
relatedCheeses(X,Y):- cheeses(L),member(X,L),member(Y,L).
relatedVegs(X,Y):- vegs(L),member(X,L),member(Y,L).
relatedCheeses(X,Y):- cookies(L),member(X,L),member(Y,L).
relatedAddons(X,Y):- addons(L),member(X,L),member(Y,L).
relatedSauces(X,Y):- addons(L),member(X,L),member(Y,L).
*/

member(X,[X|_]).
member(X,[_|R]) :- member(X,R).
takeout(X,[X|R],R).
takeout(X,[F|R],[F|S]) :- takeout(X,R,S).
append([A | B], C, [A | D]) :- append(B, C, D).
append([], A, A).

askBread(X, Y):- bread(L), member(X,L).
askMains(X):- mains(L),member(X,L).
askCheeses(X):- cheeses(L),member(X,L).
askSauces(X):- sauces(L),member(X,L).
askVegs(X):- vegs(L),member(X,L).
askCookies(X):- cookies(L),member(X,L).
askAddons(X):- addons(L),member(X,L).

bread([italian, heartyitalian, wheat, honeyoat, wholegrain, parmesan, flatbread, wrap, salad]).
mains([ham, turkey, coldcut, bbqchicken, tuna, eggmayo, meatball]).
cheeses([american, monterrey]).
vegs([lettuce, tomato, cucumber, capsicum, onion, jalapeno, pickle, avocado]).
sauces([bbq, honeymustard, mustard, sweetonion, redwine, mayonnaise, chipottle, ranch, vinegar]).
cookies([chocchip, doublechoc, walnut, macnut, raspberry, brownie]).
addons([drink, soup, chips]).

:- dynamic order(nothing).
:- dynamic reject(nothing).
:- dynamic pass(nothing).
