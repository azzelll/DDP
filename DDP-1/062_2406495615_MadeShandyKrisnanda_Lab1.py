print(">>==========================<<")
print("||                     	   ||")
print("|| Welcome to Interrogation||")
print("||                     	   ||")
print(">>==========================<<")
print("")

jawaban_interogasi = input("Mulai Interogasi(Y/N)?")
while jawaban_interogasi not in ('n', 'N', 'no', 'No', 'NO', 'y', 'Y', 'yes', 'Yes', 'YES'):
    print('')
    print('input tidak valid')
    jawaban_interogasi = input("Mulai Interogasi(Y/N)?")
while jawaban_interogasi in ('y', 'Y', 'yes', 'Yes', 'YES'):
    print("Mari kita mulai interogasi")
    print(' ')
    is_stop = False
    while is_stop == False:
        nama = input("Siapa namamu?")
        npm = input("Berapa nomor NPM mu?")
        digit_npm = 0
        for i in npm:
            digit_npm+=1
        if npm.isdigit()!= True:
            print("NPM harus berupa angka!")
            print('------------------------------')
            print(' ')
            continue
        elif int(digit_npm) != 10:
            print("NPM harus sepanjang 10 digits!")
            print('------------------------------')
            print(' ')
            continue
        elif npm.isdigit() == True and int(digit_npm) == 10:
            motif = input("Apakah kamu punya motif (Y/N)?")
            if motif in ('y', 'Y', 'yes', 'Yes', 'YES'):
                jenis_motif = input("Apa motif kamu tadi?")
                alibi = input("Apakah kamu punya alibi (Y/N)?")
                if alibi in ('y', 'Y', 'yes', 'Yes', 'YES'):
                    jenis_alibi = input("Apa alibi kamu?")
                    print(' ')
                    print('{} dengan NPM {} memiliki motif {} dan memiliki alibi {}'.format(nama,npm,jenis_motif, jenis_alibi))
                    print('{} lumayan mencurigakan nih...'.format(nama))
                    print('------------------------------')
                    print(' ')
                elif alibi in ('n', 'N', 'no', 'No', 'NO'):
                    print(' ')
                    print('{} dengan NPM {} memiliki motif {} tapi tidak memiliki alibi'.format(nama,npm, jenis_motif))
                    print('Wah, {} mencurigakan nihh >:('.format(nama))
                    print('------------------------------')
                    print(' ')
                else:
                    print('seseorang harus punya alibi atau tidak sama sekali')
                    print('------------------------------')
                    print(' ')
                    continue
            elif motif in ('n', 'N', 'no', 'No', 'NO'):
                motif = "tidak memiliki motif"
                alibi = input("Apakah kamu punya alibi (Y/N)?")
                if alibi in ('y', 'Y', 'yes', 'Yes', 'YES'):
                    jenis_alibi = input("Apa alibi kamu?")
                    print(' ')
                    print('{} dengan NPM {} tidak memiliki motif dan memiliki alibi {}'.format(nama,npm, jenis_alibi))
                    print('{} tidak terlalu mencurigakan sih'.format(nama))
                    print('------------------------------')
                    print(' ')
                elif alibi in ('n', 'N', 'no', 'No', 'NO'):
                    print(' ')
                    print('{} dengan NPM {} tidak memiliki motif maupun alibi'.format(nama,npm))
                    print('{} lumayan mencurigakan nih...'.format(nama))
                    print('------------------------------')
                    print(' ')
                else:
                    print('seseorang harus punya alibi atau tidak sama sekali')
                    print('------------------------------')
                    print(' ')
                    continue
            else:
                print("seseorang harus punya motif atau tidak sama sekali")
                print('------------------------------')
                print(' ')
                continue
            jawaban_interogasi = input("Lanjut interogasi (Y/N))?")
            if jawaban_interogasi in ('y', 'Y', 'yes', 'Yes', 'YES'):
                print('------------------------------')
                print(' ')
                continue
            elif jawaban_interogasi in ('n', 'N', 'no', 'No', 'NO'):
                print('Interogasi telah selesai')
                print('')
                print('>>==========================<<')
                print('||                     	    ||')
                print('|| Ending the Interrogation ||')
                print('||                     	    ||')
                print('>>==========================<<')
                break
            else:
                print('input tidak valid')
                continue