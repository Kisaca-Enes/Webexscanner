import requests

# Kullanıcıdan seçenek al
secenek = input('Seçenek seç: 1: seçtiğin portu tara, 2: popüler portları tara: ')

if secenek == '1':
    # Port tarama
    web_sitesi = input('Web sitesi yazın: ')
    port = input('Port yazın: ')

    try:
        r = requests.get(f'http://{web_sitesi}:{port}')
        if r.status_code == 200:
            print('Port açık')
        else:
            print('Port açık değil')
    except requests.ConnectionError:
        print('Bağlantı hatası, portu kontrol edemedik.')

elif secenek == '2':
    # Popüler portları tarama
    web_sitesi = input('Web sitesi yazın: ')
    portlar = ['80', '443', '21', '22', '25', '110', '143']  # Popüler portlar

    for port in portlar:
        try:
            r = requests.get(f'http://{web_sitesi}:{port}')
            if r.status_code == 200:
                print(f'Port {port} açık')
            else:
                print(f'Port {port} açık değil')
        except requests.ConnectionError:
            print(f'Port {port} için bağlantı hatası')

else:
    print('Geçersiz seçenek')
