# Pokemon API Project
This project is a Python based Restful API that returns data from a cloud-based CSV file about starter Pokemon
# Technologies
## IDE
Visual Studio Code
## Programming Language
Python
## Link to CSV file
"https://storageguest13.blob.core.windows.net/starterpokemon/PokemonStarterDB.csv"
## Libraries used

- pandas
- flask
- flask restful
- poetry
- poetry new <project name>

## Installing libraries
```bash
$ pip install pandas
```
```bash
$ pip install flask
```

## Useful Git commands

Getting branches from a Repo
- git checkout -b <branch name> --> create a new branch and move to that branch
- git checkout <branch name> --> move to a branch

Pushing changes to a Repo
- git status --> shows the files that are staged/unstaged
- git add * --> stage all files in project
- git status --> check again to make sure all files are staged
- git commit -m <"message"> --> send the staged files to repository
- git push origin <branch name> --> Finalize changed and send them to your branch