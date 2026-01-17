while True:
    file_name = input("Enter your text file name (e.g., notes.txt): ").strip()
    if file_name.endswith(".txt"):
        break
    print("❌ Please enter a valid .txt file name (e.g., notes.txt)")

output_file = f"counted_{file_name}"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
    total_words = len(text.split())
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", ""))

    print("\n📊 Word & Character Count:")
    print(f"Total Words: {total_words}")
    print(f"Total Characters (with spaces): {total_chars}")
    print(f"Total Characters (no spaces): {total_chars_no_spaces}")

except FileNotFoundError:
    print(f"\n❌ Error: The file '{file_name}' was not found. Check the name and try again.")
except PermissionError:
    print(f"\n❌ Error: No access to '{file_name}' — it may be open in another program.")
except UnicodeDecodeError:
    print(f"\n❌ Error: '{file_name}' contains invalid characters. Please use a UTF-8 text file.")
else:
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"File Name: {file_name}\n")
            file.write(f"Total Words: {total_words}\n")
            file.write(f"Total Characters (with spaces): {total_chars}\n")
            file.write(f"Total Characters (no spaces): {total_chars_no_spaces}\n")

        print(f"\n✅ Results saved to '{output_file}'!")
    except PermissionError:
        print(f"\n❌ Error: Cannot write to '{output_file}' — check folder permissions.")
finally:
    print("\nThanks for using the script! 😊")
