# AUTOMATED-REPORT-GENERATION

*COMPANY:* CodTech IT Solutions  

*NAME:* PEDAPROLU S S L KATYAYANI

*INTERN ID:* CTO6WS178

*DOMAIN:* Python Programming 

*DURATION:* 6 Weeks  

*MENTOR:* Neela Santosh

## About Project

The *Automated Report Generation* project is a Python-based solution designed to streamline the process of analyzing data and generating professional reports. This project was developed as part of a 4-week internship at CodTech IT Solutions under the guidance of mentor Neela Santosh.

The main objective of this project is to automatically read sales data from a CSV file, generate insightful visualizations using matplotlib, and compile them into a PDF report using fpdf. The script calculates total sales, identifies the top-performing product, and creates a bar chart for visual representation.

This application improves productivity by eliminating manual reporting tasks and allows easy customization for different datasets and formats. It can be extended to support Excel files, email delivery, or even integration with databases.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- FPDF
- CSV File Handling

---

## Features

- Reads data from a CSV file
- Analyzes total and product-wise sales
- Generates bar chart visualizations
- Exports a structured PDF report
- Creates output files in the reports/ folder

---

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies
4. pip install pandas matplotlib fpdf
5. Make sure your CSV file is located in the data/ folder.
6. Run the script:python report_generator.py

---

## Output

After successfully running the script, the following output files are generated in the reports/ directory:

### monthly_sales_report.pdf
A professionally formatted PDF document that includes:
- Title and summary (total sales, top product)
- A clean bar chart showing product-wise sales
- Neatly structured layout using the FPDF library

### sales_chart.png
A bar chart image automatically created using matplotlib, visualizing sales by product category. This chart is embedded inside the PDF report.

### Sample Output Previews

![Monthly Report Cover](https://github.com/user-attachments/assets/c987b4e8-3929-46ce-993a-b5cfa83f9d84)

![Sales Chart](https://github.com/user-attachments/assets/6784f385-5b42-4780-9932-1195cf718797)

![Report Content](https://github.com/user-attachments/assets/87117c19-a756-411d-a034-28d2df4cd873)

