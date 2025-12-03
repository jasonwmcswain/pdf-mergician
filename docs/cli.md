# Command-Line Interface Documentation

The `merge-pdf` CLI provides a user-friendly interface for all PDF manipulation operations.

## Installation

```bash
pip install merge-pdf
```

After installation, the `merge-pdf` command will be available in your terminal.

---

## Global Options

```bash
merge-pdf [OPTIONS] COMMAND [ARGS]...
```

**Options:**
- `--version` - Show version and exit
- `-h, --help` - Show help message and exit

**Example:**
```bash
merge-pdf --version
merge-pdf --help
```

---

## Commands

### merge

Merge multiple PDF files into one.

**Usage:**
```bash
merge-pdf merge [OPTIONS] OUTPUT FILES...
```

**Arguments:**
- `OUTPUT` - Path to the output PDF file (required)
- `FILES...` - One or more PDF files to merge (required)

**Options:**
- `--no-metadata` - Don't preserve metadata from the first PDF

**Examples:**

```bash
# Basic merge
merge-pdf merge output.pdf file1.pdf file2.pdf file3.pdf

# Merge all PDFs in current directory
merge-pdf merge combined.pdf *.pdf

# Merge with explicit paths
merge-pdf merge /path/to/output.pdf /path/to/file1.pdf /path/to/file2.pdf

# Merge without preserving metadata
merge-pdf merge output.pdf doc1.pdf doc2.pdf --no-metadata

# Merge PDFs from different directories
merge-pdf merge output.pdf docs/intro.pdf chapters/*.pdf appendix.pdf
```

**Output:**
```
ℹ Merging 3 PDF file(s)...
✓ Created output.pdf (1234.5 KB)
```

---

### pattern

Advanced pattern-based merging with precise page control.

**Usage:**
```bash
merge-pdf pattern [OPTIONS] OUTPUT
```

**Arguments:**
- `OUTPUT` - Path to the output PDF file (required)

**Options:**
- `-s, --spec PATTERN` - Pattern specification: `FILE:START-END` (can be used multiple times, required)

**Pattern Format:**
- `FILE:START-END` - Extract pages START through END from FILE
- `FILE:PAGE` - Extract single PAGE from FILE
- Pages are 1-based (first page is 1, not 0)
- Ranges are inclusive on both ends

**Examples:**

```bash
# Interleave pages from two documents
merge-pdf pattern output.pdf \
    -s A.pdf:1-5 \
    -s B.pdf:1-5 \
    -s A.pdf:6-10 \
    -s B.pdf:6-10

# Extract and combine specific pages
merge-pdf pattern output.pdf \
    -s report.pdf:1 \
    -s data.pdf:5-10 \
    -s report.pdf:20

# Combine cover pages
merge-pdf pattern covers.pdf \
    -s doc1.pdf:1 \
    -s doc2.pdf:1 \
    -s doc3.pdf:1

# Create custom document from multiple sources
merge-pdf pattern custom.pdf \
    -s intro.pdf:1-3 \
    -s chapter1.pdf:1-10 \
    -s chapter2.pdf:1-15 \
    -s conclusion.pdf:1-5

# Single page from each document
merge-pdf pattern summary.pdf \
    -s report1.pdf:1 \
    -s report2.pdf:1 \
    -s report3.pdf:1
```

**Output:**
```
ℹ Merging with 4 pattern specification(s)...
✓ Created output.pdf (567.8 KB)
```

**Common Use Cases:**

1. **Interleaving Documents** - Alternate pages from two documents
2. **Custom Compilations** - Build documents from specific sections
3. **Cover Collections** - Extract first pages from multiple documents
4. **Reordering** - Rearrange pages in custom order

---

### split

Split a PDF into multiple files.

**Usage:**
```bash
merge-pdf split [OPTIONS] INPUT_FILE OUTPUT_DIR
```

**Arguments:**
- `INPUT_FILE` - The PDF file to split (required)
- `OUTPUT_DIR` - Directory where split files will be saved (required)

**Options:**
- `-p, --pages-per-file INTEGER` - Number of pages per output file (default: 1, min: 1)

**Examples:**

```bash
# Split into individual pages
merge-pdf split large.pdf output_dir/

# Split into 10-page chunks
merge-pdf split document.pdf chunks/ --pages-per-file 10

# Split into 5-page sections
merge-pdf split book.pdf chapters/ -p 5

# Split with explicit paths
merge-pdf split /path/to/large.pdf /path/to/output/
```

**Output:**
```
ℹ Splitting PDF with 10 page(s) per file...
✓ Created 5 file(s) in chunks/
ℹ Files created:
  • large_001.pdf
  • large_002.pdf
  • large_003.pdf
  • large_004.pdf
  • large_005.pdf
```

**Output File Naming:**
Files are named: `{original_name}_{number:03d}.pdf`

Examples:
- `document_001.pdf`
- `document_002.pdf`
- `document_003.pdf`

---

### rotate

Rotate pages in a PDF.

**Usage:**
```bash
merge-pdf rotate [OPTIONS] INPUT_FILE OUTPUT_FILE
```

**Arguments:**
- `INPUT_FILE` - The input PDF file (required)
- `OUTPUT_FILE` - The output PDF file (required)

**Options:**
- `-a, --angle ANGLE` - Rotation angle: 90, 180, 270, or -90 (required)
- `-p, --pages PAGES` - Comma-separated page numbers to rotate (default: all pages)

**Examples:**

```bash
# Rotate all pages 90° clockwise
merge-pdf rotate input.pdf output.pdf --angle 90

# Rotate specific pages 180°
merge-pdf rotate input.pdf output.pdf --angle 180 --pages 1,3,5

# Rotate counter-clockwise
merge-pdf rotate input.pdf output.pdf --angle -90

# Rotate a range of pages
merge-pdf rotate input.pdf output.pdf --angle 90 --pages 1,2,3,4,5

# Rotate first and last pages
merge-pdf rotate input.pdf output.pdf --angle 270 --pages 1,10
```

**Output:**
```
ℹ Rotating 3 page(s) by 90°...
✓ Created output.pdf
```

**Valid Angles:**
- `90` - Clockwise 90°
- `180` - 180° (upside down)
- `270` - Clockwise 270° (same as -90°)
- `-90` - Counter-clockwise 90°

---

### extract

Extract specific pages from a PDF.

**Usage:**
```bash
merge-pdf extract [OPTIONS] INPUT_FILE OUTPUT_FILE
```

**Arguments:**
- `INPUT_FILE` - The input PDF file (required)
- `OUTPUT_FILE` - The output PDF file (required)

**Options:**
- `-p, --pages PAGES` - Comma-separated page numbers or ranges (required)

**Page Specification Format:**
- Individual pages: `1,3,5`
- Ranges: `1-10`
- Mixed: `1,3-7,10,15-20`

**Examples:**

```bash
# Extract specific pages
merge-pdf extract input.pdf output.pdf --pages 1,3,5,7

# Extract a range
merge-pdf extract input.pdf output.pdf --pages 1-10

# Mix ranges and individual pages
merge-pdf extract input.pdf output.pdf --pages 1,3-7,10,15-20

# Extract just the first page
merge-pdf extract input.pdf cover.pdf --pages 1

# Extract last few pages
merge-pdf extract input.pdf appendix.pdf --pages 95-100

# Extract non-consecutive pages
merge-pdf extract input.pdf selected.pdf --pages 2,5,8,11,14
```

**Output:**
```
ℹ Extracting 5 page(s)...
✓ Created output.pdf
```

---

## Error Messages

The CLI provides clear, user-friendly error messages:

**File Not Found:**
```
✗ Input file not found: /path/to/file.pdf
```

**Invalid Page Range:**
```
✗ Invalid range: 10-5 (start > end)
```

**Out of Range:**
```
✗ Page range 1-100 exceeds total pages (50) in document.pdf
```

**No Input Files:**
```
✗ No input files provided
```

---

## Exit Codes

- `0` - Success
- `1` - Error (file not found, invalid input, etc.)

---

## Tips & Tricks

### Using Shell Wildcards

```bash
# Merge all PDFs in current directory
merge-pdf merge combined.pdf *.pdf

# Merge PDFs matching a pattern
merge-pdf merge output.pdf chapter*.pdf

# Merge PDFs from multiple directories
merge-pdf merge output.pdf dir1/*.pdf dir2/*.pdf
```

### Piping and Scripting

```bash
# Process multiple files in a loop
for pdf in *.pdf; do
    merge-pdf rotate "$pdf" "rotated_$pdf" --angle 90
done

# Split all PDFs in a directory
for pdf in *.pdf; do
    merge-pdf split "$pdf" "split_${pdf%.pdf}/"
done

# Extract first pages from all PDFs
for pdf in *.pdf; do
    merge-pdf extract "$pdf" "cover_${pdf}" --pages 1
done
```

### Working with Paths

```bash
# Use absolute paths
merge-pdf merge /Users/name/output.pdf /Users/name/docs/*.pdf

# Use relative paths
merge-pdf merge ../output.pdf file1.pdf file2.pdf

# Use ~ for home directory
merge-pdf merge ~/Documents/output.pdf ~/Downloads/*.pdf
```

### Combining Commands

```bash
# Extract, rotate, and merge
merge-pdf extract input.pdf temp1.pdf --pages 1-5
merge-pdf rotate temp1.pdf temp2.pdf --angle 90
merge-pdf merge output.pdf temp2.pdf other.pdf
rm temp1.pdf temp2.pdf

# Split and then merge selected parts
merge-pdf split large.pdf parts/
merge-pdf merge selected.pdf parts/large_001.pdf parts/large_005.pdf
```

---

## Verbose Output

All commands provide informative output:

- **Blue (ℹ)** - Informational messages
- **Green (✓)** - Success messages
- **Yellow (⚠)** - Warning messages
- **Red (✗)** - Error messages

---

## Getting Help

```bash
# General help
merge-pdf --help

# Command-specific help
merge-pdf merge --help
merge-pdf pattern --help
merge-pdf split --help
merge-pdf rotate --help
merge-pdf extract --help
```

---

## See Also

- [Python API Documentation](api.md) - Use merge-pdf in your Python code
- [Examples](examples.md) - More usage examples
- [GitHub Repository](https://github.com/jmcswain/merge-pdf) - Source code and issues

