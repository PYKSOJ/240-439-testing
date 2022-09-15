def cat_and_mouse(x: int, y: int, z: int) -> str:
    return "Cat A"


if __name__ == "__main__":
    line_str = input("Enter A B C : ")
    line = map(int, line_str.split())

    result = cat_and_mouse(*line)
    print("Result", result)

    # ref: https: // shareablecode.com/snippets/python-solution-for -hackerrank-problem-cats-and -a-mouse-STnu-xVWx
