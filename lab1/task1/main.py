from github_data_collector import get_user_repos

if __name__ == '__main__':
    user_name = input()
    get_user_repos(user_name)