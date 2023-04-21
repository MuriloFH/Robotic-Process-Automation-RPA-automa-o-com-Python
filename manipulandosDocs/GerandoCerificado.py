from docx import Document
from docx.shared import Pt

# abrindo arquivo já existente
arquivoWord = Document("C:\\Users\\murilo.fernandes\\Documents\\Udemy\\Robotic_Process_Automation_RPA_automação_Python\\manipulandosDocs\\Certificado1.docx")

# seleiconando estilo
estilo = arquivoWord.styles["Normal"]

for paragrafo in arquivoWord.paragraphs:
    if "@nome" in paragrafo.text:
        paragrafo.text = "Murilo Henrique Fernandes"
        fonte = estilo.font
        fonte.name = "Calabri (Corpo)"
        fonte.size = Pt(24)

arquivoWord.save("Murilo Henrique Fernandes.docx")

