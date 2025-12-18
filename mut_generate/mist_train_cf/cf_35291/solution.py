"""
QUESTION:
Implement a function `simulate_write` that takes four parameters: `row`, `col`, `invoice_origin`, and `post_exectas`, and returns a string representing the value that should be written to the specified cell in an Excel file based on the given conditions.

The function should consider the following conditions:
- If `invoice_origin` is not empty, write its value to the cell at `row`, `col + 10`.
- If `post_exectas` is 1, write 0 to the cell at `row`, `col + 11`.
- If `invoice_origin` is empty and `post_exectas` is 0, write "No invoice origin and not reimbursed" to the cell at `row`, `col + 10`.

The function signature should be `def simulate_write(row: int, col: int, invoice_origin: str, post_exectas: int) -> str`.
"""

def simulate_write(row: int, col: int, invoice_origin: str, post_exectas: int) -> str:
    if invoice_origin:  
        return str(invoice_origin)  
    elif post_exectas == 1:  
        return "0"  
    else:  
        return "No invoice origin and not reimbursed"