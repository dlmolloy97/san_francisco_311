bash
#!/bin/bash

# Create the dbt project
dbt init dbt_project

# Move into the project directory
cd $PROJECT_NAME

# Set the project author name in the dbt_project.yml file
#sed -i "s/author:/author: $AUTHOR_NAME/" dbt_project.yml