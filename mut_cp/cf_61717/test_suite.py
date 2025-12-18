from solution import run_python_script
### Test Cases
import unittest

class TestRunPythonScript(unittest.TestCase):
    """
    Test class for the run_python_script function.
    """

    def test_run_on_windows(self):
        """
        Test the function when the operating system is Windows.
        """
        result = run_python_script("test_script.py", "Windows")
        self.assertIn("Press Windows + R keys", result)
        self.assertIn("type 'cmd' or 'powershell'", result)
        self.assertIn("When setting up the development environment on Windows", result)

    def test_run_on_macos(self):
        """
        Test the function when the operating system is macOS.
        """
        result = run_python_script("test_script.py", "macOS")
        self.assertIn("Use ⌘ + Spacebar", result)
        self.assertIn("type 'terminal'", result)
        self.assertIn("Linux and macOS operating systems are case sensitive", result)

    def test_run_on_linux(self):
        """
        Test the function when the operating system is Linux.
        """
        result = run_python_script("test_script.py", "Linux")
        self.assertIn("Use Ctrl + Alt + T", result)
        self.assertIn("go to the Applications menu and select 'Terminal'", result)
        self.assertIn("In Linux environments, the Python command is often linked to Python2", result)
        self.assertIn("Linux and macOS operating systems are case sensitive", result)

    def test_general_precautions(self):
        """
        Test the general precautions section of the instructions.
        """
        result = run_python_script("test_script.py", "Linux")
        self.assertIn("Ensure that the script doesn't contain malicious code", result)
        self.assertIn("Always review scripts before running them", result)
        self.assertIn("It's also a good idea to have a shebang line at the top of your script", result)

if __name__ == '__main__':
    unittest.main()
