#app is not only a folder, but a package (paquete)

import utils
import read_csv
import charts


def run():

    data = read_csv.read_csv('./my_app/data.csv')

    #Get repository name
    repo_name = input('Ingresa el nombre del repositorio ')
    result = utils.get_repo(data, repo_name.lower())

    if len(result) > 0:
        labels, values = utils.get_counts(result)

    charts.generate_bar_chart(labels, values)

    labels, values = utils.repo_issues_python(data)
    charts.generate_pie_chart(labels, values)

#If we would like this file executes itself as script, it's not enough 'python app/main.py' in shell.
#example.py has the control to start main.py. But we would like have the posibility of boot main.py by dual way, DO
#THE NEXT
if __name__ == '__main__': #Entry Point (?)
    run()