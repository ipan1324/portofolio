from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# Tambahkan secret_key supaya aplikasi bisa menangani session/flash message
app.secret_key = 'kode_rahasia_irfan' 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

# GABUNGKAN MENJADI SATU FUNGSI SAJA SEPERTI INI:
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Ambil data dari form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Muncul di terminal VS Code sebagai bukti data masuk
        print(f"DEBUG: Pesan dari {name} ({email}): {message}")
        
        # Kirim notifikasi sukses (Flash Message)
        flash(f"Terima kasih {name}, pesan kamu sudah terkirim!", "success")
        return redirect(url_for('contact'))
        
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)