# Dependency Injection: Python

Dependency Injection(ID ) adalah teknik rekayasa software untuk menentukan ketergantungan antar objek. Pada dasarnya, proses penyediaan resource yang membutuhkan potongan kode tertentu. resource yang dibutuhkan disebut ketergantungan.
Ada berbagai kelas dan objek yang didefinisikan saat menulis kode. Sebagian besar waktu, kelas-kelas ini bergantung pada kelas-kelas lain untuk memenuhi tujuan yang dimaksudkan. Kelas-kelas ini, atau Komponen kata yang lebih baik digunakan, tahu resource yang dibutuhkan dan cara mendapatkannya. DI menangani mendefinisikan resource dependen ini dan menyediakan cara untuk membuat instantiate atau membuatnya secara eksternal. Dependency Container digunakan untuk menerapkan perilaku ini dan memegang peta dependensi untuk komponen.

Jika objek A depends pada objek B, objek A tidak harus membuat import objek B. 


Keuntungan mengunakan Dependency Injection didalam kode : 

 -  Fleksibilitas komponen yang dapat dikonfigurasi

- Testing made easy

- Kompleksitas modul dalam code berkurang, peningkatan penggunaan kembali modul.

- Meminimalkan dependencies - Karena dependencies didefinisikan dengan jelas, lebih mudah untuk menghilangkan / mengurangi dependencies yang tidak perlu.


### Sebelum menggunakan DI kita harus install injektor dan dependency injector
```
pip3 install injector
```
*menggunakan pip3 apabila menggunakan pthon versi 3*

```
pip3 install dependency_injector
```
contoh penggunaannya

Membuat file :
- email_client.py

```
class EmailClient(object):
    
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
        
    def connect(self, config):
        # Implement function here
pass
```

- email_reader.py

```
class EmailReader(object):
    
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e
            
    def read(self):
        # Implement function here
pass
```

- containers.py

```
from dependency_injector import providers, containers
from email_client import EmailClient
from email_reader import EmailReader

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton(EmailClient, Configs.config)
    # other clients
    
class Readers(containers.DeclarativeContainer):
    email_reader = providers.Factory(EmailReader, client=Clients.email_client)
# other readers
```
- main.py
```
from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_reader()
print email_reader.read()
```

*Sumber : https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce*




