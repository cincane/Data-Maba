# Ahmad Dhani Difiera
# NPM : 222102030
# Program Data Maba

import re
emailre = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
maba = []
while True:
    prompt = input(f'({len(maba)} data) Command: ').lower().strip()
    # prompt = prompt.lower() mengubah ke huruf kecil
    # prompt = prompt.strip() mengabaikan spasi di depan atau di belakang
    if not prompt:
        print(' Available commands: add, show, view, and exit')
    elif prompt in ('exit', "quit"):
        break
    elif prompt == 'add':
        datamaba = {}
        while True:
            datamaba['name'] = input(' Name: ').strip()
            if datamaba['name'] != "":
                break
        # jenis kelamin
        while True:
            datamaba['jenis kelamin'] = input(' Jenis Kelamin: ').strip()
            if datamaba['jenis kelamin'] not in ('laki laki', 'perempuan'):
                print("Invalid input data")
                print("Jenis kelamin: laki laki atau perempuan")
                continue
            if datamaba['jenis kelamin'] != '':
                break
        # prodi
        while True:
            datamaba['prodi'] = input(' Prodi: ').strip()
            if datamaba['prodi'] != '':
                break
        # asal sekolah
        while True:
            datamaba['asal sekolah'] = input(' Asal Sekolah: ').strip()
            if datamaba['asal sekolah'] != '':
                break
        # npm
        while True:
            datamaba['npm'] = input(' NPM: ').strip()
            if datamaba['npm'][0] != '2' or not datamaba['npm'].isdigit():
                print('Invalid NPM number format')
                continue
            if datamaba['npm'] != '':
                break
        datamaba['phones'] = []
        # first phone
        while True:
            phone = input(' Phone: ').strip()
            if phone[0] != '0' or not phone.isdigit():  # bernilai true jika semua digit
                print("Invalid phone number format")
                continue
            if phone != "":
                break
        datamaba['phones'].append(phone)
        # next phone (jika ada)
        while True:
            phone = input(' Phone: ').strip()
            if not phone:
                break
            if phone[0] != '0' or not phone.isdigit():  # bernilai true jika semua digit
                print("Invalid phone number format")
                continue
            datamaba['phones'].append(phone)
        while True:
            datamaba['email'] = input(
                ' E-mail: ').strip() or None  # atau kosong
            if datamaba['email'] is None:
                break
            if re.fullmatch(emailre, datamaba['email']):
                break
            print('invalid email format')
        datamaba['address'] = input(
            ' Address: ').strip() or None  # atau kosong
        maba.append(datamaba)
    elif prompt == 'show':
        if not maba:
            print("Data maba is still empty")
            continue
        for i, datamaba in enumerate(maba):
            phones = ','.join(datamaba['phones'])
            print(f" {i+1}. {datamaba['name']}: {phones}")
    elif prompt == 'view':
        while True:
            no = input(' Data #: ').strip()
            if no.isdigit():
                no = int(no)
                break
        if no < 1 or no > len(maba):
            print("There is no such data")
            continue
        datamaba = maba[no - 1]
        print(f" Name: {datamaba['name']}")
        print(f" Jenis Kelamin: {datamaba['jenis kelamin']}")
        print(f" Prodi: {datamaba['prodi']}")
        print(f" Asal Sekolah: {datamaba['asal sekolah']}")
        print(f" NPM: {datamaba['npm']}")
        print(f" Phones: {','.join(datamaba['phones'])}")
        print(f" E-mail: {datamaba['email']}")
        print(f" Address: {datamaba['address']}")
    elif prompt == "delete":
        while True:
            no = input(' Data #: ').strip()
            if no.isdigit():
                no = int(no)
                break
        if no < 1 or no > len(maba):
            print("There is no such data")
            continue
        del maba[no - 1]
    elif prompt == 'edit':
        while True:
            no = input(' Data #: ').strip()
            if no.isdigit():
                no = int(no)
                break
        if no < 1 or no > len(maba):
            print(' There is no such data')
            continue
        datamaba = maba[no - 1]
        # edit name
        name = input(f" Name ({datamaba['name']}): ").strip()
        if name != '':
            datamaba['name'] = name
        # edit jenis kelamin
        while True:
            jenis_kelamin = input(
                f"Jenis kelamin ({datamaba['jenis kelamin']}): ").strip()
            if jenis_kelamin == '':
                break
            if jenis_kelamin not in ('laki laki', 'perempuan'):
                print("Invalid input data")
                print("Jenis kelamin: laki laki atau perempuan")
                continue
            datamaba['jenis kelamin'] = jenis_kelamin
        prodi = input(f"Prodi ({datamaba['prodi']}): ").strip()
        if prodi != '':
            datamaba['prodi'] = prodi
        # edit asal sekolah
        asal_sekolah = input(
            f"Asal sekolah ({datamaba['asal sekolah']}): ").strip()
        if asal_sekolah != '':
            datamaba['asal sekolah'] = asal_sekolah
        # edit NPM
        while True:
            npm = input(f"NPM ({datamaba['npm']}): ").strip()
            if npm == '':
                break
            if not (npm[0] == '2' and npm.isdigit()):
                print("Invalid NPM number format")
                continue
            datamaba['npm'] = npm

        i = 0
        while True:
            if i >= len(datamaba['phones']):
                break
            phone = input(f" Phone ({datamaba['phones'][i]}): ").strip()
            if phone == '':
                i += 1
                continue
            if phone == '-':
                del datamaba['phones'][i]
                continue
            if not (phone[0] == '0' and phone.isdigit()):
                print(' Invalid input data')
                continue
            datamaba['phones'][i] = phone
            i += 1
        if not datamaba['phones']:
            while True:
                phone = input(' Phone: ').strip()
                if not (phone[0] == '0' and phone.isdigit()):
                    print(' Invalid input data')
                    continue
                if phone != '':
                    break
            datamaba['phones'].append(phone)
        while True:
            phone = input(' Phone: ').strip()
            if not phone:
                break
            if not (phone[0] == '0' and phone.isdigit()):
                print(' Invalid input data')
                continue
            datamaba['phones'].append(phone)

        while True:
            email = input(f" E-mail ({datamaba['email']}): ").strip() or None
            if email is None:
                break
            if email == '-':
                datamaba['email'] = None
                break
            if re.fullmatch(emailre, email):
                datamaba['email'] = email
                break
            print(' Invalid input data')
        address = input(f" Address ({datamaba['address']}): ").strip() or None
        if address == '-':
            datamaba['address'] = None
        elif address is not None:
            datamaba['address'] = address
    else:
        print(' Command is not recognized')
