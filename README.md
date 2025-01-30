# string_to_number

# Convert Words to Numbers

## Overview
This Python program converts number words (e.g., "one hundred twenty-three") into numeric form (e.g., `123`). It supports numbers up to the trillions and handles different numerical segments such as "thousand," "million," "billion," and "trillion." The program also provides a formatted output with commas for better readability.

## Features
- Converts written numbers into numeric values
- Supports large numbers up to trillions
- Handles numbers with hyphens (e.g., "twenty-five")
- Formats output with commas for readability (e.g., `1,234,567`)

## Installation
Ensure you have Python installed (Python 3 recommended). Clone or download the script to your local machine.

## Usage
Run the script and input a number in words when prompted.

```sh
python main.py
```

### Example Inputs and Outputs
```sh
Enter value in words: one hundred twenty-three
123
```

```sh
Enter value in words: two million three hundred forty-five thousand six hundred seventy-eight
2,345,678
```

## How It Works
### 1. **Dictionary Mapping**
The program defines a dictionary mapping words to their numeric equivalents.

### 2. **Segment Extraction**
The input is split into relevant numerical segments (thousand, million, etc.), handling cases where numbers are grouped together.

### 3. **Recursive Computation**
The program recursively divides and processes segments, ensuring correct multiplication and addition logic.

### 4. **Normalization & Formatting**
The final number is formatted with commas if necessary.

## File Structure
```
main.py  # Main script
README.md  # Documentation
```


