#!/usr/bin/env python
# coding: UTF-8

import argparse
import csv
import random
import sys

import settings


def import_from_csv(csv_file, season):
    try:
        meals_of_season = []
        with open(csv_file) as f:
            f.readline()
            d = dict(csv.reader(f, delimiter=','))
            for key, value in d.items():
                if season == value:
                    meals_of_season.append(key)
        return meals_of_season
    except:
        print('No such file: {}'.format(csv_file))
        sys.exit(-1)


def ask_season_to_user():
    wanted_season = input('Type the wanted season:\t').lower()
    if wanted_season in settings.SPRING:
        wanted_season = 'spring'
    elif wanted_season in settings.SUMMER:
        wanted_season = 'summer'
    elif wanted_season in settings.AUTUMN:
        wanted_season = 'autumn'
    elif wanted_season in settings.WINTER:
        wanted_season = 'winter'
    else:
        print("Your season input is not an available choice.")
    return wanted_season


def random_selection_meals(meals_of_season, wanted_number):
    week_menu = []
    count = len(meals_of_season)
    while len(week_menu) < wanted_number and count:
        meal = random.choice(meals_of_season)
        if meal not in week_menu:
            week_menu.append(meal)
            count -= 1
    return week_menu


def main():
    if not args.season:
        args.season = ask_season_to_user()
    list_meals = import_from_csv(args.file, args.season)
    selected_meals = random_selection_meals(list_meals, args.number)
    if selected_meals:
        print(selected_meals)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str,
                        required=True,
                        help="Load your menu file")
    parser.add_argument('-s', '--season', type=str,
                        choices=["spring", "summer", "autumn", "winter"],
                        help="Choose your current season")
    parser.add_argument('-n', '--number', type=int,
                        default=5,
                        help="Type the number of meals in the generated menu")
    args = parser.parse_args()
    main()
