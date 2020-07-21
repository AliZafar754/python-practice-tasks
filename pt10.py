class Person(object):
    def getGender( self ):
        return "Unknown"


class Male( Person ):
    def getGender( self ):
        return "Male"


aMale = Male()
print(aMale.getGender())


class Female( Person ):
    def getGender( self ):
        return "Female"


aFemale = Female()
print(aFemale.getGender())

