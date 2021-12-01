courses = ['Php', 'Python', 'Java']
with open('test.txt', "w") as myfile:
    for c in courses:
        myfile.write("%s\n" % c)

content = open('test.txt')
print(content.read())
