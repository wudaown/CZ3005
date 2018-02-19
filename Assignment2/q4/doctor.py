from pyswip import *

class Doctor(Prolog):
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('doctor.pl')
        self.initialize()
        self.pain = True
        self.mood = True
        self.fever = True
        self.bowel = True
        self.misc = True
        self.diagnose = True

    def deterStep(self):
        if self.pain:
            return ('pain', 'Do you experience a pain that is ')
        elif self.mood:
            return ('mood', 'Do you feel ')
        elif self.fever:
            return ('fever', 'Do you have fever that is ')
        elif self.bowel:
            return ('bowel', 'Do you experience stools that is ')
        elif self.misc:
            return ('miscellaneous', 'Do you experience ')
    
    def lastCheck(self):
        if not self.pain and \
            not self.mood and \
            not self.fever and \
            not self.bowel and \
            not self.misc:
            return False
        else:
            return True

    def setFalse(self, s):
        if s == 'pain':
            self.pain = False
        elif s == 'mood':
            self.mood = False
        elif s == 'fever':
            self.fever = False
        elif s == 'bowel':
            self.bowel = False
        elif s == 'miscellaneous':
            self.misc = False

    def initialize(self):
        self.prolog.query('initalize()')

    def read(self):
        n = self.notEvent()
        s = self.deterStep()[0]
        for i in self.prolog.query('read'+s + '(X)'):
            if i['X'] not in n:
                return i['X']

    def yesEvent(self, y):
        s = self.deterStep()[0]
        self.setFalse(s)
        self.prolog.asserta(s+'(' + y + ')')

    def noEvent(self, y):
        s = self.deterStep()[0]
        self.prolog.asserta('not_' + s + '(' + y + ')')
    
    def notEvent(self):
        s = 'not_' + self.deterStep()[0]
        n = []
        for i in list(self.prolog.query(s+'(X)')):
            n.append(i['X'])
        return n
    
    def result(self):
        n = list(self.prolog.query('diagnose(X)'))
        return n[0]['X']