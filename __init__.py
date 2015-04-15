from operator import itemgetter

def otevriSoubor(filename):
    soubor = open(filename, 'r')
    return soubor

def nactiSoubor(soubor):
    text = soubor.read()
    split = text.split()
    return split

def spoctiVyskyty(slova):
    vyskyty = {}
    
    for slovo in slova:
        upraveneSlovo = slovo.lower().strip("',.:");
        vyskyty[upraveneSlovo] = vyskyty.get(upraveneSlovo, 0) + 1
        
    print("pocet slov celkem: {} pocet unikatnich slov {}".format(len(slova), len(vyskyty)))
    return vyskyty

def tiskniVyskyty(vyskyty):
    polozky = list(vyskyty.items())
    polozky.sort(key=itemgetter(1), reverse=True)  
    
    for p in polozky:
        print("slovo {0:15s} a cetnost {1:3d}".format(p[0], p[1]))

def main():
    soubor = otevriSoubor('text.txt')
    slova = nactiSoubor(soubor)
    vyskyty = spoctiVyskyty(slova)
    tiskniVyskyty(vyskyty)
    
main()