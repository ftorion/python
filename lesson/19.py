"""словари"""
d = {}
pro = {
    "title ": 1,
    "yoi" : "son"
       }
print(pro)
p = dict(title="iphone", price=110)
print(p)
si = [
    ["name", "are"],
    ["man", "rit"]
]
user = dict(si)
print(user)
user = dict.fromkeys(["prise","prise2"], 40)
print(user)
nums = {i:i+1 for i in range(1, 10)}
print(nums)
print(nums[1], nums.get(1))
for key, valus in nums.items():
    print(key, valus)
o = [
    {"t":1, "y":2},
    {"t":1, "y":2},
    {"t":1, "y":2}
]
for o in o:
    print(o["t"], o["y"])