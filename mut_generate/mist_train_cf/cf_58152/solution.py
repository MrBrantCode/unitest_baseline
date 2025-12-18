"""
QUESTION:
Implement a function called `generate_report` that takes a report format as input and generates a report in the specified format. The function should be designed in a way that new report formats can be added without modifying the existing code. The report format should be specified as a string, and the function should return a string indicating the report has been generated in the specified format. The function should initially support generating reports in 'pdf' format.
"""

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReportGenerator(ReportGenerator):
    def generate(self):
        return "Report generated in PDF format"

def generate_report(report_format):
    report_generators = {
        'pdf': PDFReportGenerator(),
        # Add new report formats here without modifying existing code
        # 'word': WordReportGenerator(),
        # 'excel': ExcelReportGenerator(),
    }

    if report_format in report_generators:
        return report_generators[report_format].generate()
    else:
        return "Unsupported report format"