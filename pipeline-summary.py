import google.generativeai as genai
import os
import argparse
import re
import json
import copy

from src.utils.StringOperations import StringOperations
from src.utils.Converter import Converter


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

  stringOperations = StringOperations()
  response = stringOperations.addLineBreaks(response)
  lineHero = stringOperations.findLineHero(response)
  # print(lineHero)
  lineHeropDup = copy.deepcopy(lineHero)
  # print(lineHeropDup)
  boldLineHeros = stringOperations.makeBoldHero(lineHeropDup)
  # print(boldLineHeros)
  response = stringOperations.replaceInMessage(response, lineHero, boldLineHeros)

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
    markdown = Converter().json_to_markdown_table(json.loads(args.response))
    print(markdown)
  if args.action == "summary":
    response = generateReport(args.response)
    print(response)
