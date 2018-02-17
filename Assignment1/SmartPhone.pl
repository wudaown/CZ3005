company(sumSum).
company(appy).
business(s3).
boss(stevey, sumSum).
develop(s3,sumSum).
stolen(s3, stevey, appy).

competitor(X, Y) :- company(X),company(Y).
unethical(X) :- boss(X,Y), develop(Z,Y),stolen(Z,X,W),competitor(Y,W).
