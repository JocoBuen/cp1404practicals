"""
CP1404 Practical
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}"

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def run_tests(self):
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

        languages = [ruby, python, visual_basic]
        print(python)

        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

    run_tests()
