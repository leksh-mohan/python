from collections import Counter
message = input("Enter the string:")
message = message.replace(" ","").lower()
countera = Counter(message)
print ("Repeated characters")
for r in countera:
    if countera[r] > 1:
        print("count of "+r+ " is",countera[r])