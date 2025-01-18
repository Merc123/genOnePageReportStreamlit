import os

import pandas as pd
import streamlit as st
from PIL import Image
from jinja2 import Template

# Function to extract text under a specified tag for Analysis
def extract_text_from_analysis_file(file_path, tag):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
      if line.strip() == f"[{tag}]":
        # Return the text below the tag (if it exists)
        return lines[i + 1].strip() if i + 1 < len(lines) else None
  return None

group = 'Analysis1'
df_analysis = pd.read_csv(os.path.join(group + ".csv"))
title_name = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Title_Name"))
logo_path = st.image(Image.open(os.path.join("logo.png")))
summary_title_name = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Summary_Title_Name"))
summary_text = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Summary_Text"))
kpi_title_name = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "KPI_Title_Name"))
kpi_data = st.write(df_analysis[["x1", "y1", "z1", "x2"]].tail(1))
chart_title_name = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Chart_Title_Name"))
chart_path = st.image(Image.open(os.path.join(group + ".png")))
chart_writeup = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Chart_Writeup"))
datatable_tile_name = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "DataTable_Tile_Name"))
data_table = st.write(df_analysis)
footer_text = st.write(extract_text_from_analysis_file(os.path.join(group + ".txt"), "Footer_Text"))

# Render the template with the report content
template = Template(os.path.join(group + ".html"))
context = {
  'title_name' : title_name,
  'logo_path' : logo_path,
  'summary_title_name' : summary_title_name,
  'summary_text' : summary_text,      
  'kpi_title_name' : kpi_title_name,
  'kpi_data' : kpi_data,
  'chart_title_name' : chart_title_name,
  'chart_path' : chart_path,
  'chart_writeup': chart_writeup,      
  'datatable_tile_name' : datatable_tile_name,
  'data_table' : data_table,
  'footer_text' : footer_text
}
rendered_html = template.render(context)

# Save the rendered report to an HTML file
with open("executive_summary_report.html", "w") as file:
    file.write(rendered_html)

