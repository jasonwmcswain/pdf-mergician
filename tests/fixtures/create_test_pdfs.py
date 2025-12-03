#!/usr/bin/env python3
"""
Create test PDF fixtures for testing.

This script generates sample PDFs with actual content for more realistic testing.
"""

from pathlib import Path

from pypdf import PdfWriter

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


def create_sample_pdf_with_text(filename: Path, num_pages: int, title: str):
    """Create a PDF with text content using reportlab."""
    if not REPORTLAB_AVAILABLE:
        raise ImportError("reportlab not available")

    c = canvas.Canvas(str(filename), pagesize=letter)
    width, height = letter

    for page_num in range(1, num_pages + 1):
        # Add title
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 100, title)

        # Add page number
        c.setFont("Helvetica", 16)
        c.drawCentredString(width / 2, height - 150, f"Page {page_num} of {num_pages}")

        # Add some body text
        c.setFont("Helvetica", 12)
        y_position = height - 200
        lines = [
            f"This is page {page_num} of the {title} document.",
            "",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
            "",
            f"Document: {title}",
            f"Page: {page_num}/{num_pages}",
        ]

        for line in lines:
            c.drawString(100, y_position, line)
            y_position -= 20

        c.showPage()

    c.save()


def create_blank_pdf(filename: Path, num_pages: int):
    """Create a simple blank PDF."""
    writer = PdfWriter()
    for _ in range(num_pages):
        writer.add_blank_page(width=612, height=792)  # Letter size
    with filename.open("wb") as f:
        writer.write(f)


def main():
    """Create all test fixtures."""
    fixtures_dir = Path(__file__).parent
    fixtures_dir.mkdir(exist_ok=True)

    print("Creating test PDF fixtures...")

    # Try to use reportlab for better PDFs
    try:
        # Document A - 10 pages
        create_sample_pdf_with_text(
            fixtures_dir / "document_a.pdf", 10, "Document A - Test File"
        )
        print("  ✓ Created document_a.pdf (10 pages with text)")

        # Document B - 10 pages
        create_sample_pdf_with_text(
            fixtures_dir / "document_b.pdf", 10, "Document B - Test File"
        )
        print("  ✓ Created document_b.pdf (10 pages with text)")

        # Document C - 5 pages
        create_sample_pdf_with_text(
            fixtures_dir / "document_c.pdf", 5, "Document C - Test File"
        )
        print("  ✓ Created document_c.pdf (5 pages with text)")

        # Small document - 3 pages
        create_sample_pdf_with_text(
            fixtures_dir / "small_doc.pdf", 3, "Small Document"
        )
        print("  ✓ Created small_doc.pdf (3 pages with text)")

        # Single page
        create_sample_pdf_with_text(fixtures_dir / "single_page.pdf", 1, "Single Page")
        print("  ✓ Created single_page.pdf (1 page with text)")

    except ImportError:
        print("  ⚠ reportlab not available, creating blank PDFs instead")

        # Fallback to blank PDFs
        create_blank_pdf(fixtures_dir / "document_a.pdf", 10)
        print("  ✓ Created document_a.pdf (10 blank pages)")

        create_blank_pdf(fixtures_dir / "document_b.pdf", 10)
        print("  ✓ Created document_b.pdf (10 blank pages)")

        create_blank_pdf(fixtures_dir / "document_c.pdf", 5)
        print("  ✓ Created document_c.pdf (5 blank pages)")

        create_blank_pdf(fixtures_dir / "small_doc.pdf", 3)
        print("  ✓ Created small_doc.pdf (3 blank pages)")

        create_blank_pdf(fixtures_dir / "single_page.pdf", 1)
        print("  ✓ Created single_page.pdf (1 blank page)")

    print("\n✅ All test fixtures created successfully!")
    print(f"   Location: {fixtures_dir}")


if __name__ == "__main__":
    main()

