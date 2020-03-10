#01 First-Class Functions
def greeting():
    print("Hello World")

greeting()

#02
greeting.lang = "English"
print(greeting.lang)

#03 Assigning Functions to Variables
def square(x):
    return x * x
square(5)

#04
foo = square
foo(6)

#05 Passing Functions as Parameters

def formalGreeting():
    print ("How are you?")
def casualGreeting():
    print ("What's up")
def greet(g):
    if g == 'formal':
        formalGreeting()
    elif g == 'casual':
        casualGreeting()
    else :
        print("Nothing!")

greet('a')

#06 Higher-order function
# Without

arr1 = [1,2,4]
arr2 = []

for i in range(len(arr1)):
    arr2.append(arr1[i]*2)

arr2

#07 With Higher-order function map
def Arr2(a):
    return a *2
arr1 = [1,2,3]
arr2 = map(Arr2, arr1)
print(list(arr2))

#--------------------------------------------
arr1 = [1,2,3]
arr2 = list(map(lambda arr1 : arr1*2, arr1))
arr2

#08 Array.prototype.map 
# Without Higher-order function
birthYear = [1975, 1997, 2002, 1995, 1985]
ages = []

for i in range(5):
    age = 2018 - birthYear[i]
    ages.append(age)
print(ages)

#09 With Higher-order function map
birthYear = [1975, 1997, 2002, 1995, 1985]
ages = list(map(lambda bitthYear: 2018-bitthYear, birthYear))
ages

#10 Array.prototype.filter
persons = [
    {'name': 'Peter', 'age': 16},
    {'name': 'Mark', 'age': 18},
    {'name': 'John', 'age': 27},
    {'name': 'Jane', 'age': 14},
    {'name': 'Tony', 'age': 24},
    ]
fullAge = []
for i in range(len(persons)):
    panggil = persons[i].get("age")
    if panggil >= 18:
        fullAge.append(persons[i])
#fullAge.append(persons[i].get("name")) ==> jika hanya nama saja
print(fullAge)


#gagal

#11 Filter
# Pass

#12 Array.prototype.reduce
arr=[5,7,1,8,9]
print(sum(arr))

#without

arr = [5,7,1,8,9]
jumlah = 0
for i in range(len(arr)):
    jumlah = jumlah + arr[i]
jumlah

#13 Creating Our own Higher-Order Function => belum jadi
strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'c']
newArray = []
def aaa(newArray):
    for i in range(len(strArray)):
        newArray.append(len(strArray[i]))
aaa(newArray)
newArray
