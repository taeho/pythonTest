########################################################################### 1번 문제
# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요
import random

import numpy as np


# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
# - 입력과 출력은 input()과 print()를 사용하세요

def get_near_neighbors(p, points, k):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = np.sqrt(np.sum(np.power(points[i] - p, 2)))
    idx = np.argsort(distances)
    return idx[:k]


def get_knn_predict(p, points, res_lists , k):
    idx = get_near_neighbors(p, points, k)
    return get_majority_vote(res_lists[idx])


def get_majority_vote(votes):
    cnt_votes = {}
    for vote in votes:
        if vote in cnt_votes:
            cnt_votes[vote] += 1
        else:
            cnt_votes[vote] = 1

    list_groups = []
    max_count = max(cnt_votes.values())
    for vote, cnt in cnt_votes.items():
        if cnt == max_count:
            list_groups.append(vote)

    if random.choice(list_groups) == 1:
        print("RED", max_count)
    else:
        print("BLUE", max_count)


# 가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
    # <---메인 코드의 시작--->
    arr = [int(value1) for value1 in input().split()]
    n = arr[0]
    p = np.array([arr[1], arr[2]])
    temp_results = []
    temp_positions = []

    for i in range(0, n):
        lists_xyz = [int(value2) for value2 in input().split()]
        temp_positions.append([lists_xyz[0], lists_xyz[1]])
        temp_results.append(lists_xyz[2])
    outcomes = np.array(temp_results)
    points = np.array(temp_positions)
    key_1 = 3
    key_2 = 5

    get_knn_predict(p, points, outcomes, key_1)
    get_knn_predict(p, points, outcomes, key_2)

# <---메인 코드의 끝--->
