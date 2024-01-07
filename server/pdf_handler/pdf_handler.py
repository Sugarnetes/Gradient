# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors



class PdfHandler:
    def __init__(self, file_name, document_title):
        """
        The file name that is being used is imparative to making this work
        """

        self.pdf = canvas.Canvas(file_name)
        self.pdf.setTitle(document_title)
        self.x = 40
        self.y = 40

    def write_title(self, text: str):
        """Writes the title text.
        """
        self.pdf.setFont("Courier-Bold", 36)
        self.pdf.drawCentredString(300, 770, text)

    def write_sub_title(self, text: str):
        """Writes the subtitle text
        """
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.setFont("Courier-Bold", 24)
        self.pdf.drawCentredString(290, 720, text)

    def draw_line(self):
        # drawing a line
        self.pdf.line(30, 710, 550, 710)

    def write_lines(self, texts: list[str]):
        text = self.pdf.beginText(40, 680)
        text.setFont("Courier", 18)

        for line in texts:
            text.textLine(line)

        self.pdf.drawText(text)

    def save(self):
        self.pdf.save()


if __name__ == "__main__":
    pdf_handler = PdfHandler("test.pdf", "for_testing")
    pdf_handler.write_title("testing")
    pdf_handler.write_sub_title("testing sub title")
    lst = [
        "Something",
        "Longer sentence is here. Hahahahahahahahhahahahahhahahahahahhahahahahhahahahhahahahha.",
        "Another one bites the dust"
    ]
    pdf_handler.write_lines(lst)

    pdf_handler.save()
