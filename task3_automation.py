import os
import shutil
import re
import requests

# CodeAlpha Internship - Task 3
# Automation with Python Scripts

print("=" * 45)
print("     PYTHON TASK AUTOMATION TOOL")
print("=" * 45)

# 1. Move all JPG files into a new folder
source_folder = "input_files"
destination_folder = "JPG_Images"

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

moved_count = 0

print("\n1. ORGANIZING JPG FILES")

for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg")):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(
            destination_folder, filename
        )

        if os.path.isfile(source_path):
            if os.path.exists(destination_path):
                print(f"Skipped duplicate file: {filename}")
                continue

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

print(f"Total images moved: {moved_count}")

# 2. Extract email addresses from a text file
print("\n2. EXTRACTING EMAIL ADDRESSES")

text_file = "emails.txt"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

try:
    with open(text_file, "r", encoding="utf-8") as file:
        content = file.read()

    emails = sorted(set(re.findall(email_pattern, content)))

    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

    with open("extracted_emails.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(emails))

    print("Saved results to extracted_emails.txt")

except FileNotFoundError:
    print("emails.txt not found. Please create the file first.")

# 3. Demonstrate an HTTP request using requests
print("\n3. HTTP REQUEST DEMO")

try:
    response = requests.get(
        "https://example.com",
        timeout=10
    )
    print("Website request successful!")
    print("HTTP Status Code:", response.status_code)

except requests.RequestException:
    print("Website request failed. Check your internet connection.")

print("\nAutomation completed!")
print("=" * 45)