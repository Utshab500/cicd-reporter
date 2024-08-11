import re
import copy

from src.utils.StringOperations import StringOperations

class ReportFormatter:
    def __init__(self):
        pass

    def geminiReportTohtml(self, data):
        # print(data)
        with open('my_file.txt', 'w') as file:
            file.write(data)

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