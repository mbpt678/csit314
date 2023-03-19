import random
from tradie import Tradie

first_names_male = ["James", "Robert", "John", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles",
                    "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew",
                    "Joshua", "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffery",
                    "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott",
                    "Brandon", "Benjamin", "Samuel", "Gregory", "Alexander", "Frank", "Patrick", "Raymond", "Jack",
                    "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Adam", "Nathan", "Kamaru", "Leon", "Oliver",
                    "Deiveson", "Max", "Sergio", "Kai"]
first_names_female = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah",
                      "Karen", "Lisa", "Nancy", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna",
                      "Michelle", "Laurel"]
last_names = ["Baltimore", "Biffle", "Canine", "Chia", "Felch", "Thobe", "Smith", "Johnson", "Williams", "Brown",
              "Jones", "Garcia", "Miller", "Davis", "Martinez", "Rodriguez", "Chatto", "Kelly", "Walker", "Chandler",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Silva", "Thomas", "Taylor", "Moore", "Jackson",
              "Martin", "Lee", "Perez", "White", "Usman", "Edwards", "Queen", "Moreno", "Verstappen", "Natsuki", "Hall"]

tradie_skills = ["Flooring", "Oven repair", "Plaster and gyprocking", "Painting", "Fence installation", "Fence repair",
                 "Roof plumbing", "Roof repair", "Decking", "Tree removal"]

company_fence = ["Wollongong Fencing services", "Knockout Fencing Wollongong", "Jim's Fencing"]
company_trees = ["Shane's Trees", "Burnett Trees", "Dingo's Tree services"]
company_oven = ["Wollongong Service company", "Wollongong Appliance repairs", "Winning Appliances"]
company_plaster = ["Paul's Plastering", "John Glen's Plastering", "New Age"]
company_decking = ["Decking Wollongong", "Decking Sydney", "Damien's Carpentry"]
company_painting = ["Optimum painting & decorating", "Mone painting and decorating", "City Coast painting"]
company_roof = ["AUZ roof and gutters", "Coastline roofing and solutions", "Roofers Wollongong"]
company_flooring = ["National Tiles", "Interscope Flooring", "BC Floors"]


def choice():
    male_female = [True, False]
    gender = random.choices(male_female, weights=(97, 3))
    return gender


def generate_name(list1a, list1b, list2):
    if choice():
        first_name = random.choice(list1a)
    else:
        first_name = random.choice(list1b)

    last_name = random.choice(list2)
    full_name = first_name + " " + last_name
    return full_name


def skill_choice(skill_list):
    skills_choice = random.choice(tradie_skills)
    if skills_choice == "Flooring":
        company_choice = random.choice(company_flooring)
    elif skills_choice == "Oven repair":
        company_choice = random.choice(company_oven)
    elif skills_choice == "Plaster and gyprocking":
        company_choice = random.choice(company_plaster)
    elif skills_choice == "Painting":
        company_choice = random.choice(company_painting)
    elif skills_choice == "Fence installation":
        company_choice = random.choice(company_fence)
    elif skills_choice == "Fence repair":
        company_choice = random.choice(company_fence)
    elif skills_choice == "Roof plumbing":
        company_choice = random.choice(company_roof)
    elif skills_choice == "Roof repair":
        company_choice = random.choice(company_roof)
    elif skills_choice == "Decking":
        company_choice = random.choice(company_decking)
    elif skills_choice == "Tree removal":
        company_choice = random.choice(company_trees)
    return skills_choice, company_choice


def create_obj(list1a, list1b, list2, skill):
    skill, company = skill_choice(skill)
    obj = Tradie(generate_name(list1a, list1b, list2), company, skill)
    return obj

list = []

for i in range(0, 20):
    i = create_obj(first_names_male, first_names_female, last_names, tradie_skills)
    list.append(i)

for i in range(0, 20):
    print(list[i].__str__())


