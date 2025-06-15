import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Load data
df = pd.read_csv("people.csv")

# Basic stats
total = len(df)
gender = df['Sex'].value_counts()
top_jobs = df['Job Title'].value_counts().head(5)

# Create pie chart
gender.plot.pie(autopct='%1.1f%%', startangle=90, title='Gender Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig("gender.png")
plt.close()

# PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "People Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", "", 12)
summary = (
    f"Total People: {total}\n\n"
    f"Gender:\n{gender.to_string()}\n\n"
    f"Top 5 Jobs:\n{top_jobs.to_string()}"
)
pdf.multi_cell(0, 10, summary)
pdf.ln()
pdf.image("gender.png", x=60, w=90)

pdf.output("Report.pdf")
print("Report saved as Report.pdf")
