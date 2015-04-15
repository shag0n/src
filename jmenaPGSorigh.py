from xml.sax import handler, make_parser
import operator

cetnost = [[0 for x in range(15)] for x in range(40)]

class Jmeno:


    def __init__(self):
        self.jmeno = '' 

    def setJmeno(self, jmeno):
        self.jmeno = jmeno
    

    def getJmeno(self):
        return self.jmeno        


class JmenoHandler(handler.ContentHandler):

    def __init__(self):

        self.inJmeno = False

        self.jmenaList = [] 
        
        
    def getJmenaList(self):

        return self.jmenaList    
    

    def startElement(self, name, attrs):
                       
        if (name == "jmeno"):

            self.inJmeno = True

            self.jmeno = Jmeno()
    

    def endElement(self, name):

        if (name == "jmeno"):

            self.jmenaList.append(self.jmeno)

            self.inJmeno = False
    

    def characters(self, chrs):

        if self.inJmeno:

            self.jmeno.setJmeno(chrs)

def index(pismeno):
    znaky = "ABCDEFGHIJKLMNOPQRSTUVWXYZĚŠČŘŽÝÁÍÉÚŮŤĎ"
    for i in range(len(znaky)):
        if znaky[i] == pismeno:
            return i

def vyskytyPismen(jmenaList):
 
    prvniPismeno = {}
    
    for jmeno in jmenaList:
        jmeno = jmeno.getJmeno()
        delka = len(jmeno)
        prvniPismeno[jmeno[0]] = prvniPismeno.get(jmeno[0],0) + 1
        pozice = index(jmeno[0])
        cetnost[pozice][delka] = cetnost[pozice][delka] + 1
    return prvniPismeno



def printVysledek(prvniPismeno):
    
    serazenePismena = sorted(prvniPismeno.items(), key=operator.itemgetter(0))
    
    for pismena in serazenePismena:
        print(str.upper(pismena[0]), ": ",  pismena[1], " jmen")
        delka = 0
        for i in cetnost[index(pismena[0])]:
            delka += 1
            if(i!=0):
                print("Jména délek: ",delka," je ",i)
          
        
def main():

    handler = JmenoHandler()
    
    parser = make_parser()
    
    parser.setContentHandler(handler)
    
    inFile = open('jmena.xml', 'r', encoding="utf-8")
    
    parser.parse(inFile)
    
    jmena = handler.getJmenaList()
    
    inFile.close()   
     
    vyskyty = vyskytyPismen(jmena)

    printVysledek(vyskyty)    
   
main()
