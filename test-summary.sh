#! /bin/bash

# RESP=$(curl --header "PRIVATE-TOKEN: ${PRIVATE_TOKEN}" "https://sgts.gitlab-dedicated.com/api/v4/projects/34770/pipelines")
# RESP=$(cat ./dummy-data/d1.json)
export TRACK=$(python pipeline-summary.py --action="title" "$RESP")
# echo "test"
# echo $RESP
python pipeline-summary.py --action="markdown" "$RESP" > test.md
sed -i'.back' 's/web_url/IGNORE_WEB_URL/g' test.md
sed -i'.back' 's/sha/IGNORE_SHA/g' test.md
sed -i'.back' 's/ref/COMMIT_BRANCH_NAME/g' test.md
sed -i'.back' 's/source/PIPELINE_TRIGGER/g' test.md
RESP=$(cat test.md)
export CONTENT=$(python pipeline-summary.py --action="summary" "$RESP")
# echo $CONTENT > test.txt
envsubst < $(pwd)/newsletter-template.html > newsletter.html

