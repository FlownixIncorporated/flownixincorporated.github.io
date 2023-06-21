import gender_guesser.detector as genderDetector
import random
import names
import time
import os

prevYear = 0
year = 1
day = 1

prevGen = 0
gen = 1

traits = [
    "friendly",
    "outgoing",
    "creative",
    "logical",
    "adventurous",
    "analytical",
    "charismatic",
    "compassionate",
    "confident",
    "curious"
]

compatable = [
    ['friendly', 'compassionate', 'charismatic', 'confident', 'outgoing'],
    ['logical', 'analytical', 'curious', 'creative', 'adventurous'],
]

events = [
    ['cried', 0, 10, 6, 'sad'],
    ['laughed', 0, 100, 40, 'happy'],
    ['ate', 0, 100, 50, 'happy'],

    # Events for Children
    ['attended a party', 6, 85, 1, 'excited'],
    ['learned how to ride a bike', 6, 10, 8, 'proud'],
    ['started kindergarten', 4, 6, 10, 'excited'],
    ['practised a musical instrument', 7, 90, 5, 'musical'],
    ['built a sandcastle', 6, 12, 1, 'imaginative'],
    ['won an award at school', 7, 18, 2, 'proud'],
    ['celebrated a holiday', 4, 100, 7, 'joyful'],
    
    # Events for Teenagers
    ['participated in a school play', 8, 18, 3, 'creative'],
    ['started high school', 14, 16, 8, 'nervous'],
    ['dated', 14, 20, 1, 'excited', True],
    ['worked on a group project with classmates', 14, 18, 3, 'collaborative'],
    ['went on a first group outing without adult supervision', 13, 18, 1, 'independent'],
    ['attended a school dance or prom', 16, 18, 3, 'elegant'],
    ['helped a friend through a difficult time', 15, 100, 1, 'supportive'],

    # Events for Adults
    ['went to work', 22, 95, 1, 'motivated'],
    ['bought a new home', 23, 100, 1, 'proud'],
    ['became a parent', 25, 100, 6, 'overjoyed'],
    ['celebrated an anniversary', 20, 100, 6, 'nostalgic'],
    ['started a small business', 30, 100, 4, 'entrepreneurial'],
    ['reconnected with old friends or classmates', 30, 100, 6, 'nostalgic'],
    ['retired after a fulfilling career', 60, 100, 15, 'content'],
]


def red(skk): print("\033[91m {}\033[00m" .format(skk))
def green(skk): print("\033[92m {}\033[00m" .format(skk))
def lightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def yellow(skk): print("\033[93m {}\033[00m" .format(skk))
def cyan(skk): print("\033[96m {}\033[00m" .format(skk))

startTime = time.time()
people = []


class Person:
    def __init__(self, name, dob, gender, trait, parents=None, occupation=None, relationships=None):
        self.name = name
        self.dob = dob
        self.age = year - self.dob
        self.maturity = "baby"
        self.gender = gender
        self.emotion = ""
        self.occupation = occupation if occupation is not None else ""
        self.relationships = relationships if relationships is not None else {}

        self.introvert = random.choice([True, False, False])
        self.trait = trait
        
        self.events = []

        self.children = []
        self.parents = parents if parents is not None else None

        self.gb = ""
        self.married = False
        self.marriedTo = ""
        self.friendshipAges = {
            "baby": [],
            "kid": [5, 6, 7, 8, 9],
            "child": [10, 11, 12, 13],
            "teenager": [14, 15, 16, 17],
            "young adult": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        }

    def addEvent(self, name, day):
        try:
            if name[5]:
                self.events.append(name[0] + self.gb.name)
                yellow(f"      {self.name} {name[0]} {self.gb.name} on {day}.")

        except:
            self.events.append(name[0])
            yellow(f"     {self.name} {name[0]} on {day}.")
        
        self.emotion = name[4]
    
    def update(self):
        if self.age >= 0 and self.age <= 3:
            self.maturity = "baby"
        elif self.age >= 4 and self.age <= 8:
            self.maturity = "kid"
        elif self.age >= 9 and self.age <= 12:
            self.maturity = "child"
        elif self.age >= 13 and self.age <= 17:
            self.maturity = "teenager"
        elif self.age >= 18 and self.age <= 25:
            self.maturity = "adult"

        self.age += 1

        if self.maturity in self.friendshipAges:
            if self.age in self.friendshipAges[self.maturity]:

                available_people = [person for person in people if person != self and person not in self.relationships.values()]

                if available_people:
                    friend = random.choice(available_people)
                    if friend.age in self.friendshipAges[self.maturity]:
                            if (self.gb == "" and friend.gb == ""):
                                self.relationships[friend.name] = friend
                                friend.relationships[self.name] = self
                                    
                                if (person.gender == 'Male' and friend.gender == 'Female') or (person.gender == 'Female' and friend.gender == 'Male'):
                                    green(f"     {self.name} and {friend.name} are now G/B Friends!")
                                    friend.gb = self
                                    self.gb = friend
                                else:
                                    green(f"     {self.name} and {friend.name} are now Friends!")

        if self.gb != "":
            if self.married == False:
                if self.age >= 23 and int(self.gb.age) >= 22:
                    yesOrNo = random.choice([True, True, True, True, True, True, False, False, False])
                    if yesOrNo:
                        self.married = True
                        self.marriedTo = self.gb
                        
                        self.gb.married = True
                        self.gb.marriedTo = self

                        green(f"     {self.name} and {self.gb.name} are now Married!")

        if self.married:
            if self.age >= 25 and self.gb.age >= 25:
                if len(self.children) <= 1:
                    name = names.get_first_name()
                    d = genderDetector.Detector()
                    child = Person(name, year, "None", random.choice(traits))

                    if d.get_gender(name) == "male" or d.get_gender(name) == "mostly_male":
                        child.gender = "Male"
                    elif d.get_gender(name) == "female" or d.get_gender(name) == "mostly_female":
                        child.gender = "Female"

                    self.children.append(child)
                    self.marriedTo.children.append(child)
                    people.append(Person(name, int(year + 1), child.gender, random.choice(traits), [self.name, self.marriedTo.name]))

                    pronounGender = "His" if child.gender == "Male" else "Her"
                    yesnoIntrovert = "Yes" if child.introvert == False else "No"
                    green(f"\n {child.name} is going to be born. {pronounGender} trait is {child.trait}. Introvert: {yesnoIntrovert}\n {pronounGender} mother and father is {self.gb.name} and {self.name}\n")



people = [Person("Henry", 1, 'Male', random.choice(traits)),
            Person("Alice", 4, 'Female', random.choice(traits)),
            Person("John", 3, 'Male', random.choice(traits)),
            Person("Emily", 2, 'Female', random.choice(traits)),
            ]


dynamicEvents = []

oneYear = 2 #days

for i in events:
    for ii in range(i[3]):
        dynamicEvents.append(i)

while True:
    currentTime = time.time()
    elapsedTime = currentTime - startTime

    if elapsedTime >= .05:
        for person in people:
            
            if day == oneYear + 1:
                prevYear += 1
                year += 1
                day = 1
            
            if prevYear + 1 == year and day == oneYear:
                person.update()

            if person.age == -1 and day == oneYear - 1:
                pronounGender = "His" if person.gender == "Male" else "Her"
                yesnoIntrovert = "Yes" if person.introvert == False else "No"
                green(f"\n {person.name} is going to be born. {pronounGender} trait is {person.trait}. Introvert: {yesnoIntrovert}\n")

            if person.age >= 0:
                if person.married:
                    cyan(f"{day}/{year}: \033[94m Married\033[96m ({person.maturity}) {person.name} is {person.age} years old.")
                else:
                    cyan(f"{day}/{year}: ({person.maturity}) {person.name} is {person.age} years old.")

            for i in range(random.choice([2,3,4,5])):
                event = random.choice(dynamicEvents)
            
                if person.age >= event[1] and person.age <= event[2]:
                    person.addEvent(event, f'{day}/{year}')
                else:
                    for i in dynamicEvents:
                        if person.age >= event[1] and person.age <= event[2]:
                            person.addEvent(event, f'{day}/{year}')
                            break

                        continue             

        startTime = currentTime
        day += 1

        print("\n\n\n")


    time.sleep(1)
