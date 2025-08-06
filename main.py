import sys
from stats import get_num_words, get_character_frequency, sort_character_frequency


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
    # Check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the second argument as the book path
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
        word_count = get_num_words(text)
        char_frequency = get_character_frequency(text)
        sorted_chars = sort_character_frequency(char_frequency)
        
        print("============= BOOKBOT =============")
        print(f"Analyzing book found at {book_path}...")
        print()
        print("--------- Word Count ---------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        for char_data in sorted_chars:
            char = char_data["char"]
            count = char_data["num"]
            print(f"{char}: {count}")
        
        print("=============== END ===============")
                
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


