import json


def test():
 print("2.....")
 items = ("One", "Two", "Three")
 item = iter(items)

 print(next(item))
 print (next(item))


 x=min(10,100,6,2000)
 y=max(4,400,40,300)

 print(x)
 print(y)


def testTwo():
    print("testTwo .....")

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



test()
testTwo()

