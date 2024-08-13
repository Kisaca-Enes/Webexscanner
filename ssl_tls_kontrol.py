import requests

def check_ssl_tls(url):
    try:
        # HTTPS isteği yapmayı dene
        response = requests.get(url, timeout=5)
        # İstek başarılı ise SSL/TLS mevcut
        return response.url.startswith("https://")
    except requests.exceptions.SSLError:
        # SSL/TLS hatası oluşursa
        return False
    except requests.exceptions.RequestException as e:
        # Diğer istekte hata durumları
        print(f"İstek hatası: {e}")
        return False

# Kullanıcıdan URL al
url = input("SSL/TLS kontrolü yapmak istediğiniz web sitesini yazın : ")

# SSL/TLS var mı yok mu kontrol et
if check_ssl_tls(url):
    print(f"{url} üzerinde SSL/TLS mevcut.")
else:
    print(f"{url} üzerinde SSL/TLS mevcut değil.")