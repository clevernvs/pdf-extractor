import re
import pandas as pd
from io import StringIO
import os

def treat_tables(text):
    rules_search = re.compile(r"((?:\|.+|\(?:\n|\r))+)", re.MULTILINE)
    tables = rules_search.findall(text)

    return tables


def transform_markdown_in_excel(text, page_number):
    tables_in_text = treat_tables(text)
    if len(tables_in_text) > 0:
        for i, text_table in enumerate(tables_in_text):
            table = pd.read_csv(StringIO(text_table), sep="|", encoding="utf-8", engine="python")
            table = table.dropna(how="all", axis=1)
            table = table.dropna(how="all", axis=0)

            table.to_excel(f"tables/tabela-{i+1}_-_pagina-{page_number}.xlsx", index=False)


folder_of_pages = "documents"
list_pages = os.listdir(folder_of_pages)

for i, page in enumerate(list_pages):
    with open(f"documents/{page}", "r", encoding="utf-8") as archive:
        text = archive.read()
    
    page_number = i + 1
    transform_markdown_in_excel(text, page_number)
