def get_valid_filename():
    while True:
        file_name = input("Enter your messy text file name (e.g., messy_notes.txt): ").strip()
        if file_name.endswith(".txt"):
            return file_name
        print("❌ Please enter a valid .txt file name!")

def clean(file_name):
    unique_lines = []
    with open(file_name, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
        for line in all_lines:
            clean_line = line.strip()
            while "  " in clean_line:
                clean_line = clean_line.replace("  ", " ")
            if clean_line:
                unique_lines.append(clean_line + "\n")
    return unique_lines

def save_clean_file(output_file, content):
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(content)

def main():
    file_name = get_valid_filename()
    output_file = f"cleaned_{file_name}"

    try:
        cleaned_content = clean(file_name)
        save_clean_file(output_file, cleaned_content)

        print(f"\n✅ SUCCESS! Duplicates removed & text cleaned (PERFECT OUTPUT!)")
        print(f"📄 Original file: {file_name} (UNCHANGED)")
        print(f"📄 Clean file saved as: {output_file}")

    except FileNotFoundError:
        print(f"\n❌ ERROR: File '{file_name}' not found! Check the name and try again.")
    except PermissionError:
        print(f"\n❌ ERROR: No access to '{file_name}' — file may be open in another program!")
    except UnicodeDecodeError:
        print(f"\n❌ ERROR: '{file_name}' has invalid characters (use UTF-8 text file).")
    finally:
        print("\nThank you for using Advanced Duplicate Remover 😊")

if __name__ == "__main__":
    main()
