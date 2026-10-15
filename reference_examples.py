"""Երեք TXT նյութերի աշխատող օրինակները՝ ուղղված սխալներով։"""

import pandas as pd


def show(title, value):
    print(f"\n{title}\n{value}")


def main():
    arr = pd.Series([1, 7, 8, 11, 8, 2], name="numbers")
    names = pd.Series(["Armen", "Vardan", "Gayane", "Anna"], index=["a", "b", "c", "d"])
    logical = pd.Series([True, True, False])
    show("Սկզբնական թվային Series", arr)

    examples = {
        "head(3): առաջին երեք տարրերը": arr.head(3),
        "tail(3): վերջին երեք տարրերը": arr.tail(3),
        "take([1, 5]): տարրերն ըստ դիրքերի": arr.take([1, 5]),
        "drop_duplicates(): չկրկնվող արժեքները՝ որպես Series": arr.drop_duplicates(),
        "unique(): չկրկնվող արժեքները՝ որպես զանգված": arr.unique(),
        "drop(2): հեռացնել 2 պիտակով տարրը": arr.drop(2),
        "drop([2, 4]): հեռացնել 2 և 4 պիտակներով տարրերը": arr.drop([2, 4]),
        "count(): ոչ բացակայող արժեքների քանակը": arr.count(),
        "count()՝ [1, None, 3] շարքի բացակայող արժեքով": pd.Series([1, None, 3]).count(),
        "cumsum(): կուտակային գումարը": arr.cumsum(),
        "cumprod(): կուտակային արտադրյալը": arr.cumprod(),
        "cummin(): կուտակային նվազագույնը": arr.cummin(),
        "cummax(): կուտակային առավելագույնը": arr.cummax(),
        "nunique(): չկրկնվող արժեքների քանակը": arr.nunique(),
        "duplicated(): կրկնությունները՝ առաջին հանդիպումից հետո": arr.duplicated(),
        "describe(): նկարագրական վիճակագրությունը": arr.describe(),
        "min()": arr.min(),
        "max()": arr.max(),
        "sum()": arr.sum(),
        "mean(): միջին թվաբանականը": arr.mean(),
        "prod(): արտադրյալը": arr.prod(),
        "std(): ընտրանքային ստանդարտ շեղումը (ddof=1)": arr.std(),
        "arr + 2": arr + 2,
        "arr * 3": arr * 3,
        "arr ** 4": arr ** 4,
        "arr / 2": arr / 2,
        "arr // 3": arr // 3,
        "arr - 3": arr - 3,
        "arr % 4": arr % 4,
        "arr > 22": arr > 22,
        "arr < 22": arr < 22,
        "arr >= 22": arr >= 22,
        "arr <= 22": arr <= 22,
        "arr == 22": arr == 22,
        "arr != 22": arr != 22,
        "(arr > 5) & (arr < 20): տրամաբանական ԵՎ": (arr > 5) & (arr < 20),
        "(arr < 5) | (arr > 20): տրամաբանական ԿԱՄ": (arr < 5) | (arr > 20),
        "all(): բոլոր արժեքները ճշմարիտ են": logical.all(),
        "any(): առնվազն մեկ արժեք ճշմարիտ է": logical.any(),
        "sort_values(): տեսակավորումն ըստ արժեքների": arr.sort_values(),
        "sort_index(): տեսակավորումն ըստ պիտակների": pd.Series([3, 1, 2], index=["c", "a", "b"]).sort_index(),
        "dtype: արժեքների տիպը": names.dtype,
        "index: ինդեքսի պիտակները (այստեղ՝ Index, ոչ թե RangeIndex)": names.index,
        "values: արժեքների զանգվածը": names.values,
        "names['b']": names["b"],
        "shape: չափերը": arr.shape,
        "size: տարրերի քանակը": arr.size,
        "ndim: չափումների քանակը": arr.ndim,
        "nbytes: տվյալների ծավալը՝ առանց ինդեքսի": arr.nbytes,
        "is_monotonic_decreasing: չաճող կարգը": arr.is_monotonic_decreasing,
        "is_monotonic_increasing: չնվազող կարգը": arr.is_monotonic_increasing,
        "is_unique: կրկնությունների բացակայությունը": arr.is_unique,
        "name: Series-ի անունը": arr.name,
        "iloc[0]: առաջին տարրը՝ ըստ դիրքի": names.iloc[0],
        "loc['a']: տարրը՝ ըստ պիտակի": names.loc["a"],
        "at['a']: առանձին արժեքը՝ ըստ պիտակի": names.at["a"],
        "empty: դատարկության հատկանիշը՝ առանց փակագծերի": arr.empty,
        "iat[0]: առանձին արժեքը՝ ըստ դիրքի": names.iat[0],
        "T: միաչափ Series-ի տրանսպոնավորումը պահպանում է դրա չափերը": arr.T,
        "array: pandas-ի զանգվածը": names.array,
        "array[0]: զանգվածի առաջին տարրը": names.array[0],
    }
    for title, value in examples.items():
        show(title, value)

    left = pd.Series([2, 4, 6], index=["a", "b", "c"])
    right = pd.Series([1, 2, 3], index=["a", "b", "c"])
    show("Երկու Series․ գործողությունները տարրերը համապատասխանեցնում են ըստ պիտակների", pd.DataFrame({"left": left, "right": right}))
    for title, value in {
        "left + right": left + right,
        "left - right": left - right,
        "left * right": left * right,
        "left / right": left / right,
        "left // right": left // right,
        "left ** right": left ** right,
        "left % right": left % right,
    }.items():
        show(title, value)


if __name__ == "__main__":
    main()
