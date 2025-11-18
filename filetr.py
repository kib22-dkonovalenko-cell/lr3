import json
import os
import re
import importlib


def main():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error reading config: {e}")
        return

    # Зчитування параметрів
    filename = config.get('text_file')
    target_lang = config.get('target_language')
    module_name = config.get('module')
    output_type = config.get('output')
    max_chars = config.get('max_characters')
    max_words = config.get('max_words')
    max_sents = config.get('max_sentences')

    # Перевірка файлу
    if not os.path.exists(filename):
        print("Error: File not found")
        return

    # Динамічний імпорт модулю
    try:
        current_module = importlib.import_module(f"my_package.{module_name}")
    except ImportError:
        print(f"Error: Module {module_name} not found")
        return

    # Статистика файлу
    with open(filename, 'r', encoding='utf-8') as f:
        full_text = f.read()

    chars_count = len(full_text)
    words_count = len(full_text.split())
    sents_count = len(re.split(r'[.!?]+', full_text)) - 1

    lang = current_module.LangDetect(full_text, "lang")

    print(f"File: {filename}")
    print(f"Size: {chars_count} chars, {words_count} words, {sents_count} sentences")
    print(f"Detected Language: {lang}")
    print("-" * 20)

    # Обробка лімітів (читаємо доки не виконається умова)
    process_text = full_text

    # Обрізка по символах
    if max_chars and len(process_text) > max_chars:
        process_text = process_text[:max_chars]

    # Обрізка по словах
    words = process_text.split()
    if max_words and len(words) > max_words:
        process_text = " ".join(words[:max_words])

    # Обрізка по реченнях
    if max_sents:
        sentences = re.split(r'([.!?]+)', process_text)
        count = 0
        new_text = ""
        for part in sentences:
            new_text += part
            if re.match(r'[.!?]+', part):
                count += 1
            if count >= max_sents:
                process_text = new_text
                break

    # Переклад
    print(f"Translating {len(process_text)} characters...")
    translated = current_module.TransLate(process_text, lang, target_lang)

    # Вивід результату
    if output_type == "screen":
        print(f"Target Language: {target_lang}")
        print(f"Used Module: {module_name}")
        print("-" * 20)
        print(translated)

    elif output_type == "file":
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_{target_lang}.txt"
        try:
            with open(new_filename, 'w', encoding='utf-8') as f:
                f.write(translated)
            print("Ok")
            print(f"Saved to {new_filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("Error: Invalid output type")


if __name__ == "__main__":
    main()