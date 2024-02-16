from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

url = "https://www.instagram.com/"

def verileri_al(kullanici_adi):
    try:
        
        urlsonhali = url + kullanici_adi
        request = Request(urlsonhali, headers={'User-Agent': 'Mozilla/5.0'})
        html_verisi = urlopen(request).read()
        soup = bs(html_verisi, 'html.parser')
        takipci_sayisi = soup.find('meta', property="og:description").attrs['content']
        takipci_sayisi = takipci_sayisi.split("-")[0]
        takipci_sayisi = takipci_sayisi.split(" ")


        print("Followers: " + takipci_sayisi[0])
        print("Following:" + takipci_sayisi[2])
        print("Posts: " + takipci_sayisi[4])
    except Exception as e:
        print("Error:", e)

def main():
    kullanici_adi = input("Enter your username: ")
    verileri_al(kullanici_adi)
if __name__ == "__main__":
    main()

