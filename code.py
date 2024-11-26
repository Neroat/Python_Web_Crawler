import sys
from PySide6.QtWidgets import QApplication, QWidget
from er_dak import Ui_Form
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class MainWindow(QWidget, Ui_Form):
    

    def __init__(self):
        super().__init__() 
        self.setupUi(self) 
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.quit_btn.clicked.connect(self.quit)
        self.textBrowser.append('해당 프로그램은 셀리니움(Chrome)을 활용하였습니다. \n(헤드리스 옵션이 포함되어있습니다.)')
        self.textBrowser.append('크롤링 대상 사이트 : https://dak.gg/er/players/{nickname}')
        self.textBrowser.append('예시 닉네임 : 인쌤, X보이 \n')
        self.textBrowser.append('최근 플레이한 20개의 매치 정보를 불러옵니다.')
        self.textBrowser.append('캐릭터 스탯, 순위, 딜량, TK/K/A, 아이템')

    def start(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        
        input_nick = self.nickname.text()
        driver.get(f"https://dak.gg/er/players/{input_nick}")
        driver.implicitly_wait(3)
        #response = requests.get(f"https://dak.gg/er/players/{input_nick}")
        #html = response.text
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # find = soup.select_one('div.right')
        # new = find.select_one('section.css-1tvia63')
        divs = soup.select('div.css-1jibmi3')
        #print(f"find 결과 : {divs}")
        for index, div in enumerate(divs):
            # 캐릭터 이름과 레벨 추출
            character_name = div.select_one("div.character-name")
            character_name = character_name.text if character_name else "N/A"
            
            character_level = div.select_one("span.character-level")
            character_level = character_level.text if character_level else "N/A"

            # 랭킹 정보 추출
            rank = div.select_one("div.rank")
            rank = rank.text if rank else "N/A"

            # 딜량 추출
            damage = div.select_one("div.damage .value")
            damage = damage.text if damage else "N/A"

            # play-stat 정보 추출
            play_stat = div.select_one("div.play-stat .stat")
            if play_stat:
                tk, k, a = play_stat.text.split("/") if play_stat.text else ["N/A", "N/A", "N/A"]
            else:
                tk, k, a = "N/A", "N/A", "N/A"  # 만약 play-stat이 없다면 기본값 설정

            # 아이템 목록 추출
            item_elements = div.select("ul.css-1149s7j li")  # 아이템 리스트 가져오기
            item_names = []

            # 각 아이템의 이름 추출 (alt 속성)
            for item in item_elements:
                item_name = item.select_one("img.item")["alt"] if item.select_one("img.item") else "없음"
                item_names.append(item_name)

            # 출력
            self.textBrowser.append("\n")
            self.textBrowser.append(f"{index + 1}번째 실험체: {character_name} \n레벨: {character_level} \n순위: {rank}, 딜량: {damage}")
            self.textBrowser.append(f"플레이 통계 - TK: {tk}, K: {k}, A: {a}")
            self.textBrowser.append(f"무기: {item_names[0]}")
            self.textBrowser.append(f"옷: {item_names[1]}")
            self.textBrowser.append(f"머리: {item_names[2]}")
            self.textBrowser.append(f"팔/장식: {item_names[3]}")
            self.textBrowser.append(f"신발: {item_names[4]}")
            
    def reset(self):
        self.nickname.clear()
        self.textBrowser.clear()

    def quit(self):
        sys.exit()   

app = QApplication() 

window = MainWindow() 
window.show() 

sys.exit(app.exec_())