import unittest
from unittest.mock import Mock
import azure.functions as func
from __init__ import main

# Testing counter function
class TestAzureFunction(unittest.TestCase):
    def test_main_function(self):
        # Create mock input data
        request = func.HttpRequest(
            method='GET',
            url='http://localhost',
            params={'count': '2'},
            body=b'',
        )
        input_document = func.DocumentList([func.Document.from_dict({'count': 2})])
        output_document = Mock()

        # Call the main function
        response = main(request, input_document, output_document)

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_body().decode('utf-8'), '3')
        output_document.set.assert_called_once_with(func.Document.from_json(input_document[0].to_json()))

if __name__ == '__main__':
    unittest.main()
