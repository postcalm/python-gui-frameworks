import os


def main():
    here = os.path.dirname(__file__)
    os.system(f"flet run -d {here}/Flet")


if __name__ == '__main__':
    main()
