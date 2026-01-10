# This script changes text file to UPPERCASE / LOWERCASE
# How to use: Run script, type choice + filename → get converted file

# Ask user for what they want to do
user_choice = input("Type 'upper' for uppercase, 'lower' for lowercase: ").strip()
file_name = input("Enter your text file name (e.g., notes.txt): ").strip()

# Process the file (no crashes if file missing!)
try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    # Change case
    if user_choice == "upper":
        new_text = text.upper()
        save_name = "uppercase_" + file_name
    elif user_choice == "lower":
        new_text = text.lower()
        save_name = "lowercase_" + file_name
    else:
        print("❌ Error: Type only 'upper' or 'lower'")
        new_text = ""
        save_name = ""

    # Save the result
    if new_text:
        with open(save_name, "w", encoding="utf-8") as file:
            file.write(new_text)
        print(f"✅ Done! Check file: {save_name}")

except FileNotFoundError:
    print(f"❌ Error: File '{file_name}' not found in this folder!")
