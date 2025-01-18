import os

import pandas as pd
import streamlit as st
from PIL import Image
from jinja2 import Template

ONE_PAGE_PROFFESIONALLY_REPORT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annual Report 2024</title>
    <style>
        @page {
          margin: 0; 
          padding: 0;
        }
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        .body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
            line-height: 1.6;
        }
        .container {
            margin: 0;
            padding: 0;
            max-width: 1200px;
            border: 1px solid #ddd;
            background-color: #fff;
            box-shadow: 0 0 5px #ccc;
        }
        .highlight {
            background-color: #f4f4f4;
            padding: 0px;
            margin: 0;
            line-height: 1;
        }
        .section {
            margin: 0;
            padding: 0;
            padding-top: 0;
            padding-bottom: 0;
            background-color: #f4f4f4;
        } 
        .header {
            color: #fff;
            text-align: center;
            font-size: 28px;
            display: flex;
            justify-content: space-between;
            background-color: #002366;
            margin: 0;
            padding: 0;
            height: 50px;
        }
        .header-name {
            font-size: 24px;
            font-weight: bold;
            color: rgb(255, 255, 255);
            padding: 0;
        }
        .header-logo img {
            height: 50px;
            width: 150px;
        }
        .kpi-table {
            margin: 0px;
            border-collapse: collapse;
            width: 100%;
            table-layout: fixed;
        }
        .kpi-table-th, .kpi-table-td {
            border: 1px solid #ddd;
            padding: 5px;
            text-align: center;
            height: 10px; 
        }
        .kpi-table-th {
            background-color: #002366;
            font-weight: bold;
            color: rgb(255, 255, 255);
        }
        .chart-table {
            margin: 0px;
            border-collapse: collapse;
            width: 100%;
        }
        .chart-table-tr, .chart-table-td, .chart-table-th {
             width: 50%;
             height: 20%;
        }
        .chart-table-td {
             width: 50%;
             height: 300%;
        }
        .image-container {
            text-align: center;
            margin: 0px;
            padding: 0px;
            font-family: Arial, sans-serif;
        }
        .image-container img {
            width: 100%;
            height: 200px;
        }
        .data-table {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
        }
        th, td {
            border: 1px solid #ddd;
            text-align: center;
            padding: 5px;
            line-height:0.5;
        }
        tr {
            height: 5px;
        }
        th {
            background-color: #002366;
            font-weight: bold;
            color: rgb(255, 255, 255);
        }
        .spacer {
            height: 175px; 
        }
        footer {
            text-align: center;
            margin: 0;
            padding: 2px;
            font-size: 12px;
            color: #666;
        }
        .page-number {
            margin: 0;
            padding: 2px;
            font-size: 12px;
            color: #999;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header Section -->
        <div class="header">
            <div class="header-name"> <h1>{{title_name}}</h1>.</div>
                <div class="header-logo">
                  <img src="file://{{logo_path}}" alt="Logo">
                </div>
        </div>  
            <!-- Summary Section -->
            <section class="highlight">
                <h2>{{summary_title_name}}</h2>
                <p> {{summary_text}}</p>
            </section>
                <!-- KPI Section -->
                <section>
                    <h2>{{kpi_title_name}}</h2>
                      <section class="kpi-table">
                        {{kpi_data}}
                      </section> 
                </section> 
                    <!-- Performance Analysis -->
                    <section>
                      <h2>{{chart_title_name}}</h2> 
                        <table class="chart-table" >
                          <tr class="chart-table-tr">
                              <td class="chart-table-td">
                                <div class="image-container">
                                  <img src="file://{{chart_path}}" alt="chart image">
                                </div>
                              </td>
                              <td class="chart-table-td">
                                <section class="highlight">
                                    <p> {{chart_writeup}}</p>
                                </section>
                              </td>
                          </tr>
                        </table>
                    </section>
                        <!-- Performance Data Table -->
                        <h2>{{datatable_tile_name}}</h2>
                          <section class="data-table">
                            {{data_table}}
                          </section> 
                              <div class="spacer"></div>
                                  <footer>
                                    {{footer_text}}
                                    <p class="page-number">Page 1</p>
                                  </footer>
    </div>
</body>
</html>
"""
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
  # 'logo_path' : logo_path,
  'summary_title_name' : summary_title_name,
  'summary_text' : summary_text,      
  'kpi_title_name' : kpi_title_name,
  # 'kpi_data' : kpi_data,
  'chart_title_name' : chart_title_name,
  # 'chart_path' : chart_path,
  'chart_writeup': chart_writeup,      
  'datatable_tile_name' : datatable_tile_name,
  # 'data_table' : data_table,
  'footer_text' : footer_text
}
rendered_html = template.render(context)

# Save the rendered report to an HTML file
with open("executive_summary_report.html", "w") as file:
    file.write(rendered_html)

