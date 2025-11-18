import sys
from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

if sys.version_info >= (3, 13):
    print("Warning: Python version >= 3.13 detected. This module might be unstable.")


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        if scr == 'auto':
            scr = 'auto'

        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        probs = detect_langs(text)
        confidence = probs[0].prob if probs else "N/A"

        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"Lang: {lang}, Confidence: {confidence}"
    except Exception as e:
        return f"Error: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        lang = lang.lower()

        if lang in langs_dict.values():
            for name, code in langs_dict.items():
                if code == lang: return name

        if lang in langs_dict:
            return langs_dict[lang]

        return "Error: Language not found"
    except Exception as e:
        return f"Error: {str(e)}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)

        header = f"{'N':<4} {'Language':<20} {'ISO-639 code':<15} {'Text':<30}"
        line = "-" * 70
        content = f"{header}\n{line}\n"

        count = 1
        for name, code in list(langs_dict.items())[:10]:
            trans_text = ""
            if text:
                try:
                    trans_text = GoogleTranslator(source='auto', target=code).translate(text)
                except:
                    trans_text = "Error"

            content += f"{count:<4} {name.capitalize():<20} {code:<15} {trans_text:<30}\n"
            count += 1

        if out == "file":
            with open("module2_list.txt", "w", encoding="utf-8") as f:
                f.write(content)
            return "Ok"
        else:
            print(content)
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"