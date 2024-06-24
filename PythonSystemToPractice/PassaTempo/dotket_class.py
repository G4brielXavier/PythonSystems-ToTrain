from colorama import Fore, Back

def points(n1=0, n2=0, n3=0, n4=0, sit=True):
    """Function to calc points of a class

    Args:
        n1 (float): reference of point 1
        n2 (float): reference of point 2
        n3 (float): reference of point 3
        n4 (float): reference of point 4
        sit (boolean): optional variable to show the situation of student.
    """
    
    points_in_base = [n1, n2, n3, n4]
    points_accepted = []
    all = {}
    
    for i in points_in_base:
        if i > 0:
            points_accepted.append(i)
    
    all['Total'] = len(points_accepted)
    all['Bigger'] = max(points_accepted)
    all['Smaller'] = min(points_accepted)
    all['Average'] = sum(points_accepted) / len(points_accepted)
    
    if sit:
        if all['Average'] >= 7:
            all['Situation'] = 'Approved'
        elif all['Average'] < 7:
            all['Situation'] = 'Disapproved'
    
    return all

res = points(5.5, 7.8, 8.8, 8.8, False)
print(Fore.GREEN + f'{res}')
    