# import pytest
from src.utils.StringOperations import StringOperations

stringOperations = StringOperations()

# @pytest.mark.parametrize(
#     ("param1", "param2"),
#     [
#         ("a", "b"),
#         ("c", "d"),
#     ],
# )
# class TestGroup:
#     """A class with common parameters, `param1` and `param2`."""

#     @pytest.fixture
#     def fixt(self) -> int:
#         """This fixture will only be available within the scope of TestGroup"""
#         return 123

#     def test_one(self, param1: str, param2: str, fixt: int) -> None:
#         print("\ntest_one", param1, param2, fixt)

#     def test_two(self, param1: str, param2: str) -> None:
#         print("\ntest_two", param1, param2)
    
def test_makeBoldHero():
        testData = "**Summary:**"
        outputData = "**Summary:**"

def test_addLineBreak():
    testData = """## Development Pipeline Status Report 

**Date:** 2024-08-04

**To:** Delivery Managers and Tech Leads

**Subject:** Recent Pipeline Executions Overview

This report summarizes the outcome of recent development pipelines across different branches, offering insights into the progression of software releases:

**Key Observations:**

* **Development Branch:**  All recent pipeline executions on the 'development' branch have been **successful**. These pipelines were triggered by both scheduled processes and code pushes, indicating a healthy rhythm of continuous integration and deployment.
* **Staging Environment:** Deployments to the 'staging' environment were also consistently **successful**. This points to a stable pipeline and potentially a well-prepared release candidate.
* **SIT (System Integration Testing):**  The 'sit' environment saw a number of **successful** pipeline executions triggered by code pushes. This suggests active integration testing is underway, ensuring the quality of features before broader deployment. 
* **Master Branch (Production):** Pipelines targeting the 'master' branch, likely representing production deployments, have been consistently **successful**. This demonstrates a robust release process with high reliability.

**Recommendations:**

* Continue to monitor pipelines for any unexpected failures or regressions.
* Review the performance of pipelines to identify potential bottlenecks and optimize for faster feedback loops.

This report provides a high-level overview of recent pipeline activity.  For more detailed information on specific pipeline executions, please refer to the pipeline logs in our CI/CD system."""
    outputData = """## Development Pipeline Status Report 

**Date:** 2024-08-04
<br />
**To:** Delivery Managers and Tech Leads
<br />
**Subject:** Recent Pipeline Executions Overview
<br />
This report summarizes the outcome of recent development pipelines across different branches, offering insights into the progression of software releases:

**Key Observations:**

* **Development Branch:**  All recent pipeline executions on the 'development' branch have been **successful**. These pipelines were triggered by both scheduled processes and code pushes, indicating a healthy rhythm of continuous integration and deployment.
<br />* **Staging Environment:** Deployments to the 'staging' environment were also consistently **successful**. This points to a stable pipeline and potentially a well-prepared release candidate.
<br />* **SIT (System Integration Testing):**  The 'sit' environment saw a number of **successful** pipeline executions triggered by code pushes. This suggests active integration testing is underway, ensuring the quality of features before broader deployment. <br />
* **Master Branch (Production):** Pipelines targeting the 'master' branch, likely representing production deployments, have been consistently **successful**. This demonstrates a robust release process with high reliability.
<br />
**Recommendations:**

* Continue to monitor pipelines for any unexpected failures or regressions.
<br />* Review the performance of pipelines to identify potential bottlenecks and optimize for faster feedback loops.
<br />
This report provides a high-level overview of recent pipeline activity.  For more detailed information on specific pipeline executions, please refer to the pipeline logs in our CI/CD system."""
    # print(stringOperations.addLineBreaks(testData))
    assert stringOperations.addLineBreaks(testData) == outputData