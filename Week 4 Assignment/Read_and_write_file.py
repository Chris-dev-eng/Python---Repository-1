def read_and_write_file():
    try:
        input_file = input("Enter the filename to read from: ")
        
        with open(input_file, 'r') as file:
            content = file.readlines()
        
        modified_content = [line.upper() for line in content]

        output_file = input("Enter the filename to write to: ")

        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}. 🎉")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please try again.")
    except IOError:
        print(f"Error: Could not read or write files. Please check your permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
