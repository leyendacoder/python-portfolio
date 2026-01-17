while True:
    file_name = input("Enter your text file name (e.g., notes.txt): ").strip()
    if file_name.endswith(".txt"):
        while True:
            user_choice = input("Type 'upper' for uppercase, 'lower' for lowercase: ").strip()
            if user_choice == "upper" or user_choice == "lower":
                break
            print("❌ Error: Please type only 'upper' or 'lower'")
        break
    print("❌ Please enter a valid .txt file name (e.g., notes.txt)")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
        if user_choice == "upper":
            new_text = text.upper()
            save_name = "uppercase_" + file_name
        elif user_choice == "lower":
            new_text = text.lower()
            save_name = "lowercase_" + file_name

except FileNotFoundError:
    print(f"\n❌ Error: The file '{file_name}' was not found. Check the name and try again.")
except PermissionError:
    print(f"\n❌ Error: No access to '{file_name}' — it may be open in another program.")
except UnicodeDecodeError:
    print(f"\n❌ Error: '{file_name}' contains invalid characters. Please use a UTF-8 text file.")
else:
    try:
        with open(save_name, "w", encoding="utf-8") as file:
            file.write(new_text)
            print(f"\n✅ Success! The job has done successfully.")
            print(f"📄 Clean file saved as: {save_name}")
    except PermissionError:
        print(f"\n❌ Error: Cannot write to '{save_name}' — check folder permissions.")
finally:
    print("\nThanks for using the script! 😊")
