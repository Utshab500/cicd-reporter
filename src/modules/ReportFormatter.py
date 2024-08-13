import re
import copy

from src.utils.StringOperations import StringOperations

class ReportFormatter:
    def __init__(self):
        pass

    def dataCleaning(self, data):
        """
        Cleans the input data by performing basic formatting adjustments.

        Args:
            data (str): The input string to be cleaned.

        Returns:
            str: The cleaned string with the following modifications:
                - Removes extra spaces by replacing double spaces with single spaces.
                - Rearranges the order of bold text and colons.

        Example:
            >>> formatter = ReportFormatter()
            >>> input_data = "## Development Pipeline Update  \n**To**: Delivery Managers and Tech Leads\n**Date**: 2024-08-05"
            >>> cleaned_data = formatter.dataCleaning(input_data)
            >>> print(cleaned_data)
            ## Development Pipeline Update
            **To:** Delivery Managers and Tech Leads
            **Date:** 2024-08-05
        """
        data = re.sub(r"  ", " ", data)
        data = re.sub(r"\*\*\:", ":**", data)
        return data

    def geminiReportTohtml(self, data):
        # print(data)
        with open('my_file.txt', 'w') as file:
            file.write(data)

        data = self.dataCleaning(data)
        with open('clean.txt', 'w') as file:
            file.write(data)
        # print(data)
        stringOperations = StringOperations()
        data = stringOperations.addLineBreaks(data)
        lineHero = stringOperations.findLineHero(data)
        # print(lineHero)
        lineHeropDup = copy.deepcopy(lineHero)
        # print(lineHeropDup)
        boldLineHeros = stringOperations.makeBoldHero(lineHeropDup)
        # print(boldLineHeros)
        data = stringOperations.replaceInMessage(data, lineHero, boldLineHeros)

        regexPattern = r"\#\#+.+"
        match = re.search(regexPattern, data)

        if match:
            captured_text = match.group()
            # print(captured_text)
        else:
            print("Text not found")

        captured_text = re.sub(r"\#\#", "<h2>", captured_text)
        data = re.sub(regexPattern, captured_text+"</h2>", data)

        data = re.sub(r"\*\*(?=\w)", "<h3>", data) # Positive look ahead
        data = re.sub(r"\*\*(?!\w)", "</h3>", data) # Negative look ahead
        data = re.sub(r"\*", "", data)
        return data