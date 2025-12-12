pytest -s -v -n=2 -m "sanity" --html=./Reports/report_1.html testCases --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report_1.html testCases --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/report_1.html testCases --browser firefox
rem pytest -s -v -n=3 -m "regression" --html=./Reports/report_1.html testCases --browser firefox