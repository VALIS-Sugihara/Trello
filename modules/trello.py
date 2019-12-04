# coding:utf-8
from trello import TrelloApi
# import json
# import simplejson as json
import json
import pytz
from datetime import datetime
import os
import requests

USERNAME = "netland1"
KEY = "f9178159f6362c4a51f7c798443031df"
TOKEN = "9c56f81c840c2b4b1bbac6ff69c17b40aa2d210d19fbb8974cf732a66c0f8e16"

class Trello():

    def __init__(self):
        self.trello = TrelloApi(KEY, TOKEN)

    def check_board_id(self, board_name=False):
        """ Check Board Id from board_name

        Keyword arguments:
        board_name: str -- expected board name
        """
        url = "https://trello.com/1/members/%s/boards?key=%s&token=%s" % (USERNAME, KEY, TOKEN,)
        response = requests.get(url)
        data = json.loads(json.dumps(response.json()))
        board_id = False
        for d in data:
            if board_name == d.get("name"):
                board_id = d["id"]
        self.board_id = board_id
        return board_id

    def check_list_id(self, list_name=False):
        url = "https://trello.com/1/boards/%s/lists?key=%s&token=%s&fields=name" % (self.board_id, KEY, TOKEN,)
        response = requests.get(url)
        data = json.loads(json.dumps(response.json()))
        # print(data)
        list_id = False
        for d in data:
            if list_name == d.get("name"):
                list_id = d["id"]
        self.list_id = list_id
        return list_id

    def check_member_id(self):
        url = "https://trello.com/1/boards/%s/members?key=%s&token=%s" % (self.board_id, KEY, TOKEN,)
        response = requests.get(url)
        data = json.loads(json.dumps(response.json()))
        self.members = data
        return data


    def create_cards(self, card_name="", desc=""):
        """
        Create Card to self.board_id
        :param card_name:
        :param desc:
        :return:
        """
        card = self.trello.cards.new(card_name, self.list_id, desc)
        card_json = json.loads(json.dumps(card))
        card_id = card_json["id"]
        card_url = card_json["url"]
        print(card_id)
        print(card_url)
        # Add Labels
        # trello.cards.new_label(card_id, 'green')
        # Set Due　　　カードの期限の設定　UTCで管理されるので日本時間からUTCに変換して設定している
        # utc = pytz.timezone('UTC')
        # jst = pytz.timezone('Asia/Tokyo')
        # jst_dt = datetime(2016, 5, 15, 17, 00, tzinfo=jst)
        # trello.cards.update_due(cardid, jst_dt.astimezone(utc))

        # Add Member　　上記で調べたメンバのID　複数人登録したい場合はnew_memberを人数分記載する
        # trello.cards.new_member(cardid, '551b4f5b19a8a6363ca1940c')  # Maeda



# trello = Trello()
# trello.check_board_id("TEST")
# trello.check_list_id("TODO")
# trello.check_member_id()
# trello.create_cards("test", "test")


"""
# Key Token
trello = TrelloApi('キー', 'トークン')

# List ID　　　上記で調べたボードIDから調べたリストID
listid = '57315d66980bb80dfb51df6e'  # 未着手
# listid = '57315d74e72aacfa5bdaf627' # 作業中
# listid = '57315d78cb6ebdf031c2ce7f' # 完了

# Card Name
cardname = '新しいタスク'

# Card Description
desc = '新しいタスクの内容です。1行目n新しいタスクの内容です。2行目n新しいタスクの内容です。3行目n'

card = trello.cards.new(cardname, listid, desc)
carddump = json.dumps(card, indent=2, ensure_ascii=False)
# print(carddump.encode('utf-8'))
cardjson = json.loads(carddump.encode('utf-8'))
cardid = cardjson['id']
cardurl = cardjson['url']
print cardid
print cardurl

# Add Labels
trello.cards.new_label(cardid, 'green')

# Set Due　　　カードの期限の設定　UTCで管理されるので日本時間からUTCに変換して設定している
utc = pytz.timezone('UTC')
jst = pytz.timezone('Asia/Tokyo')
jst_dt = datetime(2016, 5, 15, 17, 00, tzinfo=jst)
trello.cards.update_due(cardid, jst_dt.astimezone(utc))

# Add Member　　上記で調べたメンバのID　複数人登録したい場合はnew_memberを人数分記載する
trello.cards.new_member(cardid, '551b4f5b19a8a6363ca1940c')  # Maeda

# Add Comment
cardcomment = 'コメントを追加'
trello.cards.new_action_comment(cardid, cardcomment)
"""
