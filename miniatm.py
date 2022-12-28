#mini_atm/python-projctkeybaord using

import datetime
from datetime import datetime,time
import time
while True:
    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour   #clock

    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour   #clock

    print("=" * 60 + "\n" + "=" * 17 + "-|" + "Aplikasi ATM Sederhana" + "|-" + "=" * 17)
    print("=" * 16 + "-|" + jamLokal + "|-" + "=" * 16)
    if 0 <= jam <= 6:
        print("=" * 21 + "-<|Selamat Subuh|>-" + "=" * 20)

    elif 6 <= jam <= 12:
        print("=" * 21 + "-<|Selamat Pagi|>-" + "=" * 21)

    elif 12 <= jam <= 14:
        print("=" * 21 + "-<|Selamat Siang|>-" + "=" * 20)

    elif 14 <= jam <= 18:
        print("=" * 22 + "-|Selamat Sore|-" + "=" * 22)

    elif 18 <= jam <= 24:
        print("=" * 21 + "-<|Selamat Malam|>-" + "=" * 20)
    print(60 * "=")

    #Input Account Bank

    nama = input('Silahkan Masukan Nama : ')
    if nama == '':
        print("Nama Tidak Boleh Kosong")
        continue
    rekening = int(input('Silahkan Masukan No.Rekening  : '))
    print('Atas Nama '+nama+', Apa Yang Bisa Kami Bantu ?')
    print("1. Cek Uang\n2. Ambil Uang\n3. Tabung Uang\n4. Transfer Uang\n5. Batal")
    pilih1 = int(input("Masukan Pilihan : "))
    saldo = 'Rp.5.000.000'
    if pilih1 == 1:
        print("Saldo Kamu : ",saldo)
        continue
    elif pilih1 == 2:

        #Withdraw

        print(57*'=')
        print("Silahkan Masukan Pilihan Jumlah Uang Yang Ingin Di Ambil")
        print("1. Rp.50.000\n2. Rp.100.000\n3. Rp.200.000\n4. Rp.500.000\n5. Rp.1.000.000\n6. Batal")
        pilih_1 = int(input('\n= '))
        if pilih_1 == 1:
            total1 = 'Rp.4.950.000'
            print("Kamu Mengambil Rp.50.000, Sisa Uang Kamu adalah ",total1)
            continue
        elif pilih_1 == 2:
            total2 = 'Rp.4.900.000'
            print("Kamu Mengambil Rp.100.000, Sisa Uang Kamu Adalah",total2)
            continue
        elif pilih_1 == 3:
            total3 = 'Rp.4.800.000'
            print("Kamu Mengambil Rp.200.000, Sisa Uang Kamu Adalah",total3)
            continue
        elif pilih_1 == 4:
            total4 = 'Rp.4.500.000'
            print("Kamu Mengambil Rp.500.000, Sisa Uang Kamu Adalah",total4)
            continue
        elif pilih_1 == 5:
            total5 = 'Rp.4.000.000'
            print("Kamu Mengambil Rp.1.000.000, Sisa Uang Kamu Adalah",total5)
            continue
        elif pilih_1 == 6:
            break
        else:

        #imvest

            print("Pilihan Anda Tidak Tersedia")
    elif pilih1 == 3:
        print(59*'=')
        print("Silahkan Masukan Pilihan Jumlah Uang Yang Ingin Di Tabung")
        print("1. Rp.50.000\n2. Rp.100.000\n3. Rp.200.000\n4. Rp.500.000\n5. Rp.1.000.000\n6. Batal")
        pilih_2 = int(input('\n: '))
        if pilih_2 == 1:
            total1 = 'Rp.5.050.000'
            print("Kamu Menabung Rp.50.000, Total Uang Kamu adalah ",total1)
            continue
        elif pilih_2 == 2:
            total2 = 'Rp.5.100.000'
            print("Kamu Menabung Rp.100.000, Total Uang Kamu Adalah",total2)
            continue
        elif pilih_2 == 3:
            total3 = 'Rp.5.200.000'
            print("Kamu Menabung Rp.200.000, Total Uang Kamu Adalah",total3)
            continue
        elif pilih_2 == 4:
            total4 = 'Rp.5.500.000'
            print("Kamu Menabung Rp.500.000, Total Uang Kamu Adalah",total4)
            continue
        elif pilih_2 == 5:
            total5 = 'Rp.6.000.000'
            print("Kamu Menabung Rp.1.000.000, Total Uang Kamu Adalah", total5)
            continue
        elif pilih_2 == 6:
            break
        else:

        #Transfer

           print("Pilihan Anda Tidak Tersedia")
    elif pilih1 == 4:
        print(59*'=')
        print("Silahkan Masukan Nama dan No.Rekening Penerima")
        penerima = input('Nama Penerima         : ')
        nomor = int(input('No.Rekening Penerima  : '))
        if penerima and nomor == "":
            print("Nama Dan No.Rekening Tidak Boleh Kosong")
            continue
        print(57*'=')
        print('Nama Penerima :',penerima)
        print('No.Rekening   : ',nomor)
        print("Apakah Sudah Yakin Data Ini Benar ?\nKami Tidak Bertanggung Jawab Jika Data Yang Anda Masukan Salah")
        print("1. Iya\n2. Tidak")
        konfirmasi = int(input('Masukan Pilihan : '))
        print(59 * '=')

        if konfirmasi == 1:
            print("Silahkan Masukan Nominal Yang Ingin Di Transfer")
            print("1. Rp.50.000\n2. Rp.100.000\n3. Rp.200.000\n4. Rp.500.000\n5. Rp.1.000.000\n6. Batal")
            data = int(input('Masukan Pilihan : '))
            print(59 * '=')
            if data == 1:
                transfer1 = 'Rp.50.000'
                print("Kamu Mentransfer uang Rp.50.000 Kepada",penerima,"\nDengan No.Rekening",nomor,",Sekarang Sisa Uang Kamu adalah", transfer1)
            elif data == 2:
                transfer2 = 'Rp.100.000'
                print("Kamu Mentransfer uang Rp.100.000 Kepada",penerima,"\nDengan No.Rekening",nomor,",Sekarang Sisa Uang Kamu adalah", transfer2)
            elif data == 3:
                transfer3 = 'Rp.250.000'
                print("Kamu Mentransfer uang Rp.200.000 Kepada",penerima,"\nDengan No.Rekening",nomor,",Sekarang Sisa Uang Kamu adalah", transfer3)
            elif data == 4:
                transfer4 = 'Rp.500.000'
                print("Kamu Mentransfer uang Rp.500.000 Kepada",penerima,"\nDengan No.Rekening",nomor,",Sekarang Sisa Uang Kamu adalah", transfer4)
            elif data == 5:
                transfer5 = 'Rp.1.000.000'
                print("Kamu Mentransfer uang Rp.1.000.000 Kepada",penerima,"\nDengan No.Rekening",nomor,",Sekarang Sisa Uang Kamu adalah", transfer5)
            elif data == 6:
                break
            else:

            #Transfer Receipt

               print("Pilihan Anda Tidak Tersedia")
            print(59 * '=')
            print("Apakah Ingin Di Sertakan Bukti Transfer ?")
            print("1. Iya\n2. Tidak")
            konfirmasi1 = int(input("Masukan Pilihan : "))
            if konfirmasi1 == 1:
                jamLokal = time.asctime(time.localtime(time.time()))
                jam = time.localtime().tm_hour

                print("=" * 60 + "\n" + "=" * 20 + "-| " + "Bukti Transfer" + " |-" + "=" * 20)
                print("=" * 16 + "-|" + jamLokal + "|-" + "=" * 16)
                if 0 <= jam <= 6:
                    print("=" * 21 + "-<|Selamat Subuh|>-" + "=" * 20)

                elif 6 <= jam <= 12:
                    print("=" * 21 + "-<|Selamat Pagi|>-" + "=" * 21)

                elif 12 <= jam <= 14:
                    print("=" * 21 + "-<|Selamat Siang|>-" + "=" * 20)

                elif 14 <= jam <= 18:
                    print("=" * 22 + "-|Selamat Sore|-" + "=" * 22)

                elif 18 <= jam <= 24:
                    print("=" * 21 + "-<|Selamat Malam|>-" + "=" * 20)
                kode_transfer = datetime.now()
                tf = rekening
                nomor_transfer = nomor
                nama_pengirim = nama
                nama_penerima = penerima
                No_Rekening = nomor
                if  data == 1:
                    print("Kode Transfer          : ",kode_transfer)
                    print("Nama Pengirim          : ",nama_pengirim)
                    print("No.Rekening Pengirim   : ",tf)
                    print("Nama Penerima          : ",nama_penerima)
                    print("No.Rekening Penerima   : ",No_Rekening)
                    print("Jumlah Transfer        : ",transfer1)
                    print(59 * '=')
                    break # done
                elif data == 2:
                    print("Kode Transfer          : ", kode_transfer)
                    print("Nama Pengirim          : ", nama_pengirim)
                    print("No.Rekening Pengirim   : ", tf)
                    print("Nama Penerima          : ", nama_penerima)
                    print("No.Rekening Penerima   : ", No_Rekening)
                    print("Jumlah Transfer        : ", transfer2)
                    print(59 * '=')
                    break # done
                elif data == 3:
                    print("Kode Transfer          : ", kode_transfer)
                    print("Nama Pengirim          : ", nama_pengirim)
                    print("No.Rekening Pengirim   : ", tf)
                    print("Nama Penerima          : ", nama_penerima)
                    print("No.Rekening Penerima   : ", No_Rekening)
                    print("Jumlah Transfer        : ", transfer3)
                    print(59 * '=')
                    break # done
                elif data == 4:
                    print("Kode Transfer          : ", kode_transfer)
                    print("Nama Pengirim          : ", nama_pengirim)
                    print("No.Rekening Pengirim   : ", tf)
                    print("Nama Penerima          : ", nama_penerima)
                    print("No.Rekening Penerima   : ", No_Rekening)
                    print("Jumlah Transfer        : ", transfer4)
                    print(59 * '=')
                    break # done
                elif data == 5:
                    print("Kode Transfer          : ", kode_transfer)
                    print("Nama Pengirim          : ", nama_pengirim)
                    print("No.Rekening Pengirim   : ", tf)
                    print("Nama Penerima          : ", nama_penerima)
                    print("No.Rekening Penerima   : ", No_Rekening)
                    print("Jumlah Transfer        : ", transfer5)
                    print(59 * '=')
                    break # done
                else:
                    print("Pilihan Anda Tidak Tersedia")
                    continue
            elif konfirmasi1 == 2:
                break
        elif konfirmasi == 2:
            print(59 * '=')
            continue
        else:
            print("Pilihan Anda Tidak Tersedia")
    elif pilih1 == 5:
        print("Terima Kasih Telah Menggunakan ATM Ini")
        print(59*'=')
        break
    else:
        print("Pilihan Anda Tidak Tersedia")

    #all do
