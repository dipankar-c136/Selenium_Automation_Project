pytest -v -s -m "regression"
pytest -v -s testCases/test_login_ddt.py --browser chrome
echo %PATH%
python --version
where python
where pytest
python -m site