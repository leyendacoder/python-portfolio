# Python Script: Find and Replace Text in File
# Skills: String Manipulation + File Handling + Input Validation + Error Handling
# Freelance Use Case: Fix typos, update text, or clean data in text files (HIGH DEMAND!)

while True:
    file_name = input("Enter your text file name (e.g., input.txt): ").strip()
    if file_name.endswith(".txt"):
        while True:
            find = input("Enter the text you want to find: ").strip()
            if find != "":
                replace = input("Enter the new text you want to replace: ").strip()
                break
            print("❌ Please enter a valid text to find!")
        break
    print("❌ Please enter a valid .txt file name!")

output_file = f"updated_{file_name}"

try:
    with open(file_name, "r", encoding="utf-8") as original_file, open(output_file, "w", encoding="utf-8") as updated_file:
        read_file = original_file.read()
        if find in read_file:
            replaced = read_file.replace(find, replace)
            updated_file.write(replaced)
            print(f"\n✅ SUCCESS! Text replacement completed!")
            print(f"📄 Original file: {file_name} (UNCHANGED)")
            print(f"📄 Updated file saved as: {output_file}")
        else:
            print(f"❌ The text '{find}' wasn't found in the file — no changes made.")

except FileNotFoundError:
    print(f"\n❌ ERROR: The file '{file_name}' was not found! Check the name and try again.")
except PermissionError:
    print(f"\n❌ ERROR: No access to '{file_name}' — file may be open in another program!")
except UnicodeDecodeError:
    print(f"\n❌ ERROR: '{file_name}' has invalid characters (use UTF-8 text file).")
finally:
    print("\nThank you for using Find & Replace Script 😊")