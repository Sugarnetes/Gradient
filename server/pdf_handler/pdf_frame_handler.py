from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Flowable, FrameBreak, KeepTogether, PageBreak, Spacer
from reportlab.platypus import Frame, PageTemplate, KeepInFrame
from reportlab.lib.units import cm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)

styleSheet = getSampleStyleSheet()

########################################################################

def create_pdf():
    """
    Create a pdf
    """

    # Create a frame
    text_frame = Frame(
        x1=3.00 * cm,  # From left
        y1=1.5 * cm,  # From bottom
        height=19.60 * cm,
        width=15.90 * cm,
        leftPadding=0 * cm,
        bottomPadding=0 * cm,
        rightPadding=0 * cm,
        topPadding=0 * cm,
        showBoundary=1,
        id='text_frame')

    # Create text

    L = [Paragraph("""What concepts does PLATYPUS deal with?""", styleSheet['Heading2']),
         Paragraph("""
                         The central concepts in PLATYPUS are Flowable Objects, Frames, Flow
                         Management, Styles and Style Sheets, Paragraphs and Tables.  This is
                         best explained in contrast to PDFgen, the layer underneath PLATYPUS.
                         PDFgen is a graphics library, and has primitive commans to draw lines
                         and strings.  There is nothing in it to manage the flow of text down
                         the page.  PLATYPUS works at the conceptual level fo a desktop publishing
                         package; you can write programs which deal intelligently with graphic
                         objects and fit them onto the page.
                         """, styleSheet['BodyText']),

         Paragraph("""
                         How is this document organized?
                         """, styleSheet['Heading2']),

         Paragraph("""
                         Since this is a test script, we'll just note how it is organized.
                         the top of each page contains commentary.  The bottom half contains
                         example drawings and graphic elements to whicht he commentary will
                         relate.  Down below, you can see the outline of a text frame, and
                         various bits and pieces within it.  We'll explain how they work
                         on the next page.
                         """, styleSheet['BodyText']),
         ]






    # Building the story
    story = L * 20 # (alternative, story.add(L))
    story.append(KeepTogether([]))

    # Establish a document
    doc = BaseDocTemplate("Example_output.pdf", pagesize=letter)

    # Creating a page template
    frontpage = PageTemplate(id='FrontPage',
                             frames=[text_frame]
                             )
    # Adding the story to the template and template to the document
    doc.addPageTemplates(frontpage)

    # Building doc
    doc.build(story)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_pdf() # Printing the pdf
