"""Pytest configuration and fixtures for pdf-mergician tests."""

import pytest
from pypdf import PdfWriter


@pytest.fixture
def temp_pdf_dir(tmp_path):
    """Create a temporary directory for PDF files."""
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    return pdf_dir


@pytest.fixture
def sample_pdf(temp_pdf_dir):
    """Create a single-page sample PDF."""
    pdf_path = temp_pdf_dir / "sample.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)  # Letter size
    with pdf_path.open("wb") as f:
        writer.write(f)
    return pdf_path


@pytest.fixture
def multi_page_pdf(temp_pdf_dir):
    """Create a 10-page sample PDF."""
    pdf_path = temp_pdf_dir / "multi_page.pdf"
    writer = PdfWriter()
    for _ in range(10):
        writer.add_blank_page(width=612, height=792)
    with pdf_path.open("wb") as f:
        writer.write(f)
    return pdf_path


@pytest.fixture
def multiple_pdfs(temp_pdf_dir):
    """Create multiple sample PDFs with different page counts."""
    pdfs = []
    for i, num_pages in enumerate([3, 5, 2], start=1):
        pdf_path = temp_pdf_dir / f"doc{i}.pdf"
        writer = PdfWriter()
        for _ in range(num_pages):
            writer.add_blank_page(width=612, height=792)
        with pdf_path.open("wb") as f:
            writer.write(f)
        pdfs.append(pdf_path)
    return pdfs
