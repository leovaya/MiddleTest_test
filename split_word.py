def count_words_and_sentences(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        text = file.read().strip()
    
    if not text:
        return 0, 0  # Якщо файл порожній
    
    sentences_endings = {'.', '!', '?'}
    words_delimiters = {' ', ',', ':', ';'}
    sentences_count = 0
    words_count = len([word for word in text.split() if word])  # Підрахунок слів

    i = 0
    while i < len(text):
        if text[i] in sentences_endings:
            if text[i:i+3] == '...':  # Перевіряємо "..."
                i += 2  # Пропускаємо наступні дві крапки
            sentences_count += 1
        i += 1
    
    # Якщо останній символ не є кінцем речення, але є слова, додаємо речення
    if text[-1] not in sentences_endings and words_count > 0:
        sentences_count += 1
    
    return words_count, sentences_count