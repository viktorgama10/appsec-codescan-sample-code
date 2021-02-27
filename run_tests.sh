pytest -v --junitxml=test_report.xml --cov-report xml --cov  src/app/
coverage xml -i
