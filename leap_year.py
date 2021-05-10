#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program verifies if a year is a leap year or not


def main():
    year_string = input("Insert a year: ")
    print()

    try:
        year_inter = int(year_string)

        if year_inter % 4 == 0:
            if year_inter % 100 == 0:
                if year_inter % 400 == 0:
                    print("{} is a leap year!".format(year_inter))
                else:
                    print("{} is NOT a leap year!".format(year_inter))
            else:
                print("{} is a leap year!".format(year_inter))
        else:
            print("{} is NOT a leap year!".format(year_inter))
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
