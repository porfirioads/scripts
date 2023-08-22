import gitlab
from gitlab.v4.objects.groups import Group, GroupSubgroup
from gitlab.v4.objects.projects import Project
from gitlab.exceptions import GitlabAuthenticationError
from datetime import datetime, timedelta

gitlab_url = input("Enter gitlab url: ")
token = input("Enter gitlab access token: ")
gl = gitlab.Gitlab(gitlab_url, private_token=token)


def list_project_branches(project: Project, padding=0):
    branches = project.branches.list(all=True)
    print(f"{' ' * padding}{project.name}")
    max_diff = 0
    max_diff_branch = ''
    for branch in branches:
        if branch.name in ['develop', 'development', 'qas', 'master', 'main']:
            commited_date = branch.commit['committed_date']
            commited_date = datetime.strptime(
                commited_date, '%Y-%m-%dT%H:%M:%S.%f%z')
            now = datetime.now(commited_date.tzinfo)
            diff = (now - commited_date).total_seconds() / 60
            if diff > max_diff:
                max_diff = diff
                max_diff_branch = branch.name
            print(
                f"{' ' * (padding + 1)}- {branch.name.ljust(11)} {branch.commit['short_id']} {commited_date}")
    print(f"{' ' * (padding + 1)}[Most outdated: {max_diff_branch}]\n")


def list_subgroups(group: Group | GroupSubgroup, padding=0):
    subgroups = group.subgroups.list(all=True)
    print(f"{' ' * padding}{group.name}\n")

    for subgroup in subgroups:
        list_subgroups(gl.groups.get(subgroup.id), padding + 1)

    projects = group.projects.list(all=True)
    for project in projects:
        list_project_branches(gl.projects.get(project.id), padding + 1)


def main():
    try:
        gl.auth()
        groups = gl.groups.list()
        print(groups)

        group_id = input("Enter group id: ")
        group = gl.groups.get(group_id)

        list_subgroups(group)

    except GitlabAuthenticationError:
        print("Authentication failed. Please check your token.")


if __name__ == "__main__":
    main()
