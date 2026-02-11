def remove_extra(file):
    r = open(file, encoding="utf-8")
    text = r.read().replace("\n", "").replace("[", "").replace("]", "")
    r.close()
    r = open(file, "w", encoding="utf-8")
    r.write(text)
    r.close()
    return text
remove_extra("prideprejustice.txt")