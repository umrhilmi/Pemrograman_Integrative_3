def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def main():
    filename = "indata.txt"
    numbers = read_numbers_from_file(filename)
    
    if numbers:
        total = sum(numbers)
        formatted_total = '{:,.2f}'.format(total)
        print(formatted_total)

if __name__ == "__main__":
    main()
