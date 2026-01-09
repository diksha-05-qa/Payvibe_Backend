from playwright.sync_api import sync_playwright

def wait(page):
    page.wait_for_timeout(3000)   #  5 seconds wait

def test_merchant_flow():

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        # ================= LOGIN =================
        page.goto("https://payvibe-frontend2024.dealopia.com/login")
        wait(page)

        page.get_by_role("textbox", name="Email Address", exact=True).fill(
            "devraj+2@laitkor.com"
        )
        wait(page)

        page.get_by_role("textbox", name="Password").fill("Lcs1423$#")
        wait(page)

        page.locator("form").filter(
            has_text="LoginLost your password"
        ).get_by_role("button").click()
        wait(page)

        # ================= MERCHANT CREATE =================
        page.locator("a", has_text="Merchants").click()
        wait(page)

        page.get_by_role("link", name="Create New").click()
        wait(page)

        page.get_by_role("textbox", name="* Merchant Name").fill("Nick George")
        wait(page)

        page.get_by_role("textbox", name="Meta Keywords").fill("Nick Keyword Tes")
        wait(page)

        page.get_by_role("textbox", name="* Legal Name").fill("Leagle nick Tes")
        wait(page)

        page.get_by_role("textbox", name="Meta Description").fill("Nick Desc")
        wait(page)

        page.get_by_role("textbox", name="Enter Website URL").fill("https://www.google.com/")
        wait(page)

        page.get_by_role("textbox", name="Facebook Page").fill("https://www.facebook.com/")
        wait(page)

        page.get_by_role("textbox", name="Twitter Page").fill("https://x.com/")
        wait(page)

        page.get_by_role("checkbox", name="List in Merchant Directory").check()
        wait(page)

        page.get_by_role("textbox", name="User Name").fill("Nicke_George")
        wait(page)

        page.get_by_role("textbox", name="Enter email").fill("Nick1@gmsil.com")
        wait(page)

        # ================= DATE PICKER =================
        page.get_by_role("button").nth(3).click()
        wait(page)

        page.get_by_role("button", name="1 January 2026", exact=True).click()
        wait(page)

        # ================= PERSONAL INFO =================
        page.get_by_role("textbox", name="First Name").fill("Nicke")
        wait(page)

        page.get_by_role("textbox", name="Last Name").fill("George")
        wait(page)

        page.get_by_role("textbox", name="Enter Phone Number").fill("983-990-3374_")
        wait(page)

        # ================= ADDRESS =================
        page.get_by_role("textbox", name="Address 1").fill("Knoxville")
        wait(page)

        page.get_by_role("textbox", name="Address 2").fill("Knioxcolee")
        wait(page)

        page.get_by_role("textbox", name="*City").fill("us")
        wait(page)

        page.get_by_role("textbox", name="Zip Code").fill("101102")
        wait(page)

        page.locator('select[name="Country"]').select_option("CA")
        wait(page)

        page.locator('select[name="state"]').select_option("AB")
        wait(page)

        page.get_by_label("* City:").select_option(
            "59bc4089ed8ca3a10cbad142167ea7b8"
        )
        wait(page)

        page.get_by_label("Sales Person").select_option(
            "f6db082365eb9ccb1f1f1a0315811523"
        )
        wait(page)

        # ================= SAVE =================
        page.get_by_role("button", name="Save").click()
        wait(page)

        page.get_by_text("success: Merchant account has").wait_for()
        wait(page)

        # ================= MERCHANT LIST =================
        page.get_by_role("link", name="Merchant List").click()
        wait(page)

        merchant_row = page.get_by_role(
            "row", name="Nick George Nick1@gmsil.com"
        )

        merchant_row.locator("#bg-nested-dropdown").first.click()
        wait(page)

        page.get_by_role("menuitem", name="Edit").click()
        wait(page)

        page.get_by_role("link", name="Merchant List").click()
        wait(page)

        merchant_row.locator("#bg-nested-dropdown").first.click()
        wait(page)

        page.get_by_role("menuitem", name="View", exact=True).click()
        wait(page)

        page.get_by_role("button", name="Dashboard").click()
        wait(page)

        context.close()
        browser.close()
