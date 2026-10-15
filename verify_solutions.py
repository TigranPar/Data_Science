"""Լուծումների ստուգում՝ հայտնի պատասխաններով և սահմանային դեպքերով։"""

import math

import numpy as np
import pandas as pd

from sample_tasks import fibonacci_indices, remove_names_ending_a, replace_numbers
from series_arithmetic import solve as arithmetic
from series_attributes import solve as attributes
from series_functions_tasks import above_average, interval_sum, sum_or_mean, top_three


def main():
    values = [5, 10, 15, 20, 25, 30, 33, 40]
    s = pd.Series(values)
    original = s.copy()
    answers = list(arithmetic(s).values())
    mean = sum(values) / len(values)
    expected = [
        [x + 5 for x in values], [x - 10 for x in values],
        [x * 2 for x in values], [x / 5 for x in values],
        [x * x for x in values], [x * x * x for x in values],
        [x + 100 for x in values], [round(x / 2) for x in values],
        [x - values[0] for x in values], [x * values[-1] for x in values],
        [x * 3 + 10 for x in values], [(x - 5) / 5 for x in values],
        sum(values), mean, max(values) - min(values), math.prod(values),
        [2 * x + 1 for x in values],
        [x * 10 if i % 2 == 0 else x for i, x in enumerate(values)],
        [x > 20 for x in values], [x < 15 for x in values],
        [x == 33 for x in values], [x >= 25 for x in values],
        [x <= 10 for x in values], [x % 5 == 0 for x in values],
        [x % 4 == 0 for x in values], [x > 0 for x in values],
        [x for x in values if x > 10],
        [x for x in values if 10 < x < 30],
        [x for x in values if x < 10 or x > 30],
        [x for x in values if x % 10 == 0],
        [x for x in values if x % 2 != 0],
        [x > mean for x in values], True, 4, 5,
        sorted(x for x in values if x > 15),
        [x / sum(values) * 100 for x in values],
    ]
    assert len(answers) == len(expected) == 37
    for i, (actual, wanted) in enumerate(zip(answers, expected), 1):
        if isinstance(actual, pd.Series):
            actual = actual.tolist()
        np.testing.assert_allclose(actual, wanted, err_msg=f"Թվաբանություն, առաջադրանք {i}")
    pd.testing.assert_series_equal(s, original)
    assert list(arithmetic(pd.Series([-1, 1])).values())[-1].isna().all()
    # Ինդեքսների մեջ 40-ի առկայությունը չի նշանակում դրա առկայությունը արժեքների մեջ։
    assert list(arithmetic(pd.Series([1, 2], index=[40, 41])).values())[32] is False
    custom = pd.Series([3, 4, 5], index=[2, 5, 8])
    assert list(arithmetic(custom).values())[17].tolist() == [30, 4, 50]

    s1 = pd.Series([12, 7, 25, 18, 9, 33, 14], index=["anna", "boris", "mariam", "narek", "olga", "aram", "zara"])
    attr = list(attributes(s1).values())
    assert len(attr) == 12
    assert attr[0] == 7 and attr[1] == 8 and attr[2] == np.dtype("int64")
    assert attr[3] == "aram" and attr[4] == 4 and attr[5] is True
    assert attr[6] >= s1.nbytes / 1024 and attr[7] and attr[8] == (7,)
    pd.testing.assert_series_equal(attr[9], s1)
    assert attr[10] == 33 and attr[11] == 18
    repeated = pd.Series([3, 2, 2, 1])
    repeated_answers = list(attributes(repeated).values())
    assert repeated_answers[9] is False
    pd.testing.assert_series_equal(repeated_answers[10], repeated)
    assert repeated_answers[11] == 2
    ascending = pd.Series([1, 2, 3])
    pd.testing.assert_series_equal(list(attributes(ascending).values())[11], ascending)
    singleton = pd.Series([5])
    for actual in list(attributes(singleton).values())[10:]:
        pd.testing.assert_series_equal(actual, singleton)
    labels = pd.Series([1, 4, 4, 2], index=["Anna", "", 7, "zara"])
    label_answers = list(attributes(labels).values())
    assert label_answers[3] == "" and label_answers[4] == 1 and not label_answers[5]

    assert top_three(pd.Series([5, 9, 9, 2])).tolist() == [9, 9, 5]
    assert sum_or_mean(pd.Series([2, 3])) == 5
    assert sum_or_mean(pd.Series([0, 2, 4])) == 2
    assert interval_sum(pd.Series([9, 10, 20, 30, 31]), 10, 30) == 60
    assert interval_sum(pd.Series([1, 2]), 10, 30) == 0
    assert above_average(pd.Series([10, 20, 30])).tolist() == [30]
    assert above_average(pd.Series([5, 5])).empty

    probe = np.array([-8, -1, 0, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 988])
    np.testing.assert_array_equal(fibonacci_indices(probe), [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    assert fibonacci_indices(np.array([], dtype=int)).size == 0
    assert fibonacci_indices(np.array([-3, -1])).size == 0
    mixed = pd.Series([12, "12", "Արամ", -3.5, True], dtype=object)
    assert replace_numbers(mixed).tolist() == ["թիվ", "12", "Արամ", "թիվ", True]
    names = pd.Series(["Աննա", "Արամ", "Մարիա", "Գայանե", "Anna", ""])
    assert remove_names_ending_a(names).tolist() == ["Արամ", "Գայանե", "Anna", ""]
    assert remove_names_ending_a(names).index.tolist() == [1, 3, 4, 5]
    print("Բոլոր 56 առաջադրանքների և լրացուցիչ սահմանային դեպքերի ստուգումներն անցել են հաջողությամբ։")


if __name__ == "__main__":
    main()
