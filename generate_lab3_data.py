def break_into_groups(input_file, output_file):
    """
    Reads a text file, breaks the text into groups of 15 words, 
    and writes it into another file with a specified format.
    """
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            text = file.read()

        # Split the text into words
        words = text.split()

        # Initialize a list to store the groups
        groups = []

        # Iterate over the words and create 15-word groups
        for i in range(0, len(words), 15):
            group = ' '.join(words[i:i + 15])
            groups.append(f"en|{group}")

        # Write the groups to the output file
        with open(output_file, 'w') as file:
            for group in groups:
                file.write(group + '\n')

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
input_file_path = 'input.txt'  # Replace with your actual file path
output_file_path = 'output.txt'  # Replace with your desired output file path

break_into_groups(input_file_path, output_file_path)