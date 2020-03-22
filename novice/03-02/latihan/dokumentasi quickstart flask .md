# Dokumentasi quickstart Flask 

## Install Flask
```
root@arwanda:~# pip3 install Flask
Collecting Flask
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    100% |████████████████████████████████| 102kB 487kB/s 
Collecting Werkzeug>=0.15 (from Flask)
  Downloading https://files.pythonhosted.org/packages/ba/a5/d6f8a6e71f15364d35678a4ec8a0186f980b3bd2545f40ad51dd26a87fb1/Werkzeug-1.0.0-py2.py3-none-any.whl (298kB)
    100% |████████████████████████████████| 307kB 638kB/s 
Collecting itsdangerous>=0.24 (from Flask)
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from Flask)
  Downloading https://files.pythonhosted.org/packages/27/24/4f35961e5c669e96f6559760042a55b9bcfcdb82b9bdb3c8753dbe042e35/Jinja2-2.11.1-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 820kB/s 
Requirement already satisfied: click>=5.1 in /usr/lib/python3/dist-packages (from Flask) (7.0)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/lib/python3/dist-packages (from Jinja2>=2.10.1->Flask) (1.0)
Installing collected packages: Werkzeug, itsdangerous, Jinja2, Flask
  Found existing installation: Jinja2 2.10
    Not uninstalling jinja2 at /usr/lib/python3/dist-packages, outside environment /usr
    Can't uninstall 'Jinja2'. No files were found to uninstall.
Successfully installed Flask-1.1.1 Jinja2-2.11.1 Werkzeug-1.0.0 itsdangerous-1.1.0
```
Contoh pemanfaatan Flask
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

```
cara menjalankannya :
```
root@arwanda:~/Documents/praxis-academy/novice/03-02/latihan# export FLASK_APP=hello.py
root@arwanda:~/Documents/praxis-academy/novice/03-02/latihan# flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [22/Mar/2020 22:35:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Mar/2020 22:35:39] "GET /favicon.ico HTTP/1.1" 404 -

```
kemudian buka browser dan masukkan http://127.0.0.1:5000/ untuk melihat hello world yang dibuat.

## Kesalahan jika Server tidak jalan :

(pastikan melihat pesan kesalahan)

1. Old Version of Flask

Versi Flask yang lebih tua dari 0,11 digunakan untuk memiliki berbagai cara untuk memulai aplikasi. Singkatnya, perintah flask tidak ada, dan begitu pula flask python -m. Dalam hal ini Anda memiliki dua opsi: upgrade ke versi Flask yang lebih baru atau lihat dokumen Server Pengembangan untuk melihat metode alternatif untuk menjalankan server.

2. Invalid Import Name

Variabel lingkungan FLASK_APP adalah nama modul yang akan diimpor pada flask run. Seandainya modul tersebut salah nama, Anda akan mendapatkan kesalahan impor saat memulai (atau jika debug diaktifkan ketika Anda menavigasi ke aplikasi). Ini akan memberi tahu Anda apa yang coba diimpor dan mengapa gagal.

(pastikan tidak ada kesalahan ketik)

## Debug Mode
Jika kita mengaktifkan dukungan debug, server akan memuat ulang dirinya sendiri pada perubahan kode, dan itu juga akan memberi kira debugger yang bermanfaat jika terjadi kesalahan.

Ingin hanya mencatat kesalahan dan menumpuk jejak? Lihat Kesalahan Aplikasi)

Skrip flask bagus untuk memulai server pengembangan lokal, tetapi Anda harus memulai ulang secara manual setelah setiap perubahan pada kode Anda. Itu tidak terlalu bagus dan Labu dapat melakukan yang lebih baik. Jika Anda mengaktifkan dukungan debug, server akan memuat ulang dirinya sendiri pada perubahan kode, dan itu juga akan memberi Anda debugger yang bermanfaat jika terjadi kesalahan.

Untuk mengaktifkan semua fitur pengembangan (termasuk mode debug) Anda dapat mengekspor variabel lingkungan FLASK_ENV dan mengaturnya untuk pengembangan sebelum menjalankan server:

```
$ export FLASK_ENV=development
$ flask run
```

## Routing

Gunakan dekorator rute () untuk mengikat fungsi ke URL.

```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```
## Variable Rules
```
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```

## Unique URLs / Redirection Behavior
```
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```
URL kanonik untuk titik akhir proyek memiliki garis miring. Mirip dengan folder dalam sistem file. Jika Anda mengakses URL tanpa garis miring, Flask mengarahkan Anda ke URL kanonik dengan garis miring.

## URL Building
Untuk membangun URL ke fungsi tertentu, gunakan fungsi url_for (). Ini menerima nama fungsi sebagai argumen pertama dan sejumlah argumen kata kunci, masing-masing sesuai dengan bagian variabel dari aturan URL. Bagian variabel yang tidak dikenal ditambahkan ke URL sebagai parameter kueri.

Misalnya, di sini kami menggunakan metode test_request_context () untuk mencoba url_for (). test_request_context () memberi tahu Flask untuk berperilaku seolah-olah menangani permintaan bahkan saat kami menggunakan shell Python. Lihat Konteks Lokal.

```
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

## HTTP Methods
## Static Files
## Rendering Templates
## Accessing Request Data
## The Request Object
## File Uploads
## Cookies
## Redirects and Errors
## About Responses
## APIs with JSON
## Sessions
## Message Flashing
## Logging
## Hooking in WSGI Middleware
## Using Flask Extensions
