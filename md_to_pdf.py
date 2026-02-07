"""Convert module_summary.md to module_summary.pdf using markdown + xhtml2pdf."""
import markdown
from xhtml2pdf import pisa

def md_to_pdf(md_path: str, pdf_path: str) -> None:
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    html_body = markdown.markdown(md_text, extensions=["extra", "nl2br"])
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{ font-family: Helvetica, Arial, sans-serif; margin: 2em; line-height: 1.5; }}
h1 {{ font-size: 1.4em; border-bottom: 1px solid #ccc; }}
h2 {{ font-size: 1.2em; margin-top: 1.2em; }}
h3 {{ font-size: 1.05em; }}
p {{ margin: 0.5em 0; }}
ul {{ margin: 0.5em 0; padding-left: 1.5em; }}
code {{ background: #f4f4f4; padding: 0.1em 0.3em; }}
a {{ color: #0066cc; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""
    with open(pdf_path, "wb") as out:
        pisa.CreatePDF(html.encode("utf-8"), out, encoding="utf-8")

if __name__ == "__main__":
    md_to_pdf("module_summary.md", "module_summary.pdf")
    print("Created module_summary.pdf")
