"""
QUESTION:
You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as $\mbox{0}$.

Input Format

The first line contains $N$, the number of lines in the XML document. 

The next $N$ lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

Sample Input  

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output  

1

Explanation

Here, the root is a feed tag, which has depth of $\mbox{0}$. 

The tags title, subtitle, link and updated all have a depth of $\mbox{1}$. 

Thus, the maximum depth is $\mbox{1}$.
"""

import xml.etree.ElementTree as etree

def calculate_max_xml_nesting_depth(xml_document: str) -> int:
    """
    Calculate the maximum level of nesting in a given XML document.

    Parameters:
    xml_document (str): A string containing the entire XML document.

    Returns:
    int: The maximum level of nesting in the XML document.
    """
    # Parse the XML document
    tree = etree.ElementTree(etree.fromstring(xml_document))
    
    def walk(root):
        children = [child for child in root]
        if len(children) == 0:
            return 0
        return 1 + max((walk(child) for child in root))
    
    # Get the root of the tree and calculate the maximum nesting depth
    return walk(tree.getroot())