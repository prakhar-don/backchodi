class sample:
    attribute="abc"

damn=sample()
damn.attribute="ok"
yep=sample()
print(damn.attribute)
print(sample.attribute) 
print(yep.attribute)   