"""
QUESTION:
Implement the `download_gene_reference` function, which takes a list of fields as input and returns a string representing the Ensembl REST API query in TSV format. The query should include the provided fields as `<Attribute>` elements. The function should not make any actual API calls, but rather construct the query string based on the input fields. The query string should be in the format specified in the example output. The input fields are specified as a list of strings, and the output should be a string.
"""

from typing import List

def download_gene_reference(fields: List[str]) -> str:
    query_template = '''
<Query  virtualSchemaName = "default" formatter = "TSV" header = "1"
        uniqueRows = "0" count = "" datasetConfigVersion = "0.6" >
    <Dataset name = "hsapiens_gene_ensembl" interface = "default" >
''' + '\n'.join(['<Attribute name = "{}" />'.format(f) for f in fields]) + '''
    </Dataset>
</Query>'''
    return query_template