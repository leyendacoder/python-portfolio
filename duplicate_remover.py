# Python Script: Advanced Duplicate Line Remover (Day 3 Upgrade)
# Skill used: Error Handling + Input Validation + File Handling
# Freelance Use Case: Remove duplicate lines from text files, safely and reliably

while True:
    file_name = input("Enter your input file name (e.g., input.txt): ").strip()
    # Validate: Ensure the file is a text file
    if file_name.endswith(".txt"):
        break
    print("❌ Please enter a valid .txt file name (e.g., notes.txt)")

output_file = f"cleaned_{file_name}"

# Step 2: Core logic with FULL error handling
try:
    with open(file_name, "r", encoding="utf-8") as infile:
        all_lines = infile.readlines()

    # Remove duplicates while preserving order
    unique_lines = []
    for line in all_lines:
        stripped_line = line.strip() + "\n"  # Keep line breaks
        if stripped_line not in unique_lines:
            unique_lines.append(stripped_line)

except FileNotFoundError:
    print(f"\n❌ Error: The file '{file_name}' was not found. Check the name and try again.")
except PermissionError:
    print(f"\n❌ Error: No access to '{file_name}' — it may be open in another program.")
except UnicodeDecodeError:
    print(f"\n❌ Error: '{file_name}' contains invalid characters. Please use a UTF-8 text file.")
else:
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.writelines(unique_lines)
        print(f"\n✅ Success! Duplicates removed.")
        print(f"📄 Clean file saved as: {output_file}")
    except PermissionError:
        print(f"\n❌ Error: Cannot write to '{output_file}' — check folder permissions.")
finally:
    print("\nThanks for using the script! 😊")
