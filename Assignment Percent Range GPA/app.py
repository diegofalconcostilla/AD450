def percentRangeGpa(grade):
    floatGrade = float(grade)
    if floatGrade > 100 or floatGrade < 0:
        return "Error, invalid value, please enter a number between 100 and 0"
    elif floatGrade >= 95:
        return 4.0
    elif floatGrade >= 94 < 95:
        return 3.9
    elif floatGrade >= 93 < 94:
        return 3.8
    elif floatGrade >= 92 < 93:
        return 3.7
    elif floatGrade >= 91 < 92:
        return 3.6
    elif floatGrade >= 90 < 91:
        return 3.5
    elif floatGrade >= 89 < 90:
        return 3.4
    elif floatGrade >= 88 < 89:
        return 3.3
    elif floatGrade >= 87 < 88:
        return 3.2
    elif floatGrade >= 86 < 87:
        return 3.1
    elif floatGrade >= 85 < 86:
        return 3.0
    elif floatGrade >= 84 < 85:
        return 2.9
    elif floatGrade >= 83 < 84:
        return 2.8
    elif floatGrade >= 82 < 83:
        return 2.7
    elif floatGrade >= 81 < 82:
        return 2.6
    elif floatGrade >= 80 < 81:
        return 2.5
    elif floatGrade >= 79 < 80:
        return 2.4
    elif floatGrade >= 78 < 79:
        return 2.3
    elif floatGrade >= 77 < 78:
        return 2.2
    elif floatGrade >= 76 < 77:
        return 2.1
    elif floatGrade >= 75 < 76:
        return 2.0
    elif floatGrade >= 74 < 75:
        return 1.9
    elif floatGrade >= 73 < 74:
        return 1.8
    elif floatGrade >= 72 < 73:
        return 1.7
    elif floatGrade >= 71 < 72:
        return 1.6
    elif floatGrade >= 70 < 71:
        return 1.5
    elif floatGrade >= 69 < 70:
        return 1.4
    elif floatGrade >= 68 < 69:
        return 1.3
    elif floatGrade >= 67 < 68:
        return 1.2
    elif floatGrade >= 66 < 67:
        return 1.1
    elif floatGrade >= 65 < 66:
        return 1.0
    elif floatGrade >= 0.0 < 65:
        return 0.0

print(percentRangeGpa(input("Please write the grade that you would like to convert to GPA ")));


    
