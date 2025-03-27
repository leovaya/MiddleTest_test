import pytest
import split_word

# Фікстура для створення тестових файлів
@pytest.fixture
def create_txt_file(tmp_path):
    """Фікстура, яка створює тимчасові .txt файли та повертає їхній шлях"""
    def _create_file(content):
        file = tmp_path / "testfile.txt"
        file.write_text(content, encoding="utf-8")
        return str(file)
    return _create_file

# Параметризовані тести
@pytest.mark.parametrize("text_content, expected_words, expected_sentences", [
    ("Hello, world! How are you?", 5, 2),  # Звичайний текст
    ("One. Two. Three.", 3, 3),  # Кожне слово - окреме речення
    ("This is a test...", 4, 1),  # "..."" - це один роздільник
    ("Wow! Amazing! Incredible!", 3, 3),  # Кожне слово - окреме речення
    ("Sentence without punctuation", 3, 1),  # Немає знаків закінчення
    ("", 0, 0),  # Порожній файл
    ("   ", 0, 0),  # Файл із пробілами
    ("Hello, world! Hello again.", 4, 2),  # Кома не розділяє речення
])
def test_count_words_and_sentences(create_txt_file, text_content, expected_words, expected_sentences):
    """Перевірка підрахунку слів і речень у різних випадках"""
    file_path = create_txt_file(text_content)
    words, sentences = split_word.count_words_and_sentences(file_path)
    assert words == expected_words, f"Очікувалося {expected_words} слів, отримано {words}"
    assert sentences == expected_sentences, f"Очікувалося {expected_sentences} речень, отримано {sentences}"
