import random, math, statistics

def randomTeam(data):
    items = random.sample(list(data[0]), 6)
    team = []

    for i in items:
        team.append(i)
    return team

def getAllPokemonData(dataMatrix):
    pkmnData = []
    for i in range(len(dataMatrix[0])):
        pkmnData.append(dataMatrix[0][i])
    return pkmnData


def swap(team, data):
    duplicateCheck = True
    while duplicateCheck:
        swapIn = random.sample(list(data[0]), 1)[0]
        swapOutIdx = random.randint(0, len(team)-1)
        if team[swapOutIdx] != swapIn:
            team[swapOutIdx] = swapIn
            break
    return team

def getTeamScore(team, data, matrix):
    teamScore = 9999
    minScores = []
    for d in data[0]:
        teamScoresList = []
        for a in team:
            teamScoresList.append(matrix[(a,d)])
        teamScoresList.sort(reverse=True)
        minScores.append(statistics.mean([teamScoresList[0], teamScoresList[1]]))
    return min(minScores)

def generateSolution(data, matrix):
    temp_min = 1
    temp = 10^5
    B = 0.99
    time = 15

    # generate initial team to start SA
    team = randomTeam(data)
    solution = team
    bestScore = getTeamScore(team, data, matrix)

    while (temp > temp_min):
        team = swap(solution, data)
        score = getTeamScore(team, data, matrix)
        score_diff = score - bestScore
        x = score_diff / temp
        if random.uniform(0, 1) <= ((math.e) ** x):
            solution = team
            # print(bestScore)
            bestScore = score
        temp = temp * B
    return solution, bestScore

def simAnneal(data, matrix):
    best3 = []

    while (len(best3) < 3):
        solution, score = generateSolution(data, matrix)
        if (solution, score) not in best3:
            best3.append((solution, score))
    # print(best3[0][0])
    for team in best3:
        print("Team: ", team[0])
        print("Utility: ", team[1], '\n')
    return best3
