from playwright.sync_api import sync_playwright
import time

def login_interpark(username, password):
    with sync_playwright() as p:
        # 브라우저 시작 (headless 모드 해제 및 User-Agent 변경)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        page = context.new_page()

        # 페이지 이동
        page.goto('https://ticket.interpark.com/')
        
        # 로그인 버튼 클릭
        page.click('text="로그인"')
        
        # 추가 대기 시간
        time.sleep(2)
        
        # 아이디와 비밀번호 입력 필드가 나타날 때까지 대기
        page.wait_for_selector('[placeholder="아이디"]')
        
        # 로그인 정보 입력
        page.get_by_placeholder("아이디").fill(username)
        page.get_by_placeholder("비밀번호").fill(password)
        
        # CAPTCHA 처리
        if page.query_selector('#captcha_element'):
            print("CAPTCHA detected! Please solve it manually.")
            input("Press Enter to continue after solving CAPTCHA...")

        # 로그인 버튼 스크롤 및 클릭
        login_button = page.query_selector('button[type="button"]')

        if login_button:
            # 로그인 버튼이 있는 위치로 스크롤
            login_button.scroll_into_view_if_needed()

            # 로그인 버튼 클릭
            login_button.click()
        else:
            print("Login button not found")

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('networkidle')
        
        # 추가 대기 시간
        time.sleep(5)

        # 브라우저 종료
        browser.close()

# 로그인 정보 설정
username = "Dltmdduq"
password = "tmd@3046"

# 로그인 함수 호출
login_interpark(username, password)

print("kimchi")

print("lalala")