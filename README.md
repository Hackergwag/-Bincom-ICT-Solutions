<h1>🎨Bincom ICT Solutions – Dress Color Analysis</h1>

This Python 3 project analyzes the colors of dresses worn by Bincom ICT staff during the week, as provided in a sample HTML dataset.
The analysis helps determine which color of T-shirt should be produced for staff based on color frequency and statistical metrics.

<h1>🧠 Features</h1>

- <b>Extracts color data from the HTML table</b>
- <b>Cleans and normalizes color names (fixes “BLEW” → “BLUE”, etc.)</b>
- <b>Calculates:</b>
   - <b>Mean color – color frequency closest to the average</b>
   - <b>Most worn color – highest frequency</b>
   - <b>Median color – middle frequency</b>
   - <b>Variance – distribution spread</b>
   - <b>Probability of Red – chance of randomly picking “RED”</b>
- <b>Saves color frequencies into a PostgreSQL database (optional)</b>
- <b>Includes recursive search function example</b>
- <b>Generates and converts random 4-bit binary to base-10</b>
- <b>Computes the sum of the first 50 Fibonacci numbers</b>
<h2>⚙️ Requirements</h2>

- <b>Python 3.x</b>
- <b>Libraries:</b>
- <b>pip install psycopg2-binary</b>
   (Optional if you skip database saving)
<h1>🚀 How to Run</h1>

- <b>Save the provided HTML file as bincom_colors.html in the same folder as the script.</b>
- <b>Run the script:</b>
  - <b>python code_dress.py</b>

- <b>View the console output for all statistical results.</b>
<h2>🧩 Project Structure</h2>
<h3>bincom_project:</h3>

- <b> bincom_colors.html   # HTML source data</b>
- <b>code_dress.py        # Python analysis script</b>
- <b>README.md            # Project documentation</b>

<h2>💡 Notes</h2>

- <b>The script can run without PostgreSQL; comment out the DB section if not installed.</b>
- <b>Ideal for demonstrating skills in data cleaning, statistics, and Python automation.</b>
<h2>👨🏾‍💻 Author</h2>

Iroha Robert
Cybersecurity & Python Professional
