import wikipedia

def get_wiki_content(topic, language):
    wikipedia.set_lang(language)
    wiki_page = wikipedia.page(topic)
    return wiki_page.content.replace('==', '').split()

def break_into_groups(language, output_file, topic):
    try:
        words = get_wiki_content(topic, language)
        groups = []

        # Iterate over the words and create 15-word groups
        for i in range(0, len(words), 15):
            group = ' '.join(words[i:i + 15])
            groups.append(f"{language}|{group}")

        # Write to output file
        with open(output_file, 'w') as file:
            for group in groups:
                if len(group.split()) == 15:
                    file.write(group + '\n')

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == '__main__':
    # Example usage
    # input_file_path = 'input.txt'  # Replace with your actual file path
    # output_file_path = 'output.txt'  # Replace with your desired output file path
    language = input("Enter your language (en/nl): ").strip().lower()
    output_file = input("Enter the path to your output file: ")
    topic = input("Enter wikipedia a topic(s) to search for: ")

    break_into_groups(language, output_file, topic)