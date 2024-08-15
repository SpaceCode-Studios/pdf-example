from fpdf import FPDF

# Define jou Header en Footer in 'n class
class FPDF(FPDF):
    def header(self):
        # self.image('logo.png', 10, 6, 30)
        self.set_font('Arial', 'B', 25)
        self.cell(80)
        self.cell(30, 10, die_titel, 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Jy hoef nie die parameters in die "FPDF" in te pass nie, dit is die default. Wil net wys waar jy dit kan stel
pdf = FPDF("P", "mm", "A4")

# Define al jou variables eerste
width = 210
height = 279
pdf.set_font("Arial", "", 8)
pdf.set_margins(10,10,10)

# Die toets variables
toets_text = "HAZZA"
toets_text_twee = "Baie lang text string wat moontlik kan aangaan virewig as ons sou wou maar vir die sake van die voorbeels gaan ek nou een of ander tyd moet stop"
die_titel = "B A K E N S  V A N  G O N D O R"

# Na jy jou variables geset het roep jy die "add_page" funksie om page te create en sit al die logic onder hom
pdf.add_page()

# Hier moet jy jou x, y define vir posisie
pdf.text(5, 25, toets_text_twee)

# Jy kan text is cells ook render om border rondom hulle te sit vir soos 'n getal
pdf.cell(0, 8, toets_text, 1)

# Toets page
pdf.add_page()

# As jy klaar die PDF gebou het dan roep jy "output" funksie om die PDF te create
pdf.output("Invoice.pdf")