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
        self.y = 800

    def write_title(self, text: str):
        """Writes the title text.
        """
        self._decrement_y(40)
        self.pdf.setFont("Courier-Bold", 36)
        self.pdf.drawCentredString(300, self.y, text)

    def write_sub_title(self, text: str):
        """Writes the subtitle text
        """
        self._decrement_y(30)
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.setFont("Courier-Bold", 24)
        self.pdf.drawCentredString(290, self.y, text)

    def draw_line(self):
        # drawing a line
        self.pdf.line(30, 710, 550, 710)

    def write_lines(self, texts: list[str]):
        num_lines = len(texts)
        self._decrement_y(20)

        text = self.pdf.beginText(40, self.y)
        text.setFont("Courier", 16)
        self.pdf.setFillColorRGB(0, 0, 0)

        for line in texts:

            text.textLine(line)

        self._decrement_y(20 * (num_lines - 1))

        self.pdf.drawText(text)

    def _decrement_y(self, value: int):
        """Needed for manual cursor shifting """
        self.y -= value


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

    lst2 = [
        "another one bites the dust",
        "You know, you know",
        "Another thing"
    ]
    pdf_handler.write_lines(lst)
    pdf_handler.write_lines(lst2)

    pdf_handler.save()
