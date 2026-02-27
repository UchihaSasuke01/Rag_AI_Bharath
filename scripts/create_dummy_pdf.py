from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(filename):
    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    content = """
PM Kisan Samman Nidhi Scheme

Overview:
This scheme provides financial assistance of Rs. 6000 per year to small and marginal farmers.

Eligibility Criteria:
1. Applicant must be a farmer.
2. Land holding must be less than or equal to 2 hectares.
3. Annual family income must be below Rs. 200000.
4. Applicant must be an Indian citizen.

Benefits:
Eligible farmers receive Rs. 2000 every four months directly into their bank account.

Required Documents:
- Aadhaar Card
- Bank Passbook
- Land Ownership Records
- Income Certificate

Application Process:
1. Visit nearest CSC center.
2. Submit required documents.
3. Complete biometric verification.
4. Wait for approval SMS notification.

Helpline:
Call 1800-111-555 for assistance.
"""

    for line in content.split("\n"):
        elements.append(Paragraph(line, normal))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)
    print("Dummy PDF created successfully!")

if __name__ == "__main__":
    create_pdf("pm_kisan_dummy.pdf")