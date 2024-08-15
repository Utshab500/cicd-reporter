import google.generativeai as genai
import os

class ReportGenerator:
    def __init__(self):
        pass

    def generateReport(self, data):
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
        return response