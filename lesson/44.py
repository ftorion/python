import re
#регулярные вырожения
s = "hello world 2077"
pattern = "hello"
if re.search(pattern, s): # нахождения подстроки
    print("gi")
else:
    print("gg")

ma = re.search(pattern, s)
print(ma.span())  #нахождения строки
print(re.match(pattern, s))

#faindall - ищет все совподения
print(re.findall("w", s))
print(re.split(r" ", s))# разделения  r' ' - сырая строка
pattern = r"[a-z0-9]"
print(re.findall(pattern, s, flags=re.IGNORECASE))
pattern = r"\d+" # r"[0-9]"
s = "hibar@mail.ru"
pattern = r""
print(re.findall(pattern, s, flags=re.IGNORECASE))

def validate_email(email):
    return re.match(r"^.+@(\w+\.){0, 2}[a-z]{2, 6}$", email, flags=re.IGNORECASE)

print(validate_email(s))