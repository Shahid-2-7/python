f = {
    "name" : "Shahid",
    "age" : 13,
    "adress" : "Kayalpatnam"

}
print(f["name"])
print(f["age"])
print(f["adress"])
f["name"] = "Peer Mohamed Shahid"
f.update({"age" : 15})
f.pop("adress")
print(f)
print(f.keys())
print(f.values())
print(f["name"])