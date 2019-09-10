class MyFile(object):
    def __init__(self, namafile):
        print("Membuka file %s... \n" % namafile)
        self.file = open(namafile)
    def __del__(self):
        print("\Menutup file...")
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    f = MyFile ("D:/MATERI MATKUL TEKOM/semester 3/PEMROGRAMAN LANJUT/paragraf python.txt")
    f.bacadata()
if __name__=="__main__":
    main()
