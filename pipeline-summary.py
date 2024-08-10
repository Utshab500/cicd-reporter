import argparse
import json
import warnings
warnings.filterwarnings("ignore")


from src.utils.Converter import Converter
from src.modules.ReportGenerator import ReportGenerator

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
    response = ReportGenerator().generateReport(args.response)
    print(response)
