# This script removes duplicate lines from a text file
# How to use: Make a text file called input.txt, run this script → get clean output.txt

# Open input file and read lines
with open("input.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

# Remove duplicate lines (keep original order)
unique_lines = []
for line in all_lines:
    if line not in unique_lines:
        unique_lines.append(line)

# Save clean lines to new file
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(unique_lines)

# Success message
print("✅ Done! Duplicates removed. Check 'output.txt' in this folder.")
