from flask import Flask, render_template
import random

app = Flask(__name__)

# GÜNÜN SÖZÜ VERİLERİ
sozler = [
    {"soz": "'Her zaman başlamak için geç kaldığını düşüneceksin fakat kalan ömrünün en genç yaşındasın.'", "yazar": "Bilinmiyor"},
    {"soz": "'Sana ait olan, seni bulur.'", "yazar": "Bilinmiyor"},
    {"soz": "'Tüm muhteşem hikayeler iki şekilde başlar. Ya bir insan yolculuğa çıkar ya da şehre bir yabancı gelir.'", "yazar": "Tolstoy"},
    {"soz": "'Yol yüründükçe oluşur.'", "yazar": "Chuang Tzu"},
    {"soz": "'Neyi seversen o olursun sevgi simyadır. Asla yanlış şeyi sevme çünkü seni dönüştürecektir. Hiçbir şey sevgi kadar dönüştürücü değildir. Seni daha yükseklere, doruklara kadar çıkarabilecek bir şeyi sev. Senin ötende bir şeyi sev...'", "yazar": "Osho"},
]

@app.route('/')
def index():
    # Listeden rastgele bir söz seçiyoruz
    secilen_soz = random.choice(sozler)
    
    # Seçilen sözü index.html sayfasına gönderiyoruz
    return render_template('index.html', gunun_sozu=secilen_soz)

if __name__ == '__main__':
    app.run(debug=True)