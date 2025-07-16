with open("characters.txt", "w") as file:
    text = "Hello, World!"  
    for char in text:
        file.write(char + "\n")
print("File created successfully!")
