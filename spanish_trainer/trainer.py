# import csv      # Library for working with CSV (comma-separated) files
import random   # Library for random selection of elements from a list

class SpanishTrainer:
    """
    A simple class that helps you practice basic Spanish phrases.
    """

    def __init__(self):
        """
         Constructor - creates a list of phrases when the object is made.
        """
        self.phrases = [
            {"english": "Good morning.", "spanish": "Buenos días."},
            {"english": "Thank you.", "spanish": "Gracias."},
            {"english": "How are you?", "spanish": "¿Cómo estás?"},
            {"english": "Goodbye.", "spanish": "Adiós."},
            {"english": "I love you.", "spanish": "Te amo."}
        ]

    def get_random_phrases(self):
        """Select one random phrase from the list."""
        return random.choice(self.phrases)

    def show_phrase(self):
        """Show one phrase to the user."""
        phrase = self.get_random_phrases()
        print(f"🇺🇸 {phrase['english']}")
        input("👉 Press Enter to see the Spanish translation...")
        print(f"🇪🇸 {phrase['spanish']}\n")

    def start(self):
        """Start a small learning session."""
        print("🟢 Welcome to the Spanish Phrase Trainer!\n")
        again = "y"
        while again.lower() == "y":
            self.show_phrase()
            again = input("Do you want another phrase? (y/n): ")
        print("\n✅ Session finished. Great job!")