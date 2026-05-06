from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    # Formdan gelen veriyi al
    ad = request.form.get('kullanici_adi')
    
    # Veriyi düzenli bir şekilde TXT dosyasına ekle (append modu)
    with open("veriler.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"Kullanıcı Adı: {ad}\n")
    
    return f"Teşekkürler {ad}, veriniz başarıyla kaydedildi! <a href='/'>Geri dön</a>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)