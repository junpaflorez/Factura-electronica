from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import qrcode

# Pedir datos generales de la factura
numero_factura = input("Número de factura: ")
cliente = input("Cliente: ")

# Pedir productos dinámicamente
productos = []
print("\nIngrese los productos de la factura (escriba 'fin' para terminar):")
while True:
    nombre = input("Producto: ")
    if nombre.lower() == "fin":
        break
    cantidad = input("Cantidad: ")
    precio = float(input("Precio unitario: "))
    subtotal = float(cantidad) * precio
    productos.append([nombre, cantidad, precio, subtotal])

# Generar QR con información de la factura
factura_data = f"Factura #{numero_factura} - Cliente: {cliente} - producto: " + ", ".join([f"{p[0]} unidades:{p[1]} valor: ${p[2]} total= ${p[3]}" for p in productos])
qr = qrcode.make(factura_data)
qr_filename = "factura_qr.png"
qr.save(qr_filename)

# Crear PDF
pdf_filename = "factura.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Encabezado
elements.append(Paragraph("FACTURA ELECTRÓNICA", styles['Title']))
elements.append(Spacer(1, 32))
elements.append(Paragraph(f"Número: {numero_factura}", styles['Normal']))
elements.append(Paragraph(f"Cliente: {cliente}", styles['Normal']))
elements.append(Spacer(1, 32))

# Armar tabla con productos
data = [["Producto", "Cantidad", "Precio Unitario", "Subtotal"]] + productos

table = Table(data, colWidths=[120, 80, 100, 100])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
]))
elements.append(table)
elements.append(Spacer(1, 24))

# Insertar QR
elements.append(Image(qr_filename, width=220, height=220))

# Pie de página
elements.append(Spacer(1, 24))
elements.append(Paragraph("Gracias por su compra", styles['Italic']))

# Construir PDF
doc.build(elements)
print(f"Factura generada en {pdf_filename}")