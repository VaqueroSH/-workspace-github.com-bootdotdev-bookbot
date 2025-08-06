"""
Book text analysis and statistics module.
Contains functions to analyze and generate statistics from book text.
"""

import re
from collections import Counter


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


def get_num_words(text):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): The text to count words in
        
    Returns:
        int: The number of words in the text
    """
    if not text:
        return 0
    
    # Split the text into words and count them
    words = text.split()
    return len(words)


def get_num_characters(text):
    """
    Count the number of characters in the given text.
    
    Args:
        text (str): The text to count characters in
        
    Returns:
        int: The number of characters in the text
    """
    return len(text)


def get_num_sentences(text):
    """
    Count the number of sentences in the given text.
    
    Args:
        text (str): The text to count sentences in
        
    Returns:
        int: The number of sentences in the text
    """
    if not text:
        return 0
    
    # Split on sentence ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def get_num_paragraphs(text):
    """
    Count the number of paragraphs in the given text.
    
    Args:
        text (str): The text to count paragraphs in
        
    Returns:
        int: The number of paragraphs in the text
    """
    if not text:
        return 0
    
    # Split on double newlines (paragraph breaks)
    paragraphs = text.split('\n\n')
    # Filter out empty strings
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return len(paragraphs)


def get_word_frequency(text, top_n=10):
    """
    Get the most frequent words in the text.
    
    Args:
        text (str): The text to analyze
        top_n (int): Number of top words to return (default: 10)
        
    Returns:
        list: List of tuples (word, count) sorted by frequency
    """
    if not text:
        return []
    
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation from words
    cleaned_words = []
    for word in words:
        cleaned_word = re.sub(r'[^\w]', '', word)
        if cleaned_word:  # Only add non-empty words
            cleaned_words.append(cleaned_word)
    
    # Count word frequencies
    word_counts = Counter(cleaned_words)
    
    # Return top N most common words
    return word_counts.most_common(top_n)


def get_average_word_length(text):
    """
    Calculate the average length of words in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        float: Average word length in characters
    """
    if not text:
        return 0.0
    
    words = text.split()
    if not words:
        return 0.0
    
    # Remove punctuation and calculate lengths
    word_lengths = []
    for word in words:
        cleaned_word = re.sub(r'[^\w]', '', word)
        if cleaned_word:
            word_lengths.append(len(cleaned_word))
    
    if not word_lengths:
        return 0.0
    
    return sum(word_lengths) / len(word_lengths)


def get_character_frequency(text):
    """
    Count the frequency of each character in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary where keys are characters (lowercase) and values are counts
    """
    if not text:
        return {}
    
    # Convert text to lowercase
    text_lower = text.lower()
    
    # Create dictionary to store character counts
    char_counts = {}
    
    # Count each character
    for char in text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts


def generate_text_report(text):
    """
    Generate a comprehensive text analysis report.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary containing various text statistics
    """
    return {
        'characters': get_num_characters(text),
        'words': get_num_words(text),
        'sentences': get_num_sentences(text),
        'paragraphs': get_num_paragraphs(text),
        'average_word_length': round(get_average_word_length(text), 2),
        'top_words': get_word_frequency(text, 5)
    }
    