import os

def main():
    path = "/Users/benjaminmartell/Dropbox/skolan/Python/"
    search = input("Enter a value to search for in the file: ")
    for file in directory(path):
        if find(file, search) >= 1:
            print("your search", search,"was found", find(file, search), "times, in", file)


def directory(path):

    folder = os.fsencode(path)
    filenames = []

    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.txt', '.py')):
            filenames.append(filename)

    return filenames


def find(file, search):

    data = ""
    with open(file, 'r') as f:
        line = f.readline()
        while line != "":
            if search in line:
                found = True
                data += line
            line = f.readline()

        return data.count(search)


main()