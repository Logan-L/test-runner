# Test Runner
The Test Runner stores and executes [Python](https://www.python.org/doc/) test cases using [Behave](https://behave.readthedocs.io/en/stable/index.html) and generates test reports using [Allure](https://allurereport.org/docs/).

## Testing ([Behave](https://behave.readthedocs.io/en/stable/install.html))
### Runs all tests
```bash
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results
```

### Run tagged tests
```bash
# Run tests with the specified tag.
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results --tags @test
```
```bash
# Run tests without the specified tag.
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results --tags ~@test
```
```bash
# Run tests with the specified tags. Represents logical operator "OR".
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results --tags @test1,@test2
```
```bash
# Run tests with or without and with the specified tags. Represents logical operator "AND".
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results --tags @test1,~@test2 --tags @test3
```
```bash
# Run tests without the specified tags. Represents logical operator "AND".
behave --no-capture -f allure_behave.formatter:AllureFormatter -o results --tags ~@test1 --tags ~@test2
```

## Reporting ([Allure](https://allurereport.org/docs/))
### Generate the allure report (without history)
```bash
allure generate results -o reports --single-file --clean
```
### Generate the allure report (with history)
```bash
allure generate results -o reports --clean
cp -r reports/history/ results/history/
allure generate results -o reports --single-file --clean
```

## Virtual Environment (.venv)
### Create the virtual environment

```bash
# If python defaults to the correct version.
python -m venv .venv
```
```bash
# If python does not default to the correct version.
python3 -m venv .venv
```

### Activate the virtual environment
```bash
# Windows (CMD):
.venv\Scripts\activate
```
```bash
# macOS/Linux:
source .venv/bin/activate
```

### Deactivate the virtual environment
```bash
# Windows (CMD):
deactivate
```
```bash
# macOS/Linux:
deactivate # or source deactivate
```

### Generate requirements file
```bash
pip freeze > requirements.txt
```

### Install package(s) from requirements file
```bash
pip install -r requirements.txt
```
