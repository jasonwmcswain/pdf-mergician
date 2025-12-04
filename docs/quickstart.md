# Quick Start Guide

Get started with pdf-mergician in under 5 minutes!

## Installation

```bash
pip install pdf-mergician
```

## Basic Usage

### 1. Merge PDFs

Combine multiple PDFs into one:

```bash
pdf-mergician merge combined.pdf file1.pdf file2.pdf file3.pdf
```

### 2. Split a PDF

Divide a PDF into separate files:

```bash
# Split into individual pages
pdf-mergician split large.pdf output_folder/

# Split into 10-page chunks
pdf-mergician split large.pdf output_folder/ --pages-per-file 10
```

### 3. Rotate Pages

Fix page orientation:

```bash
# Rotate all pages 90° clockwise
pdf-mergician rotate input.pdf output.pdf --angle 90

# Rotate specific pages
pdf-mergician rotate input.pdf output.pdf --angle 180 --pages 1,3,5
```

### 4. Extract Pages

Pull out specific pages:

```bash
# Extract pages 1, 3, and 5
pdf-mergician extract input.pdf output.pdf --pages 1,3,5

# Extract a range
pdf-mergician extract input.pdf output.pdf --pages 1-10

# Mix ranges and individual pages
pdf-mergician extract input.pdf output.pdf --pages 1,3-7,10,15-20
```

### 5. Advanced Pattern Merging

Interleave or combine specific pages from multiple PDFs:

```bash
pdf-mergician pattern output.pdf \
    -s document1.pdf:1-5 \
    -s document2.pdf:1-5 \
    -s document1.pdf:6-10
```

## Python API

Use pdf-mergician in your Python code:

```python
from merge_pdf import merge, split_pdf, rotate_pages, extract_pages

# Merge PDFs
merge(["file1.pdf", "file2.pdf", "file3.pdf"], "combined.pdf")

# Split PDF
split_pdf("large.pdf", "output_folder/", pages_per_file=10)

# Rotate pages
rotate_pages("input.pdf", "output.pdf", 90, pages=[1, 3, 5])

# Extract pages
extract_pages("input.pdf", "output.pdf", [1, 3, 5, 7, 9])
```

## Getting Help

```bash
# General help
pdf-mergician --help

# Command-specific help
pdf-mergician merge --help
pdf-mergician pattern --help
pdf-mergician split --help
pdf-mergician rotate --help
pdf-mergician extract --help
```

## Common Tasks

### Merge all PDFs in a directory

```bash
pdf-mergician merge combined.pdf *.pdf
```

### Create a booklet

```bash
# Extract odd pages
pdf-mergician extract document.pdf odd.pdf --pages 1,3,5,7,9

# Extract even pages
pdf-mergician extract document.pdf even.pdf --pages 2,4,6,8,10
```

### Interleave two documents

```bash
pdf-mergician pattern comparison.pdf \
    -s original.pdf:1 -s revised.pdf:1 \
    -s original.pdf:2 -s revised.pdf:2 \
    -s original.pdf:3 -s revised.pdf:3
```

## Next Steps

- Read the [full documentation](docs/)
- Check out [more examples](docs/examples.md)
- Learn the [Python API](docs/api.md)
- Explore [CLI commands](docs/cli.md)

## Need Help?

- 📖 [Documentation](docs/)
- 💬 [GitHub Issues](https://github.com/jmcswain/pdf-mergician/issues)
- 🌟 [GitHub Repository](https://github.com/jmcswain/pdf-mergician)

---

Happy PDF merging! 🎉

