male(charles).
male(andrew).
male(edward).
female(ann).
%% elizabeth is define as queen
queen(elizabeth).
parentof(charles,elizabeth).
parentof(andrew,elizabeth).
parentof(edward,elizabeth).
parentof(ann,elizabeth).

elder(charles,ann).
elder(ann,andrew).
elder(andrew,edward).

%% predicate to search through birth date
older(X,Y):- elder(X,Y).
older(X,Y):- elder(X,Z), older(Z,Y).

successor(X,Y):- parentof(Y,X).

%% predicate to search through male by birth date
pre(X,Y):- male(X),male(Y),older(X,Y) ; male(X),female(Y).

successorList(X,SL):- findall(Y,successor(X,Y),SL).


insert_sort(List,Sorted):- i_sort(List,[],Sorted).

i_sort([],Acc,Acc).
i_sort([H|T],Acc,Sorted):- insert(H,Acc,NAcc),i_sort(T,NAcc,Sorted).
insert(X,[Y|T],[Y|NT]):-pre(Y,X),insert(X,T,NT).
insert(X,[Y|T],[X,Y|T]):-pre(X,Y).
insert(X,[],[X]).

successionLine(X):- insert_sort([charles,ann,andrew,edward],X).
