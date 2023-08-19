from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_invoice_pdf(invoice_data, filename):
    # Define the PDF document settings
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Define the table data for the invoice
    table_data = [
        ["Product", "Quantity", "Rate", "Total"],
    ]

    total_amount = 0

    # Process the invoice data and add it to the table
    for product, quantity, rate in invoice_data:
        total = quantity * rate
        table_data.append([product, str(quantity), f"${rate:.2f}", f"${total:.2f}"])
        total_amount += total

    # Add the table to the document
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Add total amount to the document
    styles = getSampleStyleSheet()
    elements.append(Paragraph(f"Total Amount: ${total_amount:.2f}", styles['Normal']))

    # Build the PDF document
    doc.build(elements)

# Example usage:
invoice_data = [
    ("Product A", 2, 10.99),
    ("Product B", 1, 5.49),
    ("Product C", 3, 2.99),
]

create_invoice_pdf(invoice_data, "invoice.pdf")
