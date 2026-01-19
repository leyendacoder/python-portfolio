# Python Script: Advanced Duplicate Line Remover + Text Cleaner (Fixed Version)
# Freelance Use Case: Clean and deduplicate messy text files (e.g., customer lists, logs)

# Step 1: Validate filename input
while True:
    file_name = input("Enter your messy text file name (e.g., messy_data.txt): ").strip()
    if file_name.endswith(".txt"):
        break
    print("❌ Please enter a valid .txt file name!")

# Step 2: Create safe output filename
output_file = f"cleaned_deduplicated_{file_name}"

# Step 3: Core logic with full error handling
try:
    with open(file_name, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
        unique_lines = []
        for line in all_lines:  # ✅ Fixed: loop through the list, not the closed file
            cleaned_line = line.strip().replace("  ", " ") + "\n"
            if cleaned_line and cleaned_line not in unique_lines:
                unique_lines.append(cleaned_line)

except FileNotFoundError:
    print(f"\n❌ ERROR: File '{file_name}' not found! Check the name and try again.")
except PermissionError:
    print(f"\n❌ ERROR: No access to '{file_name}' — file may be open in another program!")
except UnicodeDecodeError:
    print(f"\n❌ ERROR: '{file_name}' has invalid characters (use UTF-8 text file).")
else:
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.writelines(unique_lines)

        print(f"\n✅ SUCCESS! Duplicates removed.")
        print(f"📄 Clean file saved as: {output_file}")

    except PermissionError:
        print(f"\n❌ ERROR: Cannot write to '{output_file}' — check folder permissions!")
finally:
    print("\nThank you for using Advanced Duplicate Remover 😊")