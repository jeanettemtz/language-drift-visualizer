from googletrans import Translator

translator = Translator()

# Sequence of languages to drift through
languages = ['de', 'es', 'fr', 'en']  # German → Spanish → French → back to English

def drift_text(text, langs):
    drifted = [text]
    current_text = text
    for lang in langs:
        translated = translator.translate(current_text, dest=lang)
        drifted.append(translated.text)
        current_text = translated.text
    return drifted

# Example
input_text = "I fell in love the way you fall asleep: slowly, and then all at once." #johngreenquotehaha
drift_result = drift_text(input_text, languages)

print("\nLanguage Drift Sequence:")
for i, step in enumerate(drift_result):
    print(f"Step {i}: {step}")
