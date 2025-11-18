from googletrans import Translator, LANGUAGES

translator = Translator()


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        res = translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        return f"Error: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        res = translator.detect(text)
        if set == "lang":
            return res.lang
        elif set == "confidence":
            return str(res.confidence)
        else:
            return f"Lang: {res.lang}, Confidence: {res.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"


def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Error: Language not found"


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header = f"{'N':<4} {'ISO-639 code':<15} {'Language':<20} {'Text':<30}\n"
        line = "-" * 70 + "\n"
        content = header + line

        count = 1
        for code, name in list(LANGUAGES.items())[:15]:  # Обмежимо список для демо
            trans_text = ""
            if text:
                try:
                    trans_text = translator.translate(text, dest=code).text
                except:
                    trans_text = "Error"
            content += f"{count:<4} {code:<15} {name:<20} {trans_text:<30}\n"
            count += 1

        if out == "file":
            with open("module1_list.txt", "w", encoding="utf-8") as f:
                f.write(content)
        else:
            print(content)
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"