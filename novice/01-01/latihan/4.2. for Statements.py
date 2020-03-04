wrd = ['asdafasd', 'geef', 'saddee']
for w in wrd:
    print(w, len(w))
#digunakan untuk menghitung karakter secara bersamaan
#for digunakan untuk perulangan

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
