# Python Script: Advanced Duplicate Remover + Text Cleaner (FINAL PERFECT VERSION)
# Fixed: No duplicates, no blank lines, no extra spaces

def get_valid_filename():
    while True:
        file_name = input("Enter your messy text file name (e.g., messy_data.txt): ").strip()
        if file_name.endswith(".txt"):
            return file_name
        print("❌ Please enter a valid .txt file name!")

def clean_and_remove_duplicates(file_name):
    unique_lines = []
    seen_lines = []  # Track unique lines WITHOUT newlines
    with open(file_name, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
        for line in all_lines:
            cleaned_line = line.strip()
            while "  " in cleaned_line:
                cleaned_line = cleaned_line.replace("  ", " ")
            if cleaned_line and cleaned_line not in seen_lines:
                seen_lines.append(cleaned_line)
                unique_lines.append(cleaned_line + "\n")
    return unique_lines

def save_clean_file(output_file, content):
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(content)

def main():
    file_name = get_valid_filename()
    output_file = f"cleaned_deduplicated_{file_name}"

    try:
        cleaned_content = clean_and_remove_duplicates(file_name)
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