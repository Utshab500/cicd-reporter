from src.modules.ReportFormatter import ReportFormatter

reportFormatter = ReportFormatter()

def test__dataCleaning():
    testData = """## Development Pipeline Update
**To**: Delivery Managers and Tech Leads
**Date**: 2024-08-05
This newsletter provides a summary of recent development pipeline activity.
* **Staging Environment:** Deployments to the `staging` environment, triggered by both webhooks and manual actions, have also been successful.  This indicates that the latest features and bug fixes are ready for final testing.
"""
    outputData = """## Development Pipeline Update
**To:** Delivery Managers and Tech Leads
**Date:** 2024-08-05
This newsletter provides a summary of recent development pipeline activity.
* **Staging Environment:** Deployments to the `staging` environment, triggered by both webhooks and manual actions, have also been successful. This indicates that the latest features and bug fixes are ready for final testing.
"""
    print(reportFormatter.dataCleaning(testData))
    assert reportFormatter.dataCleaning(testData) == outputData