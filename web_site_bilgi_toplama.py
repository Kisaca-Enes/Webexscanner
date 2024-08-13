import whois

# Kullanıcıdan alan adı girmesini isteme
yaz = input("Sorgulamak istediğin web sitesini yaz: ")

# Alan adı sorgulama
domain = whois.whois(yaz)

# Bilgileri yazdırma
print(f"Alan Adı: {domain.domain_name}")
print(f"Kayıt Şirketi: {domain.registrar}")
print(f"Oluşturulma Tarihi: {domain.creation_date}")
print(f"Son Kullanma Tarihi: {domain.expiration_date}")
