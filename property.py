from PySide2.QtCore import QObject, Property, Signal


class property(QObject):


    def __init__(self, initr=None, inits=None):
        QObject.__init__(self)
        if initr is None:
            initr = ["0,0,0"]
        self.range = initr
        if inits is None:
            inits = [False]
        self.sweep = inits



    def setname(self, val):
        self.name = val

    def readname(self):
        return self.name

    def readrlist(self):
        return self.range

    def setrlist(self, val):
        self.range = val

    def readslist(self):
        return self.sweep

    def setslist(self, val):
        self.sweep = val

    saverange = Property(list, readrlist, setrlist)
    savesweep = Property(list, readslist, setslist)
    savename = Property(str, readname, setname)


obj = property()

obj.saverange = [[47, 2, 2]]
obj.savesweep = [True]

print(obj.saverange)
print(obj.savesweep)
