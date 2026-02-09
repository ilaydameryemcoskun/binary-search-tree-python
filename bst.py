class Dugum:
    def __init__(self, veri):
        self.deger = veri
        self.sol = None
        self.sag = None

def ekle(kok, veri):
    if kok is None:
        return Dugum(veri)
    gecici = kok
    while True:
        if veri < gecici.deger:
            if gecici.sol is None:
                gecici.sol = Dugum(veri)
                break
            gecici = gecici.sol
        else:
            if gecici.sag is None:
                gecici.sag = Dugum(veri)
                break
            gecici = gecici.sag
    return kok

def in_order(kok):
    if kok:
        in_order(kok.sol)
        print(kok.deger, end=" ")
        in_order(kok.sag)

def pre_order(kok):
    if kok:
        print(kok.deger, end=" ")
        pre_order(kok.sol)
        pre_order(kok.sag)

def post_order(kok):
    if kok:
        post_order(kok.sol)
        post_order(kok.sag)
        print(kok.deger, end=" ")

def dugum_sayisi(kok):
    if kok is None: return 0
    return 1 + dugum_sayisi(kok.sol) + dugum_sayisi(kok.sag)

def yukseklik(kok):
    if kok is None: return -1
    return 1 + max(yukseklik(kok.sol), yukseklik(kok.sag))

girdi = input("Lutfen sayilari aralarinda bosluk birakarak yazin: ")
liste = [int(s) for s in girdi.split()]

root = None
for x in liste:
    root = ekle(root, x)

print("\nSONUCLAR:")
print("Sirali Liste (In-Order):")
in_order(root)
print("\nPost-Order:")
post_order(root)
print("\nPre-Order:")
pre_order(root)

print(f"\n\nToplam Dugum Sayisi: {dugum_sayisi(root)}")
print(f"Agac Yuksekligi: {yukseklik(root)}")