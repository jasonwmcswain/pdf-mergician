# Examples and Use Cases

This document provides practical examples and real-world use cases for `merge-pdf`.

---

## Table of Contents

- [Basic Operations](#basic-operations)
- [Advanced Patterns](#advanced-patterns)
- [Batch Processing](#batch-processing)
- [Document Workflows](#document-workflows)
- [Scripting Examples](#scripting-examples)
- [Python API Examples](#python-api-examples)

---

## Basic Operations

### Simple Merge

Combine multiple PDFs into one:

```bash
# Merge three documents
merge-pdf merge combined.pdf intro.pdf main.pdf conclusion.pdf

# Merge all PDFs in current directory
merge-pdf merge all.pdf *.pdf

# Merge with wildcards
merge-pdf merge chapters.pdf chapter*.pdf
```

### Extract Pages

Pull out specific pages:

```bash
# Extract first page (cover)
merge-pdf extract report.pdf cover.pdf --pages 1

# Extract table of contents (pages 2-5)
merge-pdf extract book.pdf toc.pdf --pages 2-5

# Extract multiple sections
merge-pdf extract document.pdf selected.pdf --pages 1,5-10,20-25
```

### Split Documents

Divide large PDFs:

```bash
# Split into individual pages
merge-pdf split presentation.pdf slides/

# Split into 10-page sections
merge-pdf split manual.pdf sections/ --pages-per-file 10

# Split into chapters (20 pages each)
merge-pdf split book.pdf chapters/ -p 20
```

### Rotate Pages

Fix page orientation:

```bash
# Rotate entire document
merge-pdf rotate scanned.pdf fixed.pdf --angle 90

# Rotate specific pages
merge-pdf rotate document.pdf fixed.pdf --angle 180 --pages 3,7,12

# Rotate counter-clockwise
merge-pdf rotate input.pdf output.pdf --angle -90
```

---

## Advanced Patterns

### Interleaving Documents

Alternate pages from two documents:

```bash
# Create side-by-side comparison
merge-pdf pattern comparison.pdf \
    -s original.pdf:1 -s revised.pdf:1 \
    -s original.pdf:2 -s revised.pdf:2 \
    -s original.pdf:3 -s revised.pdf:3 \
    -s original.pdf:4 -s revised.pdf:4 \
    -s original.pdf:5 -s revised.pdf:5
```

### Building Custom Documents

Assemble documents from multiple sources:

```bash
# Create report from various sources
merge-pdf pattern final_report.pdf \
    -s cover.pdf:1 \
    -s toc.pdf:1-2 \
    -s executive_summary.pdf:1-3 \
    -s data_analysis.pdf:5-25 \
    -s conclusions.pdf:1-5 \
    -s appendix.pdf:1-10
```

### Extracting Cover Pages

Collect first pages from multiple documents:

```bash
# Create cover sheet compilation
merge-pdf pattern all_covers.pdf \
    -s report1.pdf:1 \
    -s report2.pdf:1 \
    -s report3.pdf:1 \
    -s report4.pdf:1 \
    -s report5.pdf:1
```

### Reordering Pages

Rearrange pages in custom order:

```bash
# Reverse order of first 5 pages
merge-pdf pattern reordered.pdf \
    -s document.pdf:5 \
    -s document.pdf:4 \
    -s document.pdf:3 \
    -s document.pdf:2 \
    -s document.pdf:1 \
    -s document.pdf:6-100
```

---

## Batch Processing

### Process Multiple Files

Rotate all PDFs in a directory:

```bash
#!/bin/bash
for pdf in *.pdf; do
    echo "Rotating $pdf..."
    merge-pdf rotate "$pdf" "rotated_$pdf" --angle 90
done
```

Split all PDFs:

```bash
#!/bin/bash
for pdf in *.pdf; do
    dirname="split_${pdf%.pdf}"
    echo "Splitting $pdf into $dirname..."
    merge-pdf split "$pdf" "$dirname/" --pages-per-file 5
done
```

Extract first pages:

```bash
#!/bin/bash
for pdf in *.pdf; do
    output="cover_${pdf}"
    echo "Extracting cover from $pdf..."
    merge-pdf extract "$pdf" "$output" --pages 1
done
```

### Conditional Processing

Process files based on criteria:

```bash
#!/bin/bash
# Only process files larger than 1MB
for pdf in *.pdf; do
    size=$(stat -f%z "$pdf")
    if [ $size -gt 1048576 ]; then
        echo "Processing large file: $pdf"
        merge-pdf split "$pdf" "split_${pdf%.pdf}/" -p 10
    fi
done
```

---

## Document Workflows

### Creating Booklets

Prepare documents for booklet printing:

```bash
# Extract odd pages (front side)
merge-pdf extract document.pdf odd_pages.pdf --pages 1,3,5,7,9,11,13,15

# Extract even pages (back side)
merge-pdf extract document.pdf even_pages.pdf --pages 2,4,6,8,10,12,14,16

# Rotate even pages for back-to-back printing
merge-pdf rotate even_pages.pdf even_rotated.pdf --angle 180
```

### Preparing Presentations

Combine slides with notes:

```bash
# Merge presentation slides with speaker notes
merge-pdf pattern presentation_with_notes.pdf \
    -s slides.pdf:1 -s notes.pdf:1 \
    -s slides.pdf:2 -s notes.pdf:2 \
    -s slides.pdf:3 -s notes.pdf:3
```

### Document Assembly

Build complete documents from parts:

```bash
# Assemble contract from templates and filled forms
merge-pdf merge contract.pdf \
    cover_letter.pdf \
    terms_and_conditions.pdf \
    filled_form.pdf \
    signature_page.pdf \
    appendix_a.pdf \
    appendix_b.pdf
```

### Quality Control

Extract samples for review:

```bash
# Extract every 10th page for quick review
merge-pdf extract large_document.pdf sample.pdf --pages 10,20,30,40,50,60,70,80,90,100
```

---

## Scripting Examples

### Automated Report Generation

```bash
#!/bin/bash
# Generate monthly report

MONTH=$(date +%B_%Y)
OUTPUT="monthly_report_${MONTH}.pdf"

echo "Generating report for $MONTH..."

# Merge all sections
merge-pdf merge "$OUTPUT" \
    templates/cover.pdf \
    data/summary_${MONTH}.pdf \
    data/details_${MONTH}.pdf \
    templates/footer.pdf

echo "Report generated: $OUTPUT"
```

### PDF Organization Script

```bash
#!/bin/bash
# Organize PDFs by page count

mkdir -p short medium long

for pdf in *.pdf; do
    # Get page count (requires pdfinfo or similar)
    pages=$(pdfinfo "$pdf" 2>/dev/null | grep Pages | awk '{print $2}')

    if [ "$pages" -lt 10 ]; then
        mv "$pdf" short/
    elif [ "$pages" -lt 50 ]; then
        mv "$pdf" medium/
    else
        mv "$pdf" long/
        # Split long documents
        merge-pdf split "long/$pdf" "long/split_${pdf%.pdf}/" -p 25
    fi
done
```

### Backup and Archive

```bash
#!/bin/bash
# Create dated archive of merged documents

DATE=$(date +%Y%m%d)
ARCHIVE_DIR="archive_${DATE}"
mkdir -p "$ARCHIVE_DIR"

# Merge all current PDFs
merge-pdf merge "${ARCHIVE_DIR}/combined_${DATE}.pdf" *.pdf

# Also keep individual copies
cp *.pdf "$ARCHIVE_DIR/"

echo "Archive created: $ARCHIVE_DIR"
```

---

## Python API Examples

### Basic Python Usage

```python
from merge_pdf import merge, extract_pages, rotate_pages
from pathlib import Path

# Merge documents
files = ["intro.pdf", "chapter1.pdf", "chapter2.pdf"]
merge(files, "book.pdf")

# Extract pages
extract_pages("book.pdf", "sample.pdf", [1, 5, 10])

# Rotate pages
rotate_pages("scanned.pdf", "fixed.pdf", 90)
```

### Advanced Python Workflows

```python
from merge_pdf import merge_pattern, split_pdf
from pathlib import Path

def create_comparison_document(original, revised, output):
    """Create interleaved comparison of two documents."""
    from pypdf import PdfReader

    # Get page counts
    orig_pages = len(PdfReader(original).pages)
    rev_pages = len(PdfReader(revised).pages)

    # Build pattern
    pattern = []
    for i in range(1, min(orig_pages, rev_pages) + 1):
        pattern.append((original, i, i))
        pattern.append((revised, i, i))

    merge_pattern(pattern, output)
    print(f"Created comparison document: {output}")

# Use the function
create_comparison_document("draft1.pdf", "draft2.pdf", "comparison.pdf")
```

### Batch Processing with Python

```python
from pathlib import Path
from merge_pdf import rotate_pages, extract_pages

def process_directory(input_dir, output_dir):
    """Process all PDFs in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    for pdf in input_path.glob("*.pdf"):
        print(f"Processing {pdf.name}...")

        # Extract first page
        cover = output_path / f"cover_{pdf.name}"
        extract_pages(pdf, cover, [1])

        # Rotate if needed
        rotated = output_path / f"rotated_{pdf.name}"
        rotate_pages(pdf, rotated, 90)

# Process documents
process_directory("input/", "output/")
```

### Custom Document Builder

```python
from merge_pdf import merge_pattern
from pathlib import Path

class DocumentBuilder:
    """Build custom documents from multiple sources."""

    def __init__(self):
        self.pattern = []

    def add_pages(self, file, start, end=None):
        """Add pages from a file."""
        if end is None:
            end = start
        self.pattern.append((file, start, end))
        return self

    def add_document(self, file):
        """Add entire document."""
        from pypdf import PdfReader
        pages = len(PdfReader(file).pages)
        self.pattern.append((file, 1, pages))
        return self

    def build(self, output):
        """Build the final document."""
        merge_pattern(self.pattern, output)
        print(f"Built document with {len(self.pattern)} sections")

# Use the builder
builder = DocumentBuilder()
builder.add_pages("cover.pdf", 1) \
       .add_pages("intro.pdf", 1, 3) \
       .add_document("main.pdf") \
       .add_pages("appendix.pdf", 1, 10) \
       .build("final.pdf")
```

### Error Handling

```python
from merge_pdf import merge, extract_pages
from pathlib import Path

def safe_merge(files, output):
    """Merge with error handling."""
    try:
        # Verify all files exist
        for file in files:
            if not Path(file).exists():
                print(f"Error: {file} not found")
                return False

        # Perform merge
        merge(files, output)
        print(f"Successfully created {output}")
        return True

    except ValueError as e:
        print(f"Invalid input: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Use safe merge
files = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
safe_merge(files, "output.pdf")
```

---

## Real-World Use Cases

### Academic Papers

```bash
# Combine paper sections
merge-pdf merge paper.pdf \
    title_page.pdf \
    abstract.pdf \
    introduction.pdf \
    methodology.pdf \
    results.pdf \
    discussion.pdf \
    references.pdf
```

### Legal Documents

```bash
# Assemble contract with exhibits
merge-pdf merge complete_contract.pdf \
    main_agreement.pdf \
    exhibit_a.pdf \
    exhibit_b.pdf \
    signature_pages.pdf
```

### Business Reports

```bash
# Create quarterly report
merge-pdf pattern Q1_2024_Report.pdf \
    -s cover.pdf:1 \
    -s executive_summary.pdf:1-2 \
    -s financial_data.pdf:1-15 \
    -s market_analysis.pdf:1-10 \
    -s projections.pdf:1-5
```

### Photo Books

```bash
# Combine photo pages
merge-pdf merge photo_album.pdf page_*.pdf

# Or with specific order
merge-pdf merge album.pdf \
    cover.pdf \
    page_01.pdf \
    page_02.pdf \
    page_03.pdf \
    back_cover.pdf
```

---

## Tips and Best Practices

1. **Test First**: Test commands on copies before processing originals
2. **Use Descriptive Names**: Name output files clearly
3. **Check Page Counts**: Verify page numbers before extracting
4. **Backup Originals**: Keep copies of original files
5. **Automate Repetitive Tasks**: Use scripts for batch operations
6. **Validate Output**: Check merged PDFs before deleting sources

---

## See Also

- [CLI Documentation](cli.md) - Complete command reference
- [API Documentation](api.md) - Python API reference
- [README](../README.md) - Project overview

