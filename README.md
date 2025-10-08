🎨Bincom ICT Solutions – Dress Color Analysis

This Python 3 project analyzes the colors of dresses worn by Bincom ICT staff during the week, as provided in a sample HTML dataset.
The analysis helps determine which color of T-shirt should be produced for staff based on color frequency and statistical metrics.

🧠 Features
Extracts color data from the HTML table
Cleans and normalizes color names (fixes “BLEW” → “BLUE”, etc.)
Calculates:
Mean color – color frequency closest to the average
Most worn color – highest frequency
Median color – middle frequency
Variance – distribution spread
Probability of Red – chance of randomly picking “RED”
Saves color frequencies into a PostgreSQL database (optional)
Includes recursive search function example
Generates and converts random 4-bit binary to base-10
Computes the sum of the first 50 Fibonacci numbers
⚙️ Requirements
Python 3.x
Libraries:
pip install psycopg2-binary

(Optional if you skip database saving)
🚀 How to Run
Save the provided HTML file as bincom_colors.html in the same folder as the script.
Run the script:
python code_dress.py

View the console output for all statistical results.
🧩 Project Structure
bincom_project/
│
├── bincom_colors.html   # HTML source data
├── code_dress.py        # Python analysis script
└── README.md            # Project documentation

💡 Notes
The script can run without PostgreSQL; comment out the DB section if not installed.
Ideal for demonstrating skills in data cleaning, statistics, and Python automation.
👨🏾‍💻 Author

Iroha Robert
Cybersecurity & Python Professional
