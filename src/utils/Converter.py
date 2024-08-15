class Converter:
    def __init__(self):
        pass
  
    def json_to_markdown_table(self, json_data):
        """Converts JSON data (list of dictionaries) to a markdown table.

        Args:
            json_data: A Python list containing dictionaries with consistent keys.

        Returns:
            A string containing the markdown representation of the JSON data as a table.

        Raises:
            ValueError: If the input data is not a list of dictionaries.
            KeyError: If a key from the first dictionary is missing in subsequent dictionaries.
        """

        if not isinstance(json_data, list):
            raise ValueError("Input data must be a list of dictionaries.")

        # Check if all dictionaries have the same keys
        if len(json_data) > 0:
            first_keys = set(json_data[0].keys())
            for item in json_data[1:]:
                if set(item.keys()) != first_keys:
                    raise KeyError("Dictionaries in the list must have the same keys.")

        # Extract headers from the first dictionary
        headers = [key for key in json_data[0].keys()]

        # Create table rows with consistent formatting
        table_rows = []
        for item in json_data:
            table_row = [str(item[key]) for key in headers]
            table_rows.append(table_row)

        # Combine headers and rows into a markdown table
        markdown_table = "| " + " | ".join(headers) + " |\n"
        markdown_table += "|-" * len(headers) + "|\n"
        for row in table_rows:
            markdown_table += "| " + " | ".join(row) + " |\n"

        return markdown_table