import nbformat
from nbconvert import TeXExporter

# Define input and output file paths
input_file = 'input.tex'
output_file = 'output.ipynb'

# Read in the LaTeX file
with open(input_file, 'r') as f:
    latex_text = f.read()

# Convert the LaTeX to a Notebook
exporter = TeXExporter()
(body, resources) = exporter.from_notebook_node(nbformat.v4.new_notebook(), latex_text)

# Write the Notebook to file
with open(output_file, 'w') as f:
    f.write(body)
