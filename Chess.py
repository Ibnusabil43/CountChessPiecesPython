#=============================Pembacaan File Teks==========================
def baca_teks():                                                                #fungsi yang digunakan untuk membaca file teks yang disediakan lalu mengubah nya menjadi list 
    print("=========================================")
    file_input = input("Masukan Nama File Catur yang ingin di kalkulasi : ")    #inputan nama file
    try :                                                                       #menggunakan try except agar jika inputan yang diberikan tidak sesuai maka akan meminta inputan sampai program tidak terdapat error
        objek = open(file_input, "r")                                           #pembacaan file teks dengan mode "r" 
        teks = []                                                               #insiasi list kosong
        teks = objek.readline().replace("/"," ").replace(""," ").split()        #mengisi list teks dengan string didalam file teks yang sudah di replace dan di split
        objek.close()                                                           #menutup file teks
        return teks                                                             #return list teks jika inputan file teks sudah benar atau tidak terdapat error
    except FileNotFoundError:                                                   #exception untuk pengkondisian saat terjadi error FileNotFoundError
        print("=========================================")
        print("Maaf format nama file salah atau file tidak dapat ditemukan")
        return baca_teks()                                                      #return saat exception berjalan karena terjadi error, 
                                                                                #return disini akan memanggil fungsi baca_teks kembali dan meminta inputan kembali sampai tidak ditemukan error FileNotFoundError

#===========================Pembacaan String Posisi========================
def baca_string_posisi(posisi):                                                 #fitur tambahan untuk membaca inputan berupa string catur, fitur tambahan ini di definisikan sebagai fungsi baca_string_posisi
    return posisi.replace("/"," ").replace(""," ").split()                      #return dari fungsi tersebut berupa string catur yang sudah berbentuk list setelah di replace dan di split
#===============================Fungsi Nilai Buah==========================
def nilai_buah(posisi, pemain):                                                 #fungsi yang akan mengembalikan nilai bidak yang dimiliki masing2 pemain
                                                                                #fungsi ini memiliki 2 parameter yaitu list posisi yang akan didapat dari 2 fungsi pembaca file dan string diatas dan pemain yang berisi sisi pemain
    petak_berisi = []                                                           #inisiasi list kosong
    for i in posisi :                                                           #iterasi list posisi 
        if i.isalpha() == True :                                                #iterasi diatas digunakan untuk mengambil elemen didalam list yang berupa string alphabet 
            petak_berisi.append(i)                                              #setelah diambil lalu kumpulan string alphabet yang sudah dipisahkan akan dimasukkan ke dalam list petak_kosong
    n = 0                                                                       #inisiasi variable
    if pemain == "hitam" :                                                      #pengkondisian apabila jumlah bidak/buah yang ingin di jumlahkan yaitu bidak/buah sisi hitam
        hitam = {"k":200, "q":9, "r":5, "b":3, "n":3, "p":1}                    #dictionary yang berisi key berupa jenis bidak/buah dan value berupa nilai bidak/buah
                                                                                #untuk bidak hitam di notasikan dengan jenis bidak yang berupa huruf kecil
        for i in petak_berisi :                                                 #iterasi list petak_berisi
            for k, v in hitam.items():                                          #mengambil key dan value dari dict hitam
                if i == k:                                                      #pengkondisian jika terdapat elemen list petak_berisi yang sama dengan key dari dictionary 
                    n = n + v                                                   #jika pengkondisian tersebut berjalan maka variabel inisiasi n akan ditambah dengan value yang berupa nilai bidak
    if pemain == "putih" :                                                      #pengkondisian apabila jumlah bidak/buah yang ingin di jumlahkan yaitu bidak/buah sisi hitam
        putih = {"K":200, "Q":9, "R":5, "B":3, "N":3, "P":1}                    #dictionary yang berisi key berupa jenis bidak/buah dan value berupa nilai bidak/buah
                                                                                #untuk bidak hitam di notasikan dengan jenis bidak yang berupa huruf kapital
        for i in petak_berisi :                                                 #iterasi list petak_berisi
            for k, v in putih.items():                                          #mengambil key dan value dari dict putih
                if i == k:                                                      #pengkondisian jika terdapat elemen list petak_berisi yang sama dengan key dari dictionary 
                    n = n + v                                                   #jika pengkondisian tersebut berjalan maka variabel inisiasi n akan ditambah dengan value yang berupa nilai bidak
    return n                                                                    #return berupa n yaitu variabel yang sudah ditambah dengan semua nilai bidak yang terdapat pada salah satu sisi pemain
#==========================Fungsi Jumlah Petak Kosong=======================
def jumlah_petak_kosong(posisi):                                                #fungsi yang mengembalikan jumlah petak kosong dalam suatu string posisi catur dengan parameter list posisi
    petak_kosong = []                                                           #inisiasi list kosong
    for i in posisi :                                                           #iterasi list posisi 
        if i.isdigit() == True :                                                #iterasi diatas digunakan untuk mengambil elemen didalam list yang berupa string angka
            petak_kosong.append(i)                                              #menambahkan elemen list petak_kosong dengan string angka yang sudah di keluarkan
    petak_kosong_int = [int(i) for i in petak_kosong]                           #mengubah keseluruhan elemen list petak_kosong menjadi integer agar bisa dijumlahkan
    n = 0                                                                       #inisiasi variable
    for i in petak_kosong_int :                                                 #iterasi list petak_kosong_int
        n = n + i                                                               #menjumlahkan variable insiasi n akan ditambah dengan elemen list petak_kosong_int yang sudah di casting elemennya menjadi integer
    return n                                                                    #mereturn n yang sudah di jumlahkan dengan elemen list petak_kosong_int
#==============================Main Program===========================
def balik():                                                                    #fungsi untuk kembali ke menu utama atau menyelesaikan penggunaan program       
    print("=========================================")
    print("1. Kembali Ke Menu Utama")                                           #daftar Menu
    print("2. Tutup Program")
    balik = int(input("Silakan Masukkan Pilihan anda (1-2) : "))
    if balik == 1:                                                              #pengkondisian untuk pilihan menu
        kembali()                                                               #Jika Pengkondisian terpenuhi akan memanggil fungsi kembali() yang merupakan main program keseluruhan
    if balik == 2:                                                              #pengkondisian untuk pilihan menu
        print("======================================================")
        print("Terimakasih Telah Menggunakan Program Catur Hula Hula ^_^")  
    return    

def kembali():                                                                  #fungsi kembali() disini merupakan keseluruhan main program                         
    print("=========================================")                          #main program dijadikan fungsi agar dapat dipanggil kembali untuk fitur "kembali ke menu utama"
    print("SELAMAT DATANG DI PROGRAM CATUR HULA HULA")
    print("=========================================")                          #ART         
    print("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                         
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿                           
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿""")
    print("=========================================")

    print("Pilihan metode input : ")                                            #Menu Pilihan Metode Input
    print("1. Input File text")
    print("""2. Input String posisi catur 
    """)

    input_method = int(input("Silakan Ketik Pilihan Anda (1-2) : "))            #Input Pilihan

    if input_method == 1:                                                       #Pengkondisian sesuai input
        print("=========================================")
        print("Sisi Pemain yang ingin di kalkulasi :")                          #pilihan menu sisi pemain yang ingin di kalkulasi
        print("1. Putih")
        print("2. Hitam")
        print("3. Keseluruhan")
        print("4. Kembali ke menu awal")
        print("")
        pemain = int(input("Silakan Ketik Pilihan Anda (1-4) : "))              #input sisi pemain

        if pemain == 1:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi
            pemain = "putih"
            posisi = baca_teks()                                                #Pemanggulan fungsi baca_teks() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong
        
            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi                                              
            print("Nilai Buah :", nilai_buah(posisi,pemain))                    #output Nilai Buah salah satu sisi pemain
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()                                                             #pemanggilan fungsi balik() untuk memberi user untuk kembali ke menu utama atau menutup program

        if pemain == 2:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi      
            pemain = "hitam"    
            posisi = baca_teks()                                                #Pemanggulan fungsi baca_teks() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong
        
            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi
            print("Nilai Buah :", nilai_buah(posisi,pemain))                    #output Nilai Buah salah satu sisi pemain
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()                                                             #pemanggilan fungsi balik() untuk memberi user untuk kembali ke menu utama atau menutup program

        if pemain == 3:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi
            putih = "putih"                             
            hitam = "hitam"
            posisi = baca_teks()                                                #Pemanggulan fungsi baca_teks() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong
            
            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi                             
            print("Nilai Buah Putih :", nilai_buah(posisi,putih))               #output Nilai Buah sisi pemain putih
            print("Nilai Buah Hitam :", nilai_buah(posisi,hitam))               #output Nilai Buah sisi pemain hitam
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()                                                             #pemanggilan fungsi balik() untuk memberi user untuk kembali ke menu utama atau menutup program
        
        if pemain == 4:                                                         #pengkondisian apabila user ingin kembali ke menu utama
            kembali()                                                           #memanggil fungsi kembali() yang berupa main program agar kembali ke menu utama

    if input_method == 2:                                                       #Pengkondisian sesuai input
        print("=========================================")
        print("FORMAT INPUT STRING")                                            #Keterangan Format Inputan yang harus diberikan user
        print("""4k3/8/8/8/8/8/4P3/4K3 artinya pada baris pertama king hitam berada di petak ke 5 (4 petak kosong di sebelah kiri, dan 3 petak
kosong di sebelah kanan). Baris kedua hingga keenam, 8 petak kosong semua. Baris ketujuh, hanya ada pawn putih di petak kelima,
sedangkan di baris kedelapan, king putih ada dipetak ketiga""")
        print("=========================================")
        str_pos = input("Masukan String Posisi Catur yang ingin di kalkulasi : ")   #(Fitur Tambahan) Inputan berupa String posisi catur 
        print("=========================================")
        print("Sisi Pemain yang ingin di kalkulasi :")                          #pilihan menu sisi pemain yang ingin di kalkulasi
        print("1. Putih")
        print("2. Hitam")
        print("3. Keseluruhan")
        print("4. Kembali ke menu awal")
        print("")
        pemain = int(input("Silakan Ketik Pilihan anda (1-4) : "))              #input sisi pemain
        
        if pemain == 1:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi
            pemain = "putih"
            posisi = baca_string_posisi(str_pos)                                #Pemanggulan fungsi baca_string_posisi() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong
        
            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi
            print("Nilai Buah :", nilai_buah(posisi,pemain))                    #output Nilai Buah salah satu sisi pemain
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()

        if pemain == 2:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi      
            pemain = "hitam"
            posisi = baca_string_posisi(str_pos)                                #Pemanggulan fungsi baca_string_posisi() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong

            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi
            print("Nilai Buah :", nilai_buah(posisi,pemain))                    #output Nilai Buah salah satu sisi pemain
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()

        if pemain == 3:                                                         #pengkondisian sesuai inputan sisi pemain yang ingin di kalkulasi
            putih = "putih"
            hitam = "hitam"
            posisi = baca_string_posisi(str_pos)                                #Pemanggulan fungsi baca_string_posisi() untuk dijadikan variabel posisi yang akan menjadi parameter fungsi nilai_buah dan jumlah_petak_kosong
            
            print("=========================================")
            print("List Posisi :", posisi)                                      #output list posisi 
            print("Nilai Buah Putih :", nilai_buah(posisi,putih))               #output Nilai Buah sisi putih
            print("Nilai Buah Hitam :", nilai_buah(posisi,hitam))               #output Nilai Buah sisi hitam
            print("Jumlah Petak Kosong :", jumlah_petak_kosong(posisi))         #output Jumlah Petak Kosong
            balik()
        
        if pemain == 4:                                                         #pengkondisian apabila user ingin kembali ke menu utama
            kembali()                                                           #memanggil fungsi kembali() yang berupa main program agar kembali ke menu utama
    return                                                                      

kembali()                                                                       #memanggil fungsi kembali() untuk menjalankan main program