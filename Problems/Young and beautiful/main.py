jack_age = int(input())
alex_age = int(input())
lana_age = int(input())


def young_person(jack_ag, alex_ag, lana_ag):
    return min(jack_ag, alex_ag, lana_ag)


print(young_person(jack_age, alex_age, lana_age))
