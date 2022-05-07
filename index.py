from os import system, name

DataNama = ['Dummy', 'Naiko']
DataPins = ['0123', '9999']
DataUang = [10000, 1000000]
deposit = 0
withdraw = 0
uang = 0
counter_1 = 1
counter_2 = 2
i = 0

while True:
    system("cls")
    print("\n=====================================")
    print(" WaPL - Testing Program   ")
    print("*************************************")
    print("=<< 1. Buat akun baru             >>=")
    print("=<< 2. Withdraw Uang              >>=")
    print("=<< 3. Deposit Uang               >>=")
    print("=<< e. Keluar dari Program        >>=")
    print("*************************************\n")
    MenuPilih = input("Pilih menu yang diatas : ")
    if MenuPilih == "1":
        print("Anda menekan nomor " + str(MenuPilih))
        NOC = 1 
        i = i + NOC
        if i > 5:
            print("Error!, kamu hanya bisa membuat 1 account")
        else:
            while counter_1 <= i:
                name = input("Input Nama : ")
                DataNama.append(name)
                pin = str(input("Input Pins : "))
                DataPins.append(pin)
                uang = 0
                deposit = eval(input("Input uang yang akan dimasukkan ke bank : "))
                uang = uang + deposit
                DataUang.append(uang)
                print("\nNama =", end=" ")
                print(DataNama[counter_2])
                print("Pin =", end=" ")
                print(DataPins[counter_2])
                print("Uang = Rp.", end=" ")
                print(DataUang[counter_2])
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("Note: Simpan pins baik baik dan jangan kasih tau kesiapapun")
                print("========================================")
        mainMenu = input("Pencet apapun untuk kembali! ")
    elif MenuPilih == "2":
        j = 0
        print("Anda menekan nomor " + str(MenuPilih))
        while j < 1:
            k = -1
            name = input("Input Nama: ")
            pin = input("Inpun Pin: ")
            while k < len(DataNama) - 1:
                k = k + 1
                if name == DataNama[k]:
                    if pin == DataPins[k]:
                        j = j + 1
                        print("Isi uang dalam bank anda: Rp. ", end=" ")
                        print(DataUang[k], end=" ")
                        uang = (DataUang[k])
                        withdraw = eval(input("Input nilai yang akan diambil: "))
                        if withdraw > uang:
                            print("Uang anda tidak cukup!\n")
                            mainMenu = input("Pencet apapun untuk kembali!")
                        else:
                            uang = uang - withdraw
                            print("\n")
                            print("Uang Berhasil diambil sebanyak: " + str(withdraw))
                            DataUang[k] = uang
                            print("Saldo anda: Rp.", uang)
            if j < 1:
                print("Nama/pin tidak ditemukan/Salah/Belum Terdaftar!\n")
                break
        mainMenu = input("Pencet apapun untuk kembali!")
    elif MenuPilih == "3":
        print("Anda menekan nomor " + str(MenuPilih))
        n = 0
        while n < 1:
            k = -1
            name = input("Input Nama: ")
            pin = input("Inpun Pin: ")
            while k < len(DataNama) - 1:
                k = k + 1
                if name == DataNama[k]:
                    if pin == DataPins[k]:
                        n = n + 1
                        print("Saldo Anda: Rp.", end=" ")
                        print(DataUang[k])
                        uang = (DataUang[k])
                        deposit = eval(input("Input nilai yang akan di tabung : "))
                        uang = uang + deposit
                        DataUang[k] = uang
                        print("\n")
                        print("Anda berhasil menabung uang anda senilai: Rp.",deposit)
                        print("Saldo Bank anda: Rp.", uang)
            if n < 1:
                print("Nama/pin tidak ditemukan/Salah/Belum Terdaftar!\n")
                break
        mainMenu = input("Pencet apapun untuk kembali! ")
    elif MenuPilih == "e":
        print("Anda menekan " + str(MenuPilih))
        print("Terima kasih telah menggunakan layanan kami")
        print("\n")
        break
    else:
        print("Menu tidak ada dipilihan")
        print("Silahkan coba lagi!")
        mainMenu = input("Pencet apapun untuk kembali! ")   