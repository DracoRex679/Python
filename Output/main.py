#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("../Names/invited_names.txt") as names_doc:
    names = names_doc.readlines()
print(names)
with open("../Letters/starting_letter.txt") as letter_doc:
    letter = letter_doc.read()
files = []
for name in names:
    files.append(letter.replace("[name]", name.strip()))
length = len(files)
for number in range(length):
    with open(f"ReadyToSend/invite{number+1}.txt", "w+") as invite:
        invite.write(files[number])
#readlines
#string_replace
#strip
