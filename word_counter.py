# This script counts words and characters in a text file
# How to use: Run script, enter filename → get instant count

file_name = input("Enter your text file name (e.g., essay.txt): ").strip()

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    # Calculate counts
    total_words = len(text.split())
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", ""))

    # Show results
    print("\n📊 Word & Character Count:")
    print(f"Total Words: {total_words}")
    print(f"Total Characters (with spaces): {total_chars}")
    print(f"Total Characters (no spaces): {total_chars_no_spaces}")

    # Save results to a file
    with open("word_count_results.txt", "w", encoding="utf-8") as file:
        file.write(f"File Name: {file_name}\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Total Characters (with spaces): {total_chars}\n")
        file.write(f"Total Characters (no spaces): {total_chars_no_spaces}\n")

    print("\n✅ Results saved to 'word_count_results.txt'!")

except FileNotFoundError:
    print(f"❌ Error: File '{file_name}' not found!")
