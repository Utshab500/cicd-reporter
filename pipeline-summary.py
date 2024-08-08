import google.generativeai as genai
import os
import argparse
import re
import json
import copy

def makeBoldHero(heroList):
    for i in range(0, len(heroList)):
        heroList[i] = re.sub(r"\*\*(?=\w)", "<b>", heroList[i])
        heroList[i] = re.sub(r"\*\*(?!\w)", "</b>", heroList[i])
    return heroList

def findLineHero(msg):
    regexPattern = r"\*\*.+\*\*(?=\s*\w)"
    matches = re.findall(regexPattern, msg)
    return matches

def replaceInMessage(msg, originalList, replaceableList):
    for i in range(0, len(originalList)):
        regexPattern = re.escape(originalList[i])
        msg = re.sub(regexPattern, replaceableList[i], msg)
    return(msg)

def addLineBreaks(msg):
    regexPattern = r"\*\*.+\*\*((\s+\d+-\d+-\d+)|(\s+[\(\`\']{0,1}((\d+-\d+-\d+)|\w+\'\w+|\w+)[\)\`\']{0,1}[.,!?]*)+)"
    matches = re.finditer(regexPattern, msg)
    match = [x.group() for x in matches]
    matchWithLineBreak = [x+"<br />" for x in match]
    msg = replaceInMessage(msg, match, matchWithLineBreak)
    return msg

def json_to_markdown_table(json_data):
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


def generateReport(data):
  genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
  model = genai.GenerativeModel('gemini-1.5-pro')

  #########################################
  # * Prompt Details * #
  # Act as a Magazine reporter
  # Web url free
  # Date time free
  #########################################
  # prompt = f"""
  #     Act as a technical magazine reporter and summerise the below in a newsletter format for DMs and TLs, make it jargon and web url free and include necessary details intuitively and in a less technical format also try to avoide any table formated presentation and make it responsive webpage.

  #   Using this JSON schema:
  #     {args.response}

  #   """

  #########################################
  # * Prompt Details * #
  # Act as a Magazine reporter
  # Web url free
  # Date time free
  #########################################
  # prompt = f"""
  #     Act as a technical magazine reporter and summerize the below in a newsletter format for DMs and TLs, make it jargon, web url and clock time free and include necessary details intuitively and in a less technical format also try to avoide any table formated presentation.
  #     Using this JSON schema which is a GitLab REST API response:
  #     {args.response}

  #   """

  #########################################
  # * Prompt Details * #
  # Act as a Technical Writer
  # Web url free
  #########################################
  # prompt = f"""
  #     Act as a technical writer and summerize the below JSON data in a newsletter format for DMs and TLs, make it jargon, web url free and include necessary details intuitively and in a less technical format also try to avoide any table formated presentation.
  #     Using this JSON schema which is a GitLab REST API response:
  #     {data}

  #     """

  #########################################
  # * Prompt Details * #
  # Act as a Technical Writer
  # Web url free
  #########################################
  # prompt = f"""
  #     Act as a technical magazine reporter and summarize the below in a newsletter format for Delivery managers and Tech leads, describing how the development process is progressing depending on the "status"
  #     Using the below markdown data:
  #     ```markdown {data}```

  #     """

  #########################################
  # * Prompt Details * #
  # General report writing
  # Web url free
  #########################################
  prompt = f"""
      Write a concise reporter and summarize the below in a newsletter format for Delivery managers and Tech leads, describing how the development process is progressing depending on the "status" and avoid including data from 'id', 'iid' and 'project_id' coloumn
      Using the below markdown data:
      ```markdown {data}```

      """


  response = model.generate_content(prompt).text
  # print(response)
  with open('my_file.txt', 'w') as file:
      file.write(response)

  response = addLineBreaks(response)
  lineHero = findLineHero(response)
  # print(lineHero)
  lineHeropDup = copy.deepcopy(lineHero)
  # print(lineHeropDup)
  boldLineHeros = makeBoldHero(lineHeropDup)
  # print(boldLineHeros)
  response = replaceInMessage(response, lineHero, boldLineHeros)

  regexPattern = r"\#\#+.+"
  match = re.search(regexPattern, response)

  if match:
      captured_text = match.group()
      # print(captured_text)
  else:
      print("Text not found")

  captured_text = re.sub(r"\#\#", "<h2>", captured_text)
  response = re.sub(regexPattern, captured_text+"</h2>", response)

  response = re.sub(r"\*\*(?=\w)", "<h3>", response) # Positive look ahead
  response = re.sub(r"\*\*(?!\w)", "</h3>", response) # Negative look ahead
  response = re.sub(r"\*", "", response)

  return response

# --action = [ markdown, summary ]
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="A script with more options.")
  parser.add_argument('response', type=str, help='The curl response')
  parser.add_argument('-a', '--action', type=str, help='Specify a action')
  args = parser.parse_args()
  # print(args.action)
  if args.action == "markdown":
    markdown = json_to_markdown_table(json.loads(args.response))
    print(markdown)
  if args.action == "summary":
    response = generateReport(args.response)
    print(response)
