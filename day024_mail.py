PLACEHOLDER = "[name]"

with open("./100days/day024_names.txt") as names_file:
    names = names_file.readlines()

with open("./100days/day024_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open (f"./100days/letter_to_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)