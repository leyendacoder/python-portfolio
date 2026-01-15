# Python Script: Text File Appender
# Purpose: Add text to the END of a file (no overwriting) | Creates file if missing

file_name = input("Enter your text file name (e.g., notes.txt): ").strip()
text_to_add = input("Enter the text you want to add to the file: ").strip()

try:
    with open(file_name, "a", encoding="utf-8", newline="") as text_file:
        text_file.write("\n")
        text_file.write(text_to_add)
    print(f"✅ SUCCESS! Your text was added to the end of '{file_name}'.")

except FileNotFoundError:
    print(f"❌ ERROR: Could not find the file '{file_name}'. Check the name and try again!")

except PermissionError:

    print(f"❌ ERROR: No access to '{file_name}' — the file may be open/locked by another program!")
