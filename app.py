import os
import requests # Bu kütüphane veriyi internete göndermemizi sağlar
from flask import Flask, render_template, request

app = Flask(__name__)

# Buradaki 'projem_verileri_123' kısmını kendine özel rastgele bir kelimeyle değiştir
BUCKET_URL = "https://kvdb.io/SizinRastgeleAnahtariniz123/kullanicilar"

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    ad = request.form.get('kullanici_adi')
    
    # Veriyi internetteki depoya gönder (Append mantığıyla ekler)
    # Not: Bu yöntem veriyi bir liste olarak saklamanıza yardımcı olur
    requests.patch(BUCKET_URL, data=f"{ad}, ")
    
    return f"Kayıt başarılı! <a href='/'>Geri dön</a>"

@app.route('/verileri-gor')
def verileri_gor():
    # Depodaki tüm verileri çeker ve ekrana basar
    yanit = requests.get(BUCKET_URL)
    return f"Kaydedilen İsimler: {yanit.text}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
