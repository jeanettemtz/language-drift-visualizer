from googletrans import Translator

# Initialize the translator
translator = Translator()

# Define the sequence of languages to "drift" through
language_sequence = ['de', 'es', 'fr', 'en']  # German → Spanish → French → back to English

def drift_translation(original_text, langs):
    drifted_texts = [original_text]
    current_text = original_text

    for i, lang in enumerate(langs):
        try:
            translation = translator.translate(current_text, dest=lang)
            print(f"\nStep {i+1}: ({lang}) {translation.text}")
            drifted_texts.append(translation.text)
            current_text = translation.text
        except Exception as e:
            print(f"Translation error at step {i+1}: {e}")
            break

    return drifted_texts

if __name__ == "__main__":
    print("🌍 Language Drift Visualizer")
    user_input = input("Enter a sentence in English: ")

    print("\n🔁 Translating across languages...\n")
    drift_translation(user_input, language_sequence)

