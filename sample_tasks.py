"""3 առաջադրանք՝ nmush (2).docx ֆայլից։"""

from numbers import Number

import numpy as np
import pandas as pd


def fibonacci_indices(values: np.ndarray) -> np.ndarray:
    if values.size == 0:
        return np.array([], dtype=int)
    limit = int(values.max())
    fibonacci = set()
    a, b = 0, 1
    while a <= limit:
        fibonacci.add(a)
        a, b = b, a + b
    return np.flatnonzero(np.isin(values, list(fibonacci)))


def replace_numbers(values: pd.Series, word: str = "թիվ") -> pd.Series:
    # bool-ը բացառվում է․ Python-ում այն int-ի ենթադաս է, սակայն այստեղ տրամաբանական արժեք է։
    return values.map(lambda value: word if isinstance(value, Number) and not isinstance(value, (bool, np.bool_)) else value)


def remove_names_ending_a(names: pd.Series) -> pd.Series:
    # Պայմանում տրված է հայերեն «ա» տառը, ոչ թե լատիներեն a-ն։
    return names[~names.str.endswith("ա", na=False)]


def main():
    rng = np.random.default_rng(42)
    values = rng.integers(0, 1000, size=100)
    indices = fibonacci_indices(values)
    print(f"1. [0, 999] միջակայքի 100 պատահական ամբողջ թվերից կազմված զանգված\n{values}")
    print(f"Ֆիբոնաչիի թվերի ինդեքսները (համարակալումը՝ 0-ից)\n{indices}")
    print(f"Համապատասխան արժեքները\n{values[indices]}")

    mixed = pd.Series([12, "Արամ", 3.5, "Աննա", -7, "Գայանե", 0], dtype=object)
    print(f"\n2. Թվերը փոխարինել «թիվ» բառով\nՄինչև՝\n{mixed}\nՀետո՝\n{replace_numbers(mixed)}")

    names = pd.Series(["Աննա", "Արամ", "Մարիա", "Գայանե", "Սոնա", "Նարեկ"], name="names")
    print(f"\n3. Հեռացնել «ա» տառով ավարտվող անունները\nՄինչև՝\n{names}\nՀետո՝\n{remove_names_ending_a(names)}")


if __name__ == "__main__":
    main()
