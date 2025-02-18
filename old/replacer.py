# print("https://qr.fluxqr.net/?text=fR2+IPU+RF2MHisk9nGKC8cgKz0MwrRCvdWTXXce7CsX0+rIA01p/gng==".replace("+", "%2B"))

# print(len('abc'))

# String de ejemplo
text = "Este es    un    ejemplo   \n\n\ncon    muchos   espacios     y saltos de línea."

# Remover espacios largos y saltos de línea
cleaned_text = ' '.join(text.split())

print(f"Texto limpio: {cleaned_text}")