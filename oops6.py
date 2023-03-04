class animal:
    species="mammal"

class pets():
    attachment="caring" 
class dogs(animal,pets):
    def __str__(self):
        return "bow! bow!"      
miku=dogs()
print(miku)