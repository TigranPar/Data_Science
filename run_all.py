"""Բոլոր լուծումներն ու տեղեկատու օրինակները գործարկել մեկ հրամանով։"""

import reference_examples
import sample_tasks
import series_arithmetic
import series_attributes
import series_functions_tasks


def main():
    modules = [series_arithmetic, series_attributes, series_functions_tasks, sample_tasks, reference_examples]
    for module in modules:
        print("\n" + "=" * 72)
        print(module.__doc__)
        print("=" * 72)
        module.main()


if __name__ == "__main__":
    main()
