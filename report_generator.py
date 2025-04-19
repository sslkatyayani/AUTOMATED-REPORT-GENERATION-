import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Read CSV data
data = pd.read_csv("data/sales_data.csv")

# Summary
total_sales = data["Sales"].sum()
top_product = data.groupby("Product")["Sales"].sum().idxmax()
top_product_sales = data.groupby("Product")["Sales"].sum().max()

# Generate bar chart
plt.figure(figsize=(8, 5))
data.groupby("Product")["Sales"].sum().plot(kind="bar", color="skyblue")
plt.title("Sales by Product")
plt.ylabel("Total Sales")
plt.tight_layout()

# Save chart
os.makedirs("reports", exist_ok=True)
chart_path = "reports/sales_chart.png"
plt.savefig(chart_path)
plt.close()

# Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Monthly Sales Report", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Sales: ${total_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Top Product: {top_product} (${top_product_sales:,.2f})", ln=True)

pdf.ln(10)
pdf.image(chart_path, w=170)

report_path = "reports/monthly_sales_report.pdf"
pdf.output(report_path)

print(f"Report generated at: {report_path}")
