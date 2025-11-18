import sys
from my_package import module2

print(f"--- Docker Container Demo (Python {sys.version.split()[0]}) ---")
print("Container Name: Konovalenko")
print("Project Folder: /Konovalenko")
print("-" * 30)

print("1. Translation (en -> uk):")
print(module2.TransLate("Docker is cool", "en", "uk"))

print("\n2. Language Detection:")
print(module2.LangDetect("Docker це круто", "all"))

print("\n3. Code for 'Ukrainian':")
print(module2.CodeLang("Ukrainian"))

print("\n4. Language List:")
module2.LanguageList("screen", "Hi")