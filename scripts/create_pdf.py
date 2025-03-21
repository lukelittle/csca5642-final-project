#!/usr/bin/env python3

import os
import glob
import nbformat
from nbconvert import get_exporter
from traitlets.config import Config
from datetime import datetime

def get_notebooks_in_order():
    """Get all notebooks sorted by their numeric prefix."""
    notebooks = glob.glob("notebooks/[0-9]*.ipynb")
    return sorted(notebooks)

def merge_notebooks(notebook_files):
    """Merge multiple notebooks into one."""
    merged = None
    
    # Create title page
    title = "NBA Pattern Analysis"
    date = datetime.now().strftime("%B %Y")
    title_cell = nbformat.v4.new_markdown_cell(source=f"""
<div style="text-align: center; padding: 100px 0;">
    <h1 style="font-size: 2.5em; color: #333;">{title}</h1>
    <p style="font-size: 1.2em; color: #666; margin-top: 20px;">Final Project Report</p>
    <p style="font-size: 1.1em; color: #666; margin-top: 50px;">{date}</p>
</div>

<div style="break-after: page"></div>
""")
    
    # Create initial notebook with title
    merged = nbformat.v4.new_notebook()
    merged.cells.append(title_cell)
    
    # Add table of contents
    toc_cell = nbformat.v4.new_markdown_cell(source="""
# Table of Contents

""")
    merged.cells.append(toc_cell)
    
    # Generate TOC entries
    for fname in notebook_files:
        notebook_name = os.path.basename(fname).replace('.ipynb', '')
        section_name = ' '.join(notebook_name.split('_')[1:]).title()
        toc_cell.source += f"- [{section_name}](#{section_name.lower().replace(' ', '-')})\n"
    
    # Add page break after TOC
    merged.cells.append(nbformat.v4.new_markdown_cell(source='<div style="break-after: page"></div>'))
    
    for fname in notebook_files:
        with open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
            # Add section header
            notebook_name = os.path.basename(fname).replace('.ipynb', '')
            section_name = ' '.join(notebook_name.split('_')[1:]).title()
            header_cell = nbformat.v4.new_markdown_cell(source=f"""
<h1 id="{section_name.lower().replace(' ', '-')}">{section_name}</h1>
""")
            merged.cells.append(header_cell)
            
            # Process and append cells
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    if 'outputs' not in cell:
                        cell['outputs'] = []
                    # Skip empty code cells
                    if not cell.source.strip():
                        continue
                merged.cells.append(cell)
            
            # Add page break between notebooks
            merged.cells.append(nbformat.v4.new_markdown_cell(source='<div style="break-after: page"></div>'))
    
    return merged

def convert_to_pdf(notebook):
    """Convert notebook to PDF using webPDF exporter."""
    # Configure the webPDF exporter
    c = Config()
    
    # General options
    c.WebPDFExporter.exclude_input_prompt = True
    c.WebPDFExporter.exclude_output_prompt = True
    
    # Get the webPDF exporter
    pdf_exporter = get_exporter('webpdf')(config=c)
    
    # Convert to PDF
    pdf_data, _ = pdf_exporter.from_notebook_node(notebook)
    return pdf_data

def main():
    # Get notebooks in order
    notebooks = get_notebooks_in_order()
    if not notebooks:
        print("No notebooks found!")
        return
    
    print(f"Found {len(notebooks)} notebooks to merge:")
    for nb in notebooks:
        print(f"  - {nb}")
    
    # Merge notebooks
    print("\nMerging notebooks...")
    merged_notebook = merge_notebooks(notebooks)
    
    # Convert to PDF
    print("Converting to PDF...")
    pdf_data = convert_to_pdf(merged_notebook)
    
    # Save PDF
    output_file = 'nba_pattern_analysis.pdf'
    print(f"Saving {output_file}...")
    with open(output_file, 'wb') as f:
        f.write(pdf_data)
    
    print("Done! PDF has been created.")

if __name__ == '__main__':
    main()
