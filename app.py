from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    produk_list = [
        {
            "nama": "Tinta Imajinasi: Buku Mewarnai Digital",
            "deskripsi": "Buku mewarnai digital untuk melatih kreativitas anak",
            "harga": "Rp50.000"
        },
        {
            "nama": "Template Konten Kreatif",
            "deskripsi": "Template desain sosial media siap pakai",
            "harga": "Rp90.000"
        },
        {
            "nama": "E-book Kreativitas Digital",
            "deskripsi": "Panduan mengembangkan ide kreatif",
            "harga": "Rp5.000"
        }
    ]
    return render_template('produk.html', produk=produk_list)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        return render_template('hasil.html', nama=nama, email=email)
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
