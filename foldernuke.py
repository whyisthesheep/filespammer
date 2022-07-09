nam = "list.txt"
listm = open(nam)
for item in listm:
    item = item.replace('\n', " ")
    open(item, "a")
