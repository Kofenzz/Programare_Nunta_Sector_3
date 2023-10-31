# Selenium Web Automation Script for making a reservation for wedding

This Python script uses the Selenium library to automate interactions with a specific website, filling out various forms. The script is designed for a particular use case, and it uses environment variables for sensitive information.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed (Python 3 is recommended)
- Selenium library installed (`pip install selenium`)
- The `python-decouple` library installed (`pip install python-decouple`)
- A compatible web driver for your browser installed (e.g., GeckoDriver for Firefox)

## Usage

1. Clone or download this repository to your local machine.

2. Create a `.env` file in the same directory as the script. Add your sensitive information to the `.env` file. Here's an example of the `.env` file structure:

   ```ini

   PHONE_NUMBER=000000000000
   EMAIL=email@email.com
   CNP_H=1111111111111
   NAME_H=LastName
   PRENUME_H=FirstName
   COUNTY_W=COUNTY
   TOWN_VILLAGE_W=TOWN
   ADRESA_H=ADDRESS
   
   CNP_W=1111111111111
   NAME_W=LastName
   PRENUME_W=FirstName
   COUNTY_W=COUNTY
   TOWN_VILLAGE_W=TOWN
   ADRESA_W=ADDRESS



Fill in the variables with your actual data.

Adjust the script as needed for your specific use case, setting the TARGET_DATE_TEXT and TARGET_HOUR_TEXT as required.

Run the script using the following command:

python main.py

## Important Note
This script is designed for a specific website and use case. Make sure you have the necessary permissions to automate interactions with the website in question.

Always keep your sensitive information and credentials secure and do not share them in your code or public repositories.

## License

This project is licensed under the [Apache License 2.0](LICENSE).


Be sure to add the LICENSE file with the Apache License 2.0 text to your project directory.



