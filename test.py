x = [{'_id': "ObjectId"'65f2cc6d5d27b86671195e5a', 'brukernavn': 'Mia', 'passord': 'meh'}]

k = ["ost", "melk"]
print(k[1])

navn = "Mia"
y = x[0]
print(y["brukernavn"])
print(y["passord"])

if navn == y["brukernavn"]:
    print("navnt ditt er det samme.")