import emoji

emojis = {
        '❤️': ':red_heart:',
        '👍': ':thumbs_up:',
        '🤔': ':thinking_face:',
        '🥳': ':partying_face:'
    }

print("Emojis disponíveis:")
for emoji_char, emoji_code in emojis.items():
        print(f"{emoji_char} - {emoji_code}")

frase_codificada = input("\nDigite uma frase e ela será emojizada: ")
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

print("Frase emojizada:")
print(frase_emojizada)
