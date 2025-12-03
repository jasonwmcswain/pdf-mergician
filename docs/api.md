# Python API Documentation

The `merge-pdf` package provides a clean Python API for programmatic PDF manipulation. All functions are available through the main package import.

## Installation

```bash
pip install merge-pdf
```

## Quick Start

```python
from merge_pdf import merge, merge_pattern, split_pdf, rotate_pages, extract_pages

# Merge PDFs
merge(["doc1.pdf", "doc2.pdf"], "output.pdf")
```

---

## API Reference

### merge()

Merge multiple PDF files into a single PDF.

**Signature:**
```python
def merge(
    files: Sequence[PathLike],
    output: PathLike,
    *,
    preserve_metadata: bool = True
) -> None
```

**Parameters:**
- `files` (Sequence[str | Path]): A sequence of file paths to merge (in order)
- `output` (str | Path): The output file path for the merged PDF
- `preserve_metadata` (bool, optional): If True, preserve metadata from the first PDF. Default: True

**Raises:**
- `FileNotFoundError`: If any input file doesn't exist
- `ValueError`: If the files list is empty
- `pypdf.errors.PdfReadError`: If any input file is not a valid PDF

**Example:**
```python
from merge_pdf import merge

# Simple merge
merge(["file1.pdf", "file2.pdf", "file3.pdf"], "combined.pdf")

# Merge without preserving metadata
merge(["doc1.pdf", "doc2.pdf"], "output.pdf", preserve_metadata=False)

# Using Path objects
from pathlib import Path
files = [Path("docs/intro.pdf"), Path("docs/chapter1.pdf")]
merge(files, Path("output/book.pdf"))
```

---

### merge_pattern()

Merge PDFs using a pattern of (file, start_page, end_page) tuples. This allows fine-grained control over which pages from which files are merged.

**Signature:**
```python
def merge_pattern(
    pattern: Sequence[Tuple[PathLike, int, int]],
    output: PathLike
) -> None
```

**Parameters:**
- `pattern` (Sequence[Tuple[str | Path, int, int]]): A sequence of (file_path, start_page, end_page) tuples where pages are 1-based and inclusive
- `output` (str | Path): The output file path for the merged PDF

**Raises:**
- `FileNotFoundError`: If any input file doesn't exist
- `ValueError`: If pattern is empty or page ranges are invalid
- `IndexError`: If page numbers are out of range

**Example:**
```python
from merge_pdf import merge_pattern

# Interleave pages from two documents
pattern = [
    ("A.pdf", 1, 5),   # Pages 1-5 from A.pdf
    ("B.pdf", 1, 5),   # Pages 1-5 from B.pdf
    ("A.pdf", 6, 10),  # Pages 6-10 from A.pdf
    ("B.pdf", 6, 10),  # Pages 6-10 from B.pdf
]
merge_pattern(pattern, "interleaved.pdf")

# Extract specific pages from multiple sources
pattern = [
    ("report.pdf", 1, 1),      # Cover page
    ("data.pdf", 5, 10),       # Data section
    ("appendix.pdf", 1, 20),   # Full appendix
]
merge_pattern(pattern, "custom_document.pdf")

# Single page extractions
pattern = [
    ("doc1.pdf", 1, 1),
    ("doc2.pdf", 1, 1),
    ("doc3.pdf", 1, 1),
]
merge_pattern(pattern, "all_covers.pdf")
```

**Notes:**
- Pages are 1-based (like Adobe Reader), not 0-based
- Page ranges are inclusive on both ends
- The same file can appear multiple times in the pattern
- Files are cached internally to avoid reopening

---

### split_pdf()

Split a PDF into multiple files.

**Signature:**
```python
def split_pdf(
    input_file: PathLike,
    output_dir: PathLike,
    *,
    pages_per_file: int = 1
) -> List[Path]
```

**Parameters:**
- `input_file` (str | Path): The input PDF file to split
- `output_dir` (str | Path): Directory where split files will be saved
- `pages_per_file` (int, optional): Number of pages per output file. Default: 1

**Returns:**
- `List[Path]`: A list of paths to the created files

**Raises:**
- `FileNotFoundError`: If input file doesn't exist
- `ValueError`: If pages_per_file < 1

**Example:**
```python
from merge_pdf import split_pdf

# Split into individual pages
files = split_pdf("large.pdf", "output_dir/")
print(f"Created {len(files)} files")

# Split into 10-page chunks
files = split_pdf("document.pdf", "chunks/", pages_per_file=10)

# Process split files
for file_path in files:
    print(f"Created: {file_path}")
```

**Output Files:**
Files are named with the pattern: `{original_name}_{number:03d}.pdf`

Example: `document_001.pdf`, `document_002.pdf`, etc.

---

### rotate_pages()

Rotate specific pages in a PDF.

**Signature:**
```python
def rotate_pages(
    input_file: PathLike,
    output_file: PathLike,
    rotation: int,
    *,
    pages: Union[Sequence[int], None] = None
) -> None
```

**Parameters:**
- `input_file` (str | Path): The input PDF file
- `output_file` (str | Path): The output PDF file
- `rotation` (int): Rotation angle in degrees (must be multiple of 90)
- `pages` (Sequence[int] | None, optional): List of page numbers to rotate (1-based). If None, rotate all pages.

**Raises:**
- `FileNotFoundError`: If input file doesn't exist
- `ValueError`: If rotation is not a multiple of 90
- `IndexError`: If any page number is out of range

**Example:**
```python
from merge_pdf import rotate_pages

# Rotate all pages 90° clockwise
rotate_pages("input.pdf", "output.pdf", 90)

# Rotate specific pages 180°
rotate_pages("input.pdf", "output.pdf", 180, pages=[1, 3, 5])

# Rotate counter-clockwise (-90°)
rotate_pages("input.pdf", "output.pdf", -90)

# Rotate first 10 pages
rotate_pages("input.pdf", "output.pdf", 90, pages=list(range(1, 11)))
```

**Valid Rotation Angles:**
- `90` - Clockwise 90°
- `180` - 180°
- `270` - Clockwise 270° (same as -90°)
- `-90` - Counter-clockwise 90°

---

### extract_pages()

Extract specific pages from a PDF into a new file.

**Signature:**
```python
def extract_pages(
    input_file: PathLike,
    output_file: PathLike,
    pages: Sequence[int]
) -> None
```

**Parameters:**
- `input_file` (str | Path): The input PDF file
- `output_file` (str | Path): The output PDF file
- `pages` (Sequence[int]): List of page numbers to extract (1-based)

**Raises:**
- `FileNotFoundError`: If input file doesn't exist
- `ValueError`: If pages list is empty
- `IndexError`: If any page number is out of range

**Example:**
```python
from merge_pdf import extract_pages

# Extract specific pages
extract_pages("input.pdf", "output.pdf", [1, 3, 5, 7])

# Extract a range (using Python's range)
extract_pages("input.pdf", "output.pdf", list(range(1, 11)))  # Pages 1-10

# Extract in custom order
extract_pages("input.pdf", "output.pdf", [10, 5, 1])  # Reverse order

# Extract single page
extract_pages("input.pdf", "cover.pdf", [1])
```

**Notes:**
- Pages are extracted in the order specified
- You can extract the same page multiple times
- Page numbers are 1-based

---

## Type Hints

All functions include comprehensive type hints for better IDE support:

```python
from typing import Sequence, List, Tuple, Union
from pathlib import Path

PathLike = Union[str, Path]

def merge(
    files: Sequence[PathLike],
    output: PathLike,
    *,
    preserve_metadata: bool = True
) -> None: ...

def merge_pattern(
    pattern: Sequence[Tuple[PathLike, int, int]],
    output: PathLike
) -> None: ...

def split_pdf(
    input_file: PathLike,
    output_dir: PathLike,
    *,
    pages_per_file: int = 1
) -> List[Path]: ...

def rotate_pages(
    input_file: PathLike,
    output_file: PathLike,
    rotation: int,
    *,
    pages: Union[Sequence[int], None] = None
) -> None: ...

def extract_pages(
    input_file: PathLike,
    output_file: PathLike,
    pages: Sequence[int]
) -> None: ...
```

---

## Error Handling

All functions raise appropriate exceptions for error conditions:

```python
from merge_pdf import merge

try:
    merge(["file1.pdf", "file2.pdf"], "output.pdf")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Advanced Examples

### Batch Processing

```python
from pathlib import Path
from merge_pdf import merge, split_pdf

# Merge all PDFs in a directory
pdf_dir = Path("documents/")
pdf_files = sorted(pdf_dir.glob("*.pdf"))
merge(pdf_files, "combined.pdf")

# Split multiple PDFs
for pdf in pdf_files:
    output_dir = Path(f"split_{pdf.stem}")
    split_pdf(pdf, output_dir, pages_per_file=5)
```

### Custom Workflows

```python
from merge_pdf import extract_pages, merge, rotate_pages

# Extract odd and even pages
extract_pages("document.pdf", "odd.pdf", [1, 3, 5, 7, 9])
extract_pages("document.pdf", "even.pdf", [2, 4, 6, 8, 10])

# Rotate even pages
rotate_pages("even.pdf", "even_rotated.pdf", 180)

# Merge back together
merge(["odd.pdf", "even_rotated.pdf"], "final.pdf")
```

### Creating Booklets

```python
from merge_pdf import merge_pattern

# Create a booklet layout (4 pages per sheet)
# Assumes 12-page document
pattern = [
    ("doc.pdf", 12, 12), ("doc.pdf", 1, 1),   # Sheet 1 front
    ("doc.pdf", 2, 2),   ("doc.pdf", 11, 11), # Sheet 1 back
    ("doc.pdf", 10, 10), ("doc.pdf", 3, 3),   # Sheet 2 front
    ("doc.pdf", 4, 4),   ("doc.pdf", 9, 9),   # Sheet 2 back
    ("doc.pdf", 8, 8),   ("doc.pdf", 5, 5),   # Sheet 3 front
    ("doc.pdf", 6, 6),   ("doc.pdf", 7, 7),   # Sheet 3 back
]
merge_pattern(pattern, "booklet.pdf")
```

---

## Integration with pypdf

Since `merge-pdf` is built on pypdf, you can combine it with direct pypdf usage:

```python
from pypdf import PdfReader, PdfWriter
from merge_pdf import merge

# Use merge-pdf for basic operations
merge(["doc1.pdf", "doc2.pdf"], "temp.pdf")

# Then use pypdf for advanced operations
reader = PdfReader("temp.pdf")
writer = PdfWriter()

# Add custom metadata
writer.add_metadata({
    "/Title": "Combined Document",
    "/Author": "Your Name",
    "/Subject": "Merged PDFs",
})

# Copy pages
for page in reader.pages:
    writer.add_page(page)

# Write final output
with open("final.pdf", "wb") as f:
    writer.write(f)
```

---

## Performance Considerations

- **File Caching**: `merge_pattern()` caches file readers to avoid reopening files
- **Memory Usage**: Large PDFs are processed page-by-page to minimize memory usage
- **Path Resolution**: All paths are resolved and expanded automatically

---

## See Also

- [CLI Documentation](cli.md) - Command-line interface reference
- [Examples](examples.md) - More usage examples
- [pypdf Documentation](https://pypdf.readthedocs.io/) - Underlying PDF library

