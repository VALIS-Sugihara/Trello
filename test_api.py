import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules.trello import *
import codecs

path = "data/test_kintone.csv"


def trello_execute():
    trello = Trello()
    trello.check_board_id("TEST")
    trello.check_list_id("チーム全体")
    trello.check_member_id()

    with codecs.open(path, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_csv(file)
        print(df.head())
        length = len(df) - 1  # for header
        for i in range(length):
            id = df.loc[i]["案件ID"]
            company_name = df.loc[i]["企業名"]
            # print(id, company_name)
            trello.create_cards(card_name=id, desc=company_name)


# trello_execute()