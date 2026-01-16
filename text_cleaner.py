# Python Script: Text File Cleaner

file_name = input("Enter your messy text file name (e.g., messy_notes.txt): ").strip()
clean_file_name = f"cleaned_{file_name}"

try:
    with open(file_name, "r", encoding="utf-8") as original_file, open(clean_file_name, "w",
                                                                       encoding="utf-8") as clean_file:
        for line in original_file:
            cleaned_line = line.strip()
            cleaned_line = cleaned_line.replace("  ", " ")
            if cleaned_line:
                clean_file.write(cleaned_line + "\n")
    print(f"\n✅ SUCCESS! File cleaned perfectly!")
    print(f"📄 Original file: {file_name} (unchanged)")
    print(f"📄 Cleaned file saved as: {clean_file_name}")
except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file '{file_name}'. Check the name and try again!")
except PermissionError:
    print(f"\n❌ ERROR: No access to '{file_name}' — file may be open/locked by another program!")