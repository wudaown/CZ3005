
/* ask(gift,0). */
ask(X,Y):-
	order(Y), related(X,Y).
ask(X,Y):-
	random(X).

askBread(X,Y):-
    order(Y), relatedBread(X,Y).

relatedBread(X,Y) :- bread(L), member(X,L), member(Y, L).



member(X,[X|_]).
member(X,[_|R]) :- member(X,R).
takeout(X,[X|R],R).
takeout(X,[F|R],[F|S]) :- takeout(X,R,S).
append([A | B], C, [A | D]) :- append(B, C, D).
append([], A, A).
/* related(X,Y):- bread(L),member(X,L),member(Y,L). */
related(X,Y):- outdoorsy(L),member(X,L),member(Y,L).
related(X,Y):- social(L),member(X,L),member(Y,L).
related(X,Y):- health_freak(L),member(X,L),member(Y,L).
related(X,Y):- loner(L),member(X,L),member(Y,L).

/* random(X):- bread(L),member(X,L). */
randomBread(X):- bread(L), member(X,L).
random(X):- outdoorsy(L),member(X,L).
random(X):- social(L),member(X,L).
random(X):- health_freak(L),member(X,L).
random(X):- loner(L),member(X,L).

bread([gifts,wine]).
outdoorsy([picnic,trekking,soccer,sports,jogging,kayaking,parks,event,woods,mountains,beaches,cricket,action_movies,dogs,lakes,fairs,swimming,breeze,fitness,water]).
social([coffee,picnic,friends,party,beer,music,concert,event,movie,soccer,dinner,gifts,gardens, roses, flowers,bouquet,cricket,board_games,cafe,netflix,dogs,networking,exhibitions,fairs,debates]).
health_freak([sports,tea,fruitjuice,smoothie,trekking,training,jogging,soccer,sweating,sleeping,swimming,lakes,exercise,burpees,fitness,cats,water,music]).
loner([books,coffee,woods,candlelight,sleeping,training,jogging,night,tea,beaches,poetry,tea,rains,fiction, novels,board_games,netflix,cats,music,painting,sketching,writing,diaries]).

/*Do not know what is below this*/
all(L):- flatten([bread(X),outdoorsy(X),social(X),health_freak(X),loner(X)], L).

flatten(List, FlatList) :-
flatten(List, [], FlatList0),!,FlatList = FlatList0.
flatten(Var, Tl, [Var|Tl]) :- var(Var),!.
flatten([], Tl, Tl) :- !.
flatten([Hd|Tl], Tail, List) :-
  !,
  flatten(Hd, FlatHeadTail, List),
  flatten(Tl, Tail, FlatHeadTail).
flatten(NonList, Tl, [NonList|Tl]).
/*Do not know what is above this*/


order(X).
reject(X).
pass(X).
