pro = {
    "title": 1,
    "yoi" : "son"
       }
print(pro.items())
print(pro.keys())
print(pro.pop("title", "NO"))
print(pro.setdefault("title"))
pro.update({"test": "iwiiw"})
print(pro)
print(pro.values())
