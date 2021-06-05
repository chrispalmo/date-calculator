import argparse
from date_utils import daysBetween

if __name__ == "__main__":
    parser = argparse.ArgumentParser("calculate the number of full days elapsed in between two dates")
    ARG_HELP = "dd/mm/yyyy (string representing a date)"
    parser.add_argument("dateString1", help=ARG_HELP, type=str)
    parser.add_argument("dateString2", help=ARG_HELP, type=str)
    args = parser.parse_args()
    try:
        print(daysBetween(args.dateString1, args.dateString2))
    except Exception as e:
        print(e)

