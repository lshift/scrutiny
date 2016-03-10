import github
import yaml

config = yaml.load(open("backup.yaml"))

g = github.Github(login_or_token=config["token"])

repos = [repo.name for repo in g.get_organization(config["org"]).get_repos()]
with open(config["repos"], "w") as reposfile:
	for repo in sorted(repos, key=unicode.lower):
		reposfile.write("%s\n" % repo)
