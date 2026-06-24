import os

def analyze_text_file(file_path: str) -> dict:
    """Reads a file and returns basic stats like word count and line count."""
    stats = {"line_count": 0, "word_count": 0, "unique_words": 0}
    words_list = []

    if not os.path.exists(file_path):
        return {"error": f"File '{file_path}' not found."}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stats["line_count"] += 1
                line_words = line.strip().split()
                words_list.extend(line_words)
        
        stats["word_count"] = len(words_list)
        # Using a set to find unique words
        stats["unique_words"] = len(set(word.lower() for word in words_list)) 
        
    except IOError as e:
        return {"error": f"An error occurred while reading the file: {e}"}

    return stats


# Example Usage:
if __name__ == "__main__":
    # Create a dummy file to test
    sample_file = "sample.txt"
    with open(sample_file, "w") as f:
        f.write("Hello World\nWelcome to Python scripting.\nPython is great.")

    results = analyze_text_file(sample_file)
    print("File Analysis Results:", results)
    
    # Cleanup
    if os.path.exists(sample_file):
        os.remove(sample_file)
