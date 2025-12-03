# Quick Start Guide

Get started with merge-pdf in under 5 minutes!

## Installation

```bash
pip install merge-pdf
```

## Basic Usage

### 1. Merge PDFs

Combine multiple PDFs into one:

```bash
merge-pdf merge combined.pdf file1.pdf file2.pdf file3.pdf
```

### 2. Split a PDF

Divide a PDF into separate files:

```bash
# Split into individual pages
merge-pdf split large.pdf output_folder/

# Split into 10-page chunks
merge-pdf split large.pdf output_folder/ --pages-per-file 10
```

### 3. Rotate Pages

Fix page orientation:

```bash
# Rotate all pages 90° clockwise
merge-pdf rotate input.pdf output.pdf --angle 90

# Rotate specific pages
merge-pdf rotate input.pdf output.pdf --angle 180 --pages 1,3,5
```

### 4. Extract Pages

Pull out specific pages:

```bash
# Extract pages 1, 3, and 5
merge-pdf extract input.pdf output.pdf --pages 1,3,5

# Extract a range
merge-pdf extract input.pdf output.pdf --pages 1-10

# Mix ranges and individual pages
merge-pdf extract input.pdf output.pdf --pages 1,3-7,10,15-20
```

### 5. Advanced Pattern Merging

Interleave or combine specific pages from multiple PDFs:

```bash
merge-pdf pattern output.pdf \
    -s document1.pdf:1-5 \
    -s document2.pdf:1-5 \
    -s document1.pdf:6-10
```

## Python API

Use merge-pdf in your Python code:

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
merge-pdf --help

# Command-specific help
merge-pdf merge --help
merge-pdf pattern --help
merge-pdf split --help
merge-pdf rotate --help
merge-pdf extract --help
```

## Common Tasks

### Merge all PDFs in a directory

```bash
merge-pdf merge combined.pdf *.pdf
```

### Create a booklet

```bash
# Extract odd pages
merge-pdf extract document.pdf odd.pdf --pages 1,3,5,7,9

# Extract even pages
merge-pdf extract document.pdf even.pdf --pages 2,4,6,8,10
```

### Interleave two documents

```bash
merge-pdf pattern comparison.pdf \
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
- 💬 [GitHub Issues](https://github.com/jmcswain/merge-pdf/issues)
- 🌟 [GitHub Repository](https://github.com/jmcswain/merge-pdf)

---

Happy PDF merging! 🎉

