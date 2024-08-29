import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-sw4tyjcYJtflJ311Sz5q2ibmMjGG0521I0BGc5Mzztg3SIT4"

from llama_parse import LlamaParse

documents = LlamaParse(result_type="markdown", parsing_instruction="This file contains texts and tables. I'd like to get only the tables from the text").load_data("resultado.pdf")

print(len(documents))

for i, page in enumerate(documents):
    with open(f"documents/pagina-{i+1}.md", "w", encoding="utf-8") as archive:
        archive.write(page.text)