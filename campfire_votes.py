#! python3

import sys
import urllib.request
from bs4 import BeautifulSoup

ossz=[]

def main():
    
    hiba=False
    oldal=1
    while not hiba:

        
        url="http://tabortuz.sziget.hu/votes/index/page:"+str(oldal)
        print("Downloading data from:",url)
        
        try:
        
            page = urllib.request.urlopen(url).read()

        except urllib.error.HTTPError:
            if oldal==1:
                print("Error while downloading!")
                sys.exit()
            else:
                print("No more data")
                hiba=True
                break
        
        soup = BeautifulSoup(page,"html.parser")
        soup.prettify()

        
        i=0
        bandak=[]
        szavazat=[]
        
        for row in soup.find_all("h4", {"class": "band-name"}):
            if i%2 == 0:
                bandak.append(row.string)        
            else:
                szavazat.append(row.string)
            i+=1

        for i in range(len(bandak)):
            ossz.append([int(szavazat[i]),bandak[i]])
        print("Done!")
        oldal+=1

    kiir()
    
def kiir():
    ossz.sort(reverse=True)
    print("\n\n\n")
    for i in range(len(ossz)):
        print("{}.  ".format(i+1),ossz[i][1],ossz[i][0])

if __name__ == "__main__":
    main()
