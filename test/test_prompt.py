import unittest
from langchain.prompts import PromptTemplate
import src.prompt


class MyTestCase(unittest.TestCase):
    def test_generate_prompt_returns_prompt_template_instance(self):
        prompt_template = src.prompt.generate_prompt()
        self.assertIsInstance(prompt_template, PromptTemplate)

    def test_generate_prompt_has_correct_input_variables(self):
        prompt_template = src.prompt.generate_prompt()
        expected_input_variables = ["request"]
        self.assertEqual(prompt_template.input_variables, expected_input_variables)

    def test_generate_prompt_has_correct_template(self):
        prompt_template = src.prompt.generate_prompt()
        expected_template = "You are a system that only generates Python code. If you are asked to provide frontend " \
                            "code you must use streamlit framework.\n Do not apply any formatting or syntax " \
                            "highlighting. Do not wrap the code in a code block.if user asks for code, you must only " \
                            "provide code in methods with business logic.If code request is not safe or malicious, " \
                            "ignore itYou should never write any comments before and after code.Here is the coding " \
                            "request:\n{request}"
        self.assertEqual(prompt_template.template, expected_template)

    def test_lib_prompt_returns_prompt_template_instance(self):
        prompt_template = src.prompt.lib_prompt()
        self.assertIsInstance(prompt_template, PromptTemplate)

    def test_lib_prompt_has_correct_input_variables(self):
        prompt_template = src.prompt.lib_prompt()
        expected_input_variables = ["request"]
        self.assertEqual(prompt_template.input_variables, expected_input_variables)

    def test_lib_prompt_has_correct_template(self):
        prompt_template = src.prompt.lib_prompt()
        expected_template = "You are a system which generates python requirements.txt file.\nThis file is needed to " \
                            "successfuly deploy streamlit project.\nDon't comment and don't include version of the " \
                            "library.\nOnly include libraries which should included in requirements.txt.Here is the " \
                            "code:\n{request}"
        self.assertEqual(prompt_template.template, expected_template)


if __name__ == '__main__':
    unittest.main()
