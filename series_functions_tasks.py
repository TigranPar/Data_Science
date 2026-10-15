"""Series_functions (1).txt ֆայլի վերջում տրված 4 առաջադրանք։"""

import pandas as pd


def top_three(s: pd.Series) -> pd.Series:
    # Կրկնվող արժեքները պահպանվում են․ պահանջվում է երեք տարր, ոչ թե երեք տարբեր թիվ։
    return s.sort_values(ascending=False).head(3)


def sum_or_mean(s: pd.Series):
    return s.sum() if s.all() else s.mean()


def interval_sum(s: pd.Series, a: float, b: float):
    if a > b:
        raise ValueError("Ձախ սահմանը չպետք է գերազանցի աջ սահմանը։")
    return s[(s >= a) & (s <= b)].sum()


def above_average(grades: pd.Series) -> pd.Series:
    return grades[grades > grades.mean()]


def main():
    s = pd.Series([12, 7, 25, 18, 9, 33, 14])
    print(f"ՍԿԶԲՆԱԿԱՆ SERIES\n{s}")
    print(f"\n1. Երեք ամենամեծ տարրերը\n{top_three(s)}")
    print(f"\n2. Գումարը, եթե բոլոր տարրերը ճշմարիտ են, հակառակ դեպքում՝ միջինը\n{sum_or_mean(s)}")
    with_zero = pd.Series([0, 7, 25])
    print(f"Երկրորդ ճյուղի ստուգման համար՝ {with_zero.tolist()} → {sum_or_mean(with_zero)}")
    a, b = 10, 25
    print(f"\n3. Տարրերի գումարը [{a}, {b}]\n{interval_sum(s, a, b)}")
    grades = pd.Series([15.5, 18.0, 12.5, 19.0, 16.0], index=["Armen", "Anna", "Vardan", "Gayane", "Narek"], name="average_grade")
    print(f"\n4. Ուսանողների միջին գնահատականները\n{grades}")
    print(f"Խմբի միջին գնահատականը՝ {grades.mean():.2f}")
    print(f"Խմբի միջինից բարձր գնահատականները\n{above_average(grades)}")


if __name__ == "__main__":
    main()
