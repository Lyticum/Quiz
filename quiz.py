import random
import sys

oyun=True
while oyun:
    sorular={ 

    "soru1" : {"soru" : "Türkiyenin başkenti neresidir?",
    "cevap" : "Ankara" }, 
    "soru2" : {"soru" : "Nobel ödüllü Türk bilim insanı kimdir",
    "cevap" : "Aziz Sancar"},
    "soru3" : {"soru" : "İlber .... adlı ünlü tarihçinin soyadı nedir?",
    "cevap" : "Ortaylı"}
            }

    score=0

    for key, value in sorular.items():
        print(value["soru"])
        cevap = input("Cevap nedir?")

        if cevap.lower() == value["cevap"].lower():
            print("Cevap doğru")
            score += 1
            print(score)
        else:
            print("Cevap yanlış")
            loop = input("Tekrar oynamak ister misiniz? Evet; E Hayır;H").lower()
            if loop == "e":
                oyun=True
            elif loop =="h":
                sys.exit("Oynadığınız için teşekkürler")
            else:
                print("Lütfen E veya H harflerini kullanın!")
    
