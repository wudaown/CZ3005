main:-readpain(),
      readmood(),
      readfever(),
      readbowel(),
      readmiscellaneous(),
      diagnose().

% dynamic predicate to store the conditions of patient
:- dynamic pain(X).
:- dynamic mood(X).
:- dynamic fever(X).
:- dynamic bowel(X).
:- dynamic miscellaneous(X).
:- dynamic not_pain(X).
:- dynamic not_mood(X).
:- dynamic not_fever(X).
:- dynamic not_bowel(X).
:- dynamic not_miscellaneous(X).

% this part is included specially for GUI program
c(cancer).
a(amoebiasis).
b(barbados).
r(rabies).
h(heart_trouble).
d(dehydration).
o(others).


input(X):-
   X=='yes'.

% determine a list is empty or not
emptyList([]):-true().
emptyList([_|_]):-false().


% Symptom lists
painLibrary([severe,moderate,mild,no]).
moodLibrary([gloomy, grumpy, guilty, indifferent, irritated, mad, melancholy, pessimistic, rejected, restless, sad, stressed, weird]).
feverLibrary([extremely_high,high,mild,low,no]).
bowel_movementsLibrary([hard,loose,tarry,bloody,normal]).
miscellaneousLibrary([fatigue,coughing,itchy,giddy,hallucinating,twitches,palpitations,no_special_symptoms]).


% Diseases rules
cancer(X):-pain(strong),mood(gloomy),fever(mild),bowel(bloody),
          miscellaneous(giddy),c(X).
barbados(X):- pain(mild),mood(grumpy),fever(low),miscellaneous(fatigue),b(X).
amoebiasis(X):-pain(unbearable),mood(weepy),fever(high),bowel(loose),
              miscellaneous(itchy),a(X).
rabies(X):-pain(strong),mood(angry),fever(high),bowel(normal),
          miscellaneous(hallucinating),r(X).
heart_trouble(X):-pain(unbearable),mood(stressed),fever(no),bowel(normal),
                 miscellaneous(palpitations),h(X).
dehydration(X):-pain(no),mood(calm),fever(no),bowel(hard),
               miscellaneous(giddy),d(X).


% diagnose rules depending on disease rules
diagnose(X):-nl,
            cancer(X)->write("You may have cancer."); % if have cancer then print
            amoebiasis(X)->write("You may have amoebiasis.");
            barbados(X)->write("You may have barbados")
            rabies(X)->write("You may have rabies.");
            heart_trouble(X)->write("You may have heart trouble.");
            dehydration(X)->write("you may have dehydration.");
            o(X)->write("The current knowledge base cannot determine your diseases").

/*
% take out member of element from list, this part is for GUI program
readpain(X):- painLibrary(Y), member(X,Y).
readmood(X):- moodLibrary(Y), member(X,Y).
readfever(X):- feverLibrary(Y), member(X,Y).
readbowel(X):- bowel_movementsLibrary(Y), member(X,Y).
readmiscellaneous(X):- miscellaneousLibrary(Y), member(X,Y).
*/

readpain():-painLibrary(X),readpain(X). 
readmood():-moodLibrary(X),readmood(X).
readfever():-feverLibrary(X),readfever(X).
readbowel():-bowel_movementsLibrary(X),readbowel(X).
readmiscellaneous():-miscellaneousLibrary(X),readmiscellaneous(X).


readpain(List):-
                  [H|T]=List,
                  format("Do you experience pain that is ~w",[H]), 
                  read(X), % read user input
                  ((input(X);emptyList(T))->assert(pain(H)); 
                  readain(T)).


readmood(List):-
                  [H|T]=List,
                  format("Do you feel ~w",[H]),
                  read(X),
                  ((input(X);emptyList(T))->assert(mood(H));
                  readmood(T)
                  ).


readfever(List):-
                  [H|T]=List,
                  format("Do you have fever that is ~w",[H]),
                  read(X),
                  ((input(X);emptyList(T))->assert(fever(H));
                  readfever(T)
                  ).


readbowel(List):-
                  [H|T]=List,
                  format("Do you experience stools that is ~w",[H]),
                  read(X),
                  ((input(X);emptyList(T))->assert(bowel(H));
                  readbowel(T)
                  ).

readmiscellaneous(List):-
                  [H|T]=List,
                  format("Do you experience ~w ",[H]),
                  read(X),
                  ((input(X);emptyList(T))->assert(miscellaneous(H));
                  readmiscellaneous(T)
                  ).
