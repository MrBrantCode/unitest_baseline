"""
QUESTION:
Implement a function `manage_test_scenarios` that centrally manages test specifications, combines them into test coverage scenarios, tracks progress, links test specs with bug reports, and generates progress reports. The function should meet the following requirements:

- Store test specifications in text format
- Combine test specs into test coverage scenarios
- Track the progress through testing scenarios
- Link test specs with bug reports
- Generate progress reports
- Be centrally managed on its own without relying on external software or hacks/extensions.
"""

class TestScenarioManager:
    def __init__(self):
        self.test_specs = {}
        self.test_scenarios = {}
        self.bug_reports = {}
        self.progress = {}

    def add_test_spec(self, spec_id, spec_text):
        self.test_specs[spec_id] = spec_text

    def combine_specs_into_scenarios(self, scenario_id, spec_ids):
        self.test_scenarios[scenario_id] = [self.test_specs[spec_id] for spec_id in spec_ids]

    def track_progress(self, scenario_id, progress_status):
        self.progress[scenario_id] = progress_status

    def link_spec_with_bug_report(self, spec_id, bug_report_id):
        if spec_id in self.test_specs:
            self.bug_reports[spec_id] = bug_report_id

    def generate_progress_report(self):
        report = ""
        for scenario_id, progress_status in self.progress.items():
            report += f"Scenario {scenario_id}: {progress_status}\n"
        return report


def manage_test_scenarios(test_specs, test_scenarios, bug_reports):
    manager = TestScenarioManager()
    
    for spec_id, spec_text in test_specs.items():
        manager.add_test_spec(spec_id, spec_text)

    for scenario_id, spec_ids in test_scenarios.items():
        manager.combine_specs_into_scenarios(scenario_id, spec_ids)

    for spec_id, bug_report_id in bug_reports.items():
        manager.link_spec_with_bug_report(spec_id, bug_report_id)

    return manager