# Unit 4 - Q3: File Methods and File-Related Exceptions

filename = input("Enter the name of an existing text file: ")

try:
    file = open(filename, "r", encoding="utf-8")

    print("\nFile name:", file.name)
    print("File mode:", file.mode)

    print("\n----- read() -----")
    print(file.read())
    print("Position after read():", file.tell())

    # Move the file pointer to the beginning.
    file.seek(0)
    print("\nPosition after seek(0):", file.tell())

    print("\n----- readline() -----")
    print(file.readline(), end="")
    print("\nPosition after readline():", file.tell())

    file.seek(0)
    print("\n----- readlines() -----")
    lines = file.readlines()
    print(lines)

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except PermissionError:
    print("Error: Permission denied while accessing the file.")
except OSError as error:
    print("File operation error:", error)
else:
    print("\nFile operations completed successfully.")
finally:
    # Close the file if it was opened successfully.
    if "file" in locals() and not file.closed:
        file.close()
    print("\nFinally block executed.")
    if "file" in locals():
        print("Is file closed?", file.closed)
