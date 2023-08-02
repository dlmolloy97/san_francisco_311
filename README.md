# Project overview

## Project description
This repository compiles work done with a dbt project with data from the City of San Francisco's 311 service requests. The data is available on [SF OpenData](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6). The project is a work in progress and is not yet complete.

## Project structure

The project is structured as follows:

```
├── README.md          <- The top-level README for developers using this project.
├── data
│-─ dbt_san_francisco_311        <- Directory for dbt modules
    ├── models
    │   ├── base
    │   ├── analytics
    │   ├── features
    ├── docs
    ├── examples
    ├── logs
    ├── models
    ├── notebooks
    ├── reports
    ├── sf311
    ├── tests
    ├── .gitignore
    ├── dbt_creation.sh
    ├── newshell.sh
    ├──pyproject.toml

```

## How to use this project

### Requirements

- [dbt](https://docs.getdbt.com/docs/installation)
- [Python](https://www.python.org/downloads/)

### Installation

1. Clone this repository
2. Create a virtual environment
3. Install the requirements
4. Run the dbt project

### Running the dbt project

1. Activate the virtual environment
2. Run the dbt project with the following command:

```
dbt run
```
3. Test the dbt project with the following command:

```
dbt test
```

### Generating the documentation
1. Generate the documentation with the following command:

```
cd docs
make html
```
### Viewing the documentation
1. Open the index.html file in the _build directory in a browser

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgements

- [dbt](https://www.getdbt.com/)
- [SF OpenData](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6)
- [dbt documentation](https://docs.getdbt.com/docs/introduction)
- [dbt Discourse](https://discourse.getdbt.com/)
- [dbt Slack](https://community.getdbt.com/)
- [dbt Learn](https://learn.getdbt.com/)
- [dbt Tutorials](https://docs.getdbt.com/tutorial/setting-up)
- [dbt Cloud](https://cloud.getdbt.com/)
