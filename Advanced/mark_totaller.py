a = [
    {
        "Firstname": "Arul",
        "Lastname": "Kumar",
        "Mark": 80,
        "Subject": "Maths"
    },
    {
        "Firstname": "Arul",
        "Lastname": "Kumar",
        "Mark": 85,
        "Subject": "Physics"
    },
    {
        "Firstname": "sathish",
        "Lastname": "Narayanan",
        "Mark": 60,
        "Subject": "science"
    },
    {
        "Firstname": "Pradeep",
        "Lastname": "Kumar",
        "Mark": 70,
        "Subject": "Maths"
    },
    {
        "Firstname": "sathish",
        "Lastname": "Narayanan",
        "Mark": 90,
        "Subject": "Tamil"
    },
]


def get_cons(x):
    group_dict = {}
    for xy in x:
        if (xy['Firstname'], xy['Lastname']) in group_dict:
            if group_dict.get((xy['Firstname'], xy['Lastname']))['Marks'] < xy['Mark']:
                group_dict[(xy['Firstname'], xy['Lastname'])]['Subject'] = xy['Subject']
            group_dict[(xy['Firstname'], xy['Lastname'])]['Marks'] += xy['Mark']  
        else:
            group_dict[(xy['Firstname'], xy['Lastname'])] = {'Marks': xy['Mark'], 'Subject': xy['Subject']}
    return [{"Firstname":k[0], "Lastname":k[1], **v} for k,v in group_dict.items()]
    
    
x = get_cons(a)
print(x)