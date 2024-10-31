import streamlit as st
from spellchecker import SpellChecker

# Creating Class
class SpellCheck:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                st.write(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)

        # Returning corrected words
        return ' '.join(corrected_words)

# Streamlit app function
def run_spell_checker():
    st.title("Spell Checker App")
    
    # Text input field
    text = st.text_area("Enter text to check for spelling mistakes:")

    # Button to run the spell checker
    if st.button("Check Spelling"):
        if text:
            spell_checker = SpellCheck()
            corrected_text = spell_checker.correct_text(text)
            st.write(f"Corrected Text: {corrected_text}")
        else:
            st.write("Please enter some text to check.")

# Run the Streamlit app
if __name__ == "__main__":
    run_spell_checker()
