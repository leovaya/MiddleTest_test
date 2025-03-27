import split_word as sw
def main():
    file_path = "test_file.txt"  # Вкажи свій файл

    try:
        words, sentences = sw.count_words_and_sentences(file_path)
        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено! Переконайтеся, що 'sample.txt' існує.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()