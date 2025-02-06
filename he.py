import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# 봇 탐지 방지 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

# ChromeDriver 경로 설정
driver_path = r"C:\Users\sims\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 수강신청 사이트 열기
driver.get("https://for-s.seoultech.ac.kr/view/login.jsp")

try:
    # 사용자 로그인 후 CAPTCHA 입력 대기
    input("🔴 [CAPTCHA 입력 후 로그인]한 다음, [수강신청 페이지]에 도달하면 Enter 키를 누르세요. 🔴")

    while True:
        # 현재 시간을 확인
        now = datetime.now()

        # 초와 밀리초가 모두 0일 때 대기 (정확히 매 분 정각 이후)
        if now.second == 0 and now.microsecond == 0:
            time.sleep(0.1)  # 0.1초 대기 후 작업 실행
            try:
                # 1️⃣ 첫 번째 버튼 (id=cb_grd_basket) 클릭
                first_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "cb_grd_basket"))
                )
                first_button.click()
                print("✅ 첫 번째 버튼 클릭 완료!")

                # 2️⃣ 두 번째 버튼 (id=btn_basketSave) 클릭
                second_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "btn_basketSave"))
                )
                second_button.click()
                print("✅ 두 번째 버튼 클릭 완료!")

                # 3️⃣ 팝업 창에서 엔터 키 입력
                alert = WebDriverWait(driver, 5).until(EC.alert_is_present())  # 팝업이 뜰 때까지 기다림
                alert.accept()  # 확인(엔터) 누르기
                print("✅ 팝업 창에서 엔터 입력 완료!")

            except Exception as e:
                print(f"🚨 버튼 클릭 오류 발생: {e}")

            # 다음 실행을 위해 잠시 대기
            print("⏳ 다음 작업을 기다리는 중...")
            time.sleep(1)  # 같은 정각 반복 방지

except Exception as e:
    print(f"🚨 오류 발생: {e}")

finally:
    driver.quit()  # 브라우저 종료
