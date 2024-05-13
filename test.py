import random
print("Hello")

dict = { "key-1" : "value1",
        "key-2" : "value2"
}

print (dict["key-1"]+" "+ dict["key-2"])

list = [1,5,3]
for nombre in list:
    print(nombre)


def randomSomme(maximum):

    v1 = random.randint(0, maximum)
    print(v1)
    v2 = random.randint(0, maximum)
    print(v2)
    somme = v1+v2
    return somme


print(randomSomme(200))

mylist = ["pomme","melon","kiwi","banane"]
print(random.choices(mylist, weights=[10,1,1,1], k=3))

def aleatoire (booleen, liste, min, max) :
    if booleen == True :
        return random.choice(liste)
    else :
        return random.randint(min, max)
print (aleatoire(False,mylist,0,200))