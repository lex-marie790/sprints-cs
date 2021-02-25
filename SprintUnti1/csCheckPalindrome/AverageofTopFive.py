"""
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
"""

def csAverageOfTopFive(scores):
    scores1 = {}
    
    for score in scores:
        if score[0] in scores1:
            scores1[score[0]].append(score[1])
        else:
            scores1[score[0]] = [score[1]]
            
    res = []
    for key, value in scores1.items():
        value.sort(reverse=True)
        if len(value) >= 5:
            topFive = value[:5]
        else:
            topFive = value
        scores1[key] = sum(topFive) // len(topFive)
        res.append([key,scores1[key] ])
    
    return res
        
