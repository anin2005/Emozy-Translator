# Define a dictionary mapping words/phrases to emojis
emoji_dict = {
    'happy': '😊',
    'sad': '😢',
    'love': '❤️',
    'star': '⭐',
    'fire': '🔥',
    'cat': '😸',
    'dog': '🐶',
    'hello': '👋',
    'goodbye': '👋',
    'music': '🎵',
    'party': '🎉'
}

def text_to_emoji(text):
    # Split the input text into words
    words = text.lower().split()
    
    # Translate each word to its corresponding emoji if available
    translated_words = [emoji_dict.get(word, word) for word in words]
    
    # Join the translated words back into a single string
    return ' '.join(translated_words)

# Example usage
if __name__ == "__main__":
    input_text = input("Enter a text to translate into emojis: ")
    translated_text = text_to_emoji(input_text)
    print("Translated text:", translated_text)
