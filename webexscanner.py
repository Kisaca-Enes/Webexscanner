import os

def run_scanner(scanner_script):
    print(f"Webex Scanner: Çalıştırılıyor {scanner_script}...")
    os.system(f'python {scanner_script}')

def main():
    print("Webex Scanner")
    print("1: SQL Scanner")
    print("2: IDOR Scanner")
    print("3: CSRF Scanner")
    print("4: XSS Scanner")
    print("5: LFI Scanner")
    print("6: web site bilgi toplama")
    print("7: ssl tls kontrol")
    print("8: htpps http port tarayıcı")
    print("9: udp port tarayıcı")
    print("10: tcp port tarayıcı")
    
    scanners = {
        1: 'sql_scanner.py',
        2: 'idor_scanner.py',
        3: 'csrf_scanner.py',
        4: 'xss_scanner.py',
        5: 'lfi_scanner.py',
        6: 'web_site_bilgi_toplama.py',
        7: 'ssl_tls_kontrol.py',
        8: 'https_http_port_tarayıcı.py',
        9: 'udp_port_tarayıcı.py',
        10: 'tcp_port_tarayıcı',
    }
    
    try:
        choice = int(input("Bir seçim yapın (1-5): "))
        scanner_script = scanners.get(choice)
        
        if scanner_script:
            run_scanner(scanner_script)
        else:
            print("Geçersiz seçim! Lütfen 1, 2, 3, 4 veya 5 girin.")
    except ValueError:
        print("Geçersiz giriş! Lütfen sayı girin.")

if __name__ == "__main__":
    main()