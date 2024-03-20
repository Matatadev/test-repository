# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here with some numbers: 987\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.\n")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of 'my_file.txt':\n", contents)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File reading process completed.\n")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending a new line here\n")
            file.write("More data to append\n")
            file.write("Last line for now\n")
        print("Data appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Permission denied. Unable to append data to file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File appending process completed.\n")


def main():
    create_file()
    read_file()
    append_file()


if __name__ == "__main__":
    main()
