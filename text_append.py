while True:
    file_name = input("Enter your file name: ").strip()
    if file_name.endswith(".txt"):
        while True:
            text_to_add = input("Enter the text you want to add to the file: ").strip()
            if text_to_add != "":
                break
            print("❌ Please enter some text to add!")
        break
    print("❌ Please enter a valid .txt file name (e.g., notes.txt)")

try:
    with open(file_name, "a", encoding="utf-8", newline="") as text_file:
        text_file.write("\n")
        text_file.write(text_to_add)
    print(f"✅ SUCCESS! Your text was added to the end of '{file_name}'.")

except FileNotFoundError:
    print(f"\n❌ Error: The file '{file_name}' was not found. Check the name and try again.")
except PermissionError:
    print(f"\n❌ Error: No access to '{file_name}' — it may be open in another program.")
except UnicodeDecodeError:
    print(f"\n❌ Error: '{file_name}' contains invalid characters. Please use a UTF-8 text file.")

finally:
    print("\nThanks for using the script! 😊")
    
