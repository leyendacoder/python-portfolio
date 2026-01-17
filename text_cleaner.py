while True:
    file_name = input("Enter your messy text file name (e.g., messy_notes.txt): ").strip()
    if file_name.endswith(".txt"):
        break
    print("❌ Please enter a valid .txt file name (e.g., notes.txt)")

clean_file_name = f"cleaned_{file_name}"

try:
    with open(file_name, "r", encoding="utf-8") as file, open(clean_file_name, "w", encoding="utf-8") as clean:
        for line in file:
            cleaned_line = line.strip()
            cleaned_line = cleaned_line.replace("  ", " ")
            if cleaned_line:
                clean.write(cleaned_line + "\n")
    print(f"\n✅ SUCCESS! File cleaned perfectly!")
    print(f"📄 Original file: {file_name} (unchanged)")
    print(f"📄 Cleaned file saved as: {clean_file_name}")

except FileNotFoundError:
    print(f"\n❌ Error: The file '{file_name}' was not found. Check the name and try again.")
except PermissionError:
    print(f"\n❌ Error: No access to '{file_name}' — it may be open in another program.")
except UnicodeDecodeError:
    print(f"\n❌ Error: '{file_name}' contains invalid characters. Please use a UTF-8 text file.")
finally:
    # This runs ALWAYS, whether there was an error or not
    print("\nThanks for using the script! 😊")
