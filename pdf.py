#pdf oluşturma
dosyaadi='İmha Raporu.pdf'
title="İmha Raporu"
teknikeleman=u"Raporu Oluşturan Kişi:".encode('utf-8')
firma='Firma:'
diskbilgileri="disk disk disk"


rapor_yazısı=['Bu rapor Tekniknokta Bilişim Teknoloji Hizm. tarafından Hazırlanmış Prowipe yazılımı ile hazırlanmıştır.'
              'Konu disk yukarıda belirtilmiştir.'
              'Disk üzerinde yapılan işlem:']

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def drawMyRuler(pdf):
    pdf.drawString(100,810,'x100')
    pdf.drawString(200,810,'x200')
    pdf.drawString(300,810,'x300')
    pdf.drawString(400,810,'x400')
    pdf.drawString(500,810,'x500')

    pdf.drawString(10,800,'y800')
    pdf.drawString(10,700,'y700')
    pdf.drawString(10,600,'y600')
    pdf.drawString(10,500,'y500')
    pdf.drawString(10,400,'y400')
    pdf.drawString(10,300,'y300')
    pdf.drawString(10,200,'y200')
    pdf.drawString(10,100,'y100')
    logo="tn-logo.jpg"
    baslik="Veri İmha Raporu123"
    pdf.drawImage(logo,450,800)
    pdf.drawString(50,700,baslik)


pdf=canvas.Canvas(dosyaadi,pagesize=A4)

pdf.setTitle(title)
drawMyRuler(pdf)
pdf.save()


