import os ,dataset,math,random #memanggil library yang akan digunakan
dataset=input("masukkan nama dataset : ")#mengimputkan nama dataset dari keyboard
cities=input("masukkan jumlah kota : ")#mengimputkan nama kota dari keyboard
label=input("masukkan label kota : ")#mengimputkan label dari keyboard
kordinat=input("masukkan koordinat kota : ")#mengimputkan tour dari keyboard
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)#fungsi menghitung jarak dua titik kota a-b;b-c,dst.
def totaldistancetour(tour):
    d=0 #fungsi menghitung total jarak yang akan terakumulasi dengan nilai awal =0 
    print(cities)#mencetak nama kota yang dikunjungi
    print(tour)#mencetak jumlah kota yang dikunjungi
    for i in range(1,len(tour)):#perulangan yang akan terjadi akumulasi secara terus menerus hingga mencapai batas yang telah di tentukan
    x1=cities[tour[i-1]][0]#x1 merupakan kota ke 0 dari cities yang ke tour i-1(0) dengan dua kolom dengan koordinat x kolom 0
    y1=cities[tour[i-1]][1]#y1 merupakan kota ke 1 dari cities yang ke tour i-1(0) dengan dua kolom dengan koordinat y kolom 1
    x2=cities[tour[i]][0]#x1 merupakan kota ke 0 dari cities yang ke tour 1 dengan dua kolom dengan koordinat x kolom 0
    y2=cities[tour[i]][1]#x1 merupakan kota ke 0 dari cities yang ke tour 1 dengan dua kolom dengan koordinat x kolom 1
    d=d+distance(x1,y1,x2,y2)#menghitung jarak sementara dari satu kota ke satu kota lainnya
    print("jarak seentara" ,d)
    x1=cities[tour[len(tour)-1]][0]
    y1=cities[tour[len(tour)-1]][1]
    x2=cities[tour[0]][0]
    y2=cities[tour[0]][1]
    d=d+distance(x1,y1,x2,y2)#menghitung total jarak yang telah di lewati dan kembali ke kota awal
    return d
os.getcwd()
xls=pandas.exelfile
sheet = pandas.read_exel(xls,sheet1)
cities=sheet.as_matrix()
n=len(cities)
tour=random.sample(range(n),n)
print("tour dengan biaya terendah untuk mengunjungi semua kota dengan biaya minimum",tour)#mencetak tour dengan biaya terendah untuk mengunjungi semua kota dengan biaya minimum
    
    

