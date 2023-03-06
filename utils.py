def get_repo(data, repo_name):
    return list(filter(lambda x : x['repositories'] == repo_name, data))


def get_counts(repo):
    repo_as_dic = repo[0]
    print(repo_as_dic)
    labels = ['stars_count', 'forks_count', 'issues_count', 'pull_requests']
    values = []
    for e in labels:
        values.append(int(repo_as_dic[e]))  
    return labels, values


def repo_issues_python(data):
    data = list(filter(lambda  item: item.get('language') ==  'Python', data))

    repos = list(map(lambda item: item.get('repositories'), data))
    issues= list(map(lambda item: int(item.get('issues_count')), data)) 

    labels = repos
    values = issues
    
    return labels, values


