try:
    # Creating a new text file in write mode
    with open("my_file.txt", "w") as file:
        # Writing three lines of text to the file
        file.write("Hello, python!\n")
        file.write("34325\n")
        file.write("Python is interesting!\n")

    # Reading and displaying the contents of the file
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Contents:")
        print(content)

    # Opening the file in append mode
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text
        file.write("Adding some more text\n")
        file.write("67560\n")
        file.write("Appending to the file\n")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied. Check file permissions.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File operation completed.")
