from xml.sax import handler, make_parser

class Jmeno:

    def __init__(self):
        self.idcko = ''
        self.jmeno = '' 
        self.prijmeni = ''
        self.pozice = ''

    def setJmeno(self, jmeno):
        self.jmeno = jmeno    

    def getJmeno(self):
        return self.jmeno 
    
    def setPrijmeni(self, prijmeni):
        self.prijmeni = prijmeni
    
    def getPrijmeni(self):
        return self.prijmeni 
    
    def getIdcko(self):
        return self.Idcko 
    
    def setIdcko(self, idcko):
        self.idcko = idcko
        
    def getPozice(self):
        return self.Pozice 
    
    def setPozice(self, pozice):
        self.pozice = pozice
        
        
class JmenoHandler(handler.ContentHandler):

    def __init__(self):

        self.inOsoba=False
        self.inPrijmeni=False
        self.inJmeno = False
        
        self.jmenaList = []
        
        
    def getJmenaList(self):

        return self.jmenaList    
    

    def startElement(self, name, attrs):
                       
        if (name == "jmeno"):

            self.inJmeno = True
        
        elif (name == "osoba"):
            
            self.jmeno = Jmeno()
            self.inOsoba=True
            self.jmeno.setIdcko(attrs.get("id"))
            self.jmeno.setPozice(attrs.get("pozice"))
           
                   
        elif (name == "prijmeni"):
            
            self.inPrijmeni=True
        
    
    def endElement(self, name):

        if (name == "osoba"):

            self.jmenaList.append(self.jmeno)

            self.inOsoba = False
        
        elif (name == "jmeno"):
            
            self.inJmeno=False
            
        elif (name == "prijmeni"):
            
            self.inPrijmeni=False
    

  
    def characters(self, chrs):

        if self.inJmeno:

            self.jmeno.setJmeno(chrs)
            
        elif self.inPrijmeni:
            
            self.jmeno.setPrijmeni(chrs)
                      
        
def main():

    handler = JmenoHandler()
    
    parser = make_parser()
    
    parser.setContentHandler(handler)
  
    inFile = open('zamestnanci.xml', 'r', encoding="utf-8")
      
    parser.parse(inFile)
    
    jmena = handler.getJmenaList()
    
    inFile.close()  
    
    serazeny = sorted(jmena, key=lambda x: x.jmeno)
    
    for jmeno in serazeny:
        print (jmeno.idcko+" "+jmeno.jmeno+" "+jmeno.prijmeni+" "+jmeno.pozice)    
   
main()
