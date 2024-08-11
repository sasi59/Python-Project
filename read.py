
def dict_update():
    file = open("file.txt", "r")
    dictio = {}
    LisT_ID = 1
    for l in file:
        l = l.replace("\n", "")
        dictio.update({LisT_ID: l.split(",")})
        LisT_ID = LisT_ID + 1
    file.close()
    return dictio

def tabular_format():
    file = open("file.txt", "r")
    r = 0
    for l in file:
        print(r+1, "\t\t" + l.replace(",", "\t\t"))
        r = r + 1
        if(r == 5):
            break
    file.close()
