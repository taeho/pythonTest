########################################################################### 1번 문제
# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요
import numpy as np
import random


# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
# - 입력과 출력은 input()과 print()를 사용하세요

def distance(a, b):
    return np.sqrt(np.sum(np.power(b - a, 2)))


def find_nearest_neighbors(p, points, k):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)

    if random.choice(winners) == 1:
        print("RED", max_count)
    else:
        print("BLUE", max_count)


# 가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
    # <---메인 코드의 시작--->
    arr = [int(value1) for value1 in input().split()]
    n = arr[0]
    p = np.array([arr[1], arr[2]])
    tmp_outcomes = []
    tmp_points = []

    for i in range(0, n):
        xyz = [int(value2) for value2 in input().split()]
        tmp_points.append([xyz[0], xyz[1]])
        tmp_outcomes.append(xyz[2])
    outcomes = np.array(tmp_outcomes)
    points = np.array(tmp_points)
    k_1 = 3
    k_2 = 5

    knn_predict(p, points, outcomes, k_1)
    knn_predict(p, points, outcomes, k_2)

# <---메인 코드의 끝--->