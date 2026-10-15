def greet(name):
    return f"Hello, {name}! Welcome to GitHub!"


def greet_team():
    return greet("AI for Green Team")


if __name__ == "__main__":
    print(greet_team())
