with open("test.txt") as f:
    content_list = f.readlines()
# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)