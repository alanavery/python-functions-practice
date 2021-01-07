# Problem 1 ——————————————————————————————
def tripler(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i] * 3)
    return new_lst


print(tripler([3, 6, 9]))

# Problem 2 ——————————————————————————————


def odd_range(end):
    new_lst = []
    for i in range(end):
        i += 1
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst


print(odd_range(13))

# Problem 3 ——————————————————————————————


def is_prime(num):
    for i in range(num):
        i += 1
        if i != 1 and i != num and num % i == 0:
            return False
    return True


print(is_prime(2017))

# Problem 4 ——————————————————————————————


def cat_builder(name, color, toys):
    cat = {
        "name": name,
        "color": color,
        "toys": toys
    }
    return cat


print(cat_builder('Poopsie', 'white', ['dead mice', 'dead birds']))

# Problem 5 ——————————————————————————————


def value_pair(obj1, obj2, key):
    new_lst = []
    new_lst.append(obj1[key])
    new_lst.append(obj2[key])
    return new_lst


object1 = {"name": 'One', "location": 'Remote', "age": 1}
object2 = {"name": 'Two', "location": 'San Francisco'}

print(value_pair(object1, object2, 'name'))

# Problem 6 ——————————————————————————————


def does_key_exist(obj, guess):
    for key in obj:
        if key == guess:
            return True
    return False


obj1 = {"company": 'General Assembly',
        "course": 'Software Engineering Immersive'}

print(does_key_exist(obj1, 'name'))

# Problem 7 ——————————————————————————————


def adults(people):
    new_lst = []
    for i in range(len(people)):
        if people[i]['age'] >= 18:
            new_lst.append(people[i])
    return new_lst


ppl = [
    {"name": 'Khalid Robinson', "age": 22},
    {"name": 'Ariel Winter', "age": 20},
    {"name": 'Post Malone', "age": 25},
    {"name": 'Willow Smith', "age": 17}
]

print(adults(ppl))

# Problem 8 ——————————————————————————————


def count_scores(people):
    new_dic = {}
    for i in range(len(people)):
        if people[i]['name'] in new_dic:
            new_dic[people[i]['name']] += people[i]['score']
        else:
            new_dic[people[i]['name']] = people[i]['score']
    return new_dic


peeps = [
    {"name": 'Pete', "score": 2},
    {"name": 'Dexter', "score": 2},
    {"name": 'Mike', "score": 2},
    {"name": 'Dexter', "score": 2},
    {"name": 'Mike', "score": 2},
    {"name": 'Pete', "score": 2},
    {"name": 'Dexter', "score": 2}
]

print(count_scores(peeps))
