#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():
    # Open the files we will be using
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')
    
    # Write the header for the CSV file
    outFile.write("Last Name,First Name,UserID,Major-Year\n")
    
    # Skip the first line (header) in the input file
    inFile.readline()
    
    # Process each line of the input file and output to the CSV file
    for line in inFile:
        # Split the line into fields using "|" as delimiter and strip whitespace
        fields = [field.strip() for field in line.split('|')]
        
        # Extract relevant fields
        first_name = fields[0]
        last_name = fields[1]
        student_id = fields[3]
        major = fields[6]
        year = fields[5]
        
        # Generate UserID
        user_id = f"{first_name[0].lower()}{last_name.lower()}{student_id[-3:]}"
        if len(last_name) < 5:
            user_id += "X"
        
        # Generate Major-Year
        year_abbreviation = {
            "Freshman": "FR",
            "Sophomore": "SO",
            "Junior": "JR",
            "Senior": "SR"
        }
        major_year = f"{major[:3].lower()}-{year_abbreviation.get(year, 'Unknown')}"
        
        # Write the processed data to the output file
        outFile.write(f"{last_name},{first_name},{user_id},{major_year}\n")
    
    # Close files in the end to save and ensure they are not damaged
    inFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
