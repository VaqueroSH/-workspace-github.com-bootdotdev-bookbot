from stats import get_num_words, get_character_frequency


def get_book_text(file_path):
    """
    Read and return the text content of a book file.
    
    Args:
        file_path (str): Path to the book file
        
    Returns:
        str: The text content of the book
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Book file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading book file: {e}")


def main():
    # Example usage
    book_path = "books/frankenstein.txt"
    try:
        text = get_book_text(book_path)
        word_count = get_num_words(text)
        char_frequency = get_character_frequency(text)
        
        print(f"{word_count} words found in the document")
        print(f"Character frequency analysis:")
        
        # Show top 10 most frequent characters
        sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
        for char, count in sorted_chars[:10]:
            if char == ' ':
                print(f"  'space': {count}")
            elif char == '\n':
                print(f"  'newline': {count}")
            else:
                print(f"  '{char}': {count}")
                
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


