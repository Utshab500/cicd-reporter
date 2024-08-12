from src.utils.StringOperations import StringOperations

def test_addLineBreak():
    testData = """## Development Pipeline Update

        **To**: Delivery Managers and Tech Leads

        **Date**: 2024-08-04

        This newsletter provides a summary of recent development pipeline activity. 

        **Overall Pipeline Status**: All recent pipelines have been successful.

        **Deployment Status by Branch**:

        * **Development**: We've seen consistent success in our development branch pipelines, indicating a stable development process. Recent deployments have been triggered by both schedule and push events. 
        * **SIT**:  The SIT environment has also seen successful deployments, triggered by push events.
        * **Staging**: Staging deployments have been successfully completed, triggered by web events.
        * **Master**:  Successful deployments have been made to the master branch, indicating readiness for production releases. These were triggered by web events. 

        **Note**: This summary excludes specific identifying data like IDs and project details.

        Please contact the development team if you require further details."""
    outputData = """## Development Pipeline Update

        **To**: Delivery Managers and Tech Leads<br />

        **Date**: 2024-08-04<br />

        This newsletter provides a summary of recent development pipeline activity. 

        **Overall Pipeline Status**: All recent pipelines have been successful.<br />

        **Deployment Status by Branch**:<br />

        * **Development**: We've seen consistent success in our development branch pipelines, indicating a stable development process. Recent deployments have been triggered by both schedule and push events. <br />
        * **SIT**:  The SIT environment has also seen successful deployments, triggered by push events.<br />
        * **Staging**: Staging deployments have been successfully completed, triggered by web events.<br />
        * **Master**:  Successful deployments have been made to the master branch, indicating readiness for production releases. These were triggered by web events. <br />

        **Note**: This summary excludes specific identifying data like IDs and project details.<br />

        Please contact the development team if you require further details."""
    # print(StringOperations().addLineBreaks(testData))
    assert StringOperations().addLineBreaks(testData) == outputData