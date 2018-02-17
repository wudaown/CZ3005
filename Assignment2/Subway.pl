member(X,[X|_]).
member(X,[_|R]) :- member(X,R).
given(X,[X|R],R).
given(X,[F|R],[F|S]) :- given(X,R,S).
add([A | B], C, [A | D]) :- add(B, C, D).
add([], A, A).

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
