import random       # in standard Python library

# User Class
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

# Teacher - child class
class Teacher(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name,email)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    # teach - instance method
    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]

# Student - child class
    def __init__(self, first_name, last_name, email,gpa):
        super().__init__(first_name, last_name,email)
        self.gpa = gpa
        self.knowledge = []

    # learn - instance method
    def learn(self, knowledge_string):
        self.knowledge.append(knowledge_string)



sandy = Teacher("Sandy", "Smith", "sandy.smith@uni.edu")
bob = Student("Bob", "Dylan", "bob.dylan11@uni.edu", 3.4)
millie = Student("Millie", "Brown", "millie.brown4@uni.edu", 3.8)

bob.learn(sandy.teach())
bob.learn(sandy.teach())
bob.learn(sandy.teach())
print("Millie's knowledge")
print(millie.knowledge)
print("Bob's knowledge")
print(bob.knowledge)