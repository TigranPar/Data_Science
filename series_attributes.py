"""12 առաջադրանք՝ series tasks (1).docx ֆայլից․ Series-ի հատկանիշները։"""

import numpy as np
import pandas as pd


def solve(s1: pd.Series) -> dict:
    if s1.empty:
        raise ValueError("Առավելագույն արժեքը և միջին դիրքի տարրը գտնելու համար անհրաժեշտ է ոչ դատարկ Series։")

    # 4-րդ առաջադրանքի պայմանով Series-ի մեթոդներ չեն օգտագործվում։
    # Մի քանի առավելագույն արժեքների դեպքում ընտրվում է առաջին համապատասխան պիտակը։
    maximum_label = s1.index[np.argmax(s1.values)]
    labels_first_half = sum(
        isinstance(label, str) and bool(label) and "a" <= label[0].lower() <= "m"
        for label in s1.index
    )
    if s1.is_monotonic_decreasing:
        decreasing_result = s1.copy()
    else:
        decreasing_result = s1.iloc[-2]

    if s1.is_monotonic_increasing:
        increasing_result = s1.copy()
    else:
        # Տարրերի զույգ քանակի դեպքում ընտրվում է երկու կենտրոնական տարրերից աջը։
        increasing_result = s1.iloc[s1.size // 2]

    return {
        "01. Տարրերի քանակը՝ առանց len()-ի": s1.size,
        "02. Մեկ տարրի տվյալների միջին ծավալը՝ բայթերով": s1.nbytes / s1.size,
        "03. s1.values զանգվածի տվյալների տիպը": s1.values.dtype,
        "04. Առավելագույն արժեքի ինդեքսի պիտակը՝ առանց Series-ի մեթոդների": maximum_label,
        "05. a–m տառերով սկսվող պիտակների քանակը": labels_first_half,
        "06. Արդյոք ինդեքսի բոլոր պիտակները տողեր են": all(isinstance(label, str) for label in s1.index),
        "07. Series-ի հիշողությունը՝ ինդեքսի հետ միասին, ԿԲ (1024 բայթ)": s1.memory_usage(index=True, deep=True) / 1024,
        "08. Արդյոք Series-ը միաչափ է": s1.ndim == 1,
        "09. Series-ի չափերը": s1.shape,
        "10. Series-ը, եթե կրկնություններ չկան, հակառակ դեպքում՝ False": s1.copy() if s1.is_unique else False,
        "11. Series-ը, եթե դասավորված է նվազման կարգով, հակառակ դեպքում՝ նախավերջին տարրը": decreasing_result,
        "12. Series-ը, եթե դասավորված է աճման կարգով, հակառակ դեպքում՝ միջին դիրքի տարրը": increasing_result,
    }


def main():
    s1 = pd.Series([12, 7, 25, 18, 9, 33, 14], index=["anna", "boris", "mariam", "narek", "olga", "aram", "zara"], name="values")
    print("ՍԿԶԲՆԱԿԱՆ SERIES\n", s1, sep="")
    for task, result in solve(s1).items():
        print(f"\n{task}\n{result}")


if __name__ == "__main__":
    main()
