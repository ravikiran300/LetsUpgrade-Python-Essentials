#Make a Lambda function for capitalizing the whole sentence passed using arguments.
#And map all the sentences in the List, with the lambda functions

arr = []
st = ["hey this is ravikiran","I am in JB NAGAR(chakkala",""]
for x in st:
    arr.append(x.upper())

print(arr)

