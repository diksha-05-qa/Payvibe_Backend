from playwright.sync_api import sync_playwright

def test_create_merchant():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ----------------- LOGIN -----------------
        page.goto("https://payvibe-frontend2024.dealopia.com/login")
        page.get_by_role("textbox", name="Email Address", exact=True).fill("devraj+2@laitkor.com")
        page.get_by_role("textbox", name="Password").fill("Lcs1423$#")
        page.locator("form").filter(has_text="LoginLost your password").get_by_role("button").click()
        
        # ----------------- NAVIGATE TO MERCHANTS -----------------
        page.locator("a").filter(has_text="Merchants").click()
        page.get_by_role("link", name="Create New").click()

        # ----------------- MERCHANT DETAILS -----------------
        page.get_by_role("textbox", name="* Merchant Name").fill("Hannah")
        page.get_by_role("textbox", name="Meta Keywords").fill("HannahKeyword")
        page.get_by_role("textbox", name="* Legal Name").fill("Leagle test")
        page.get_by_role("textbox", name="Meta Description").fill("Meta desc Test")
        page.get_by_role("textbox", name="Enter Website URL").fill("https://www.google.com/")
        page.get_by_role("textbox", name="Facebook Page").fill("https://www.facebook.com/")
        page.get_by_role("textbox", name="Twitter Page").fill("https://x.com/")
        page.get_by_role("checkbox", name="List in Merchant Directory").check()

        # ----------------- USER DETAILS -----------------
        page.get_by_role("textbox", name="User Name").fill("Nick ")
        page.get_by_role("textbox", name="User Name").press("Tab")
        page.get_by_role("textbox", name="First Name").fill("Nick")
        page.get_by_role("textbox", name="Last Name").fill("George")
        page.get_by_role("textbox", name="Enter email").fill("Nick@gmail.com")

        # ----------------- DATE OF BIRTH -----------------
        page.locator("div").filter(has_text="Date Of Birth//").first.click()
        page.get_by_role("button").nth(3).click()
        page.get_by_role("button", name="1 January 2026", exact=True).click()

        # ----------------- PHONE -----------------
        page.get_by_role("textbox", name="Enter Phone Number").fill("983-990-3374_")

        # ----------------- ADDRESS -----------------
        page.locator('select[name="Country"]').select_option("CA")
        page.locator('select[name="state"]').select_option("MB")
        page.get_by_role("textbox", name="Address 2").fill("xccv")
        page.get_by_role("textbox", name="Address 1").fill("gfgfg")
        page.get_by_role("textbox", name="*City").fill("fdg")
        page.get_by_role("textbox", name="Zip Code").fill("20112")

        # ----------------- DROPDOWN SELECTION -----------------
        page.get_by_label("* City:").select_option("59bc4089ed8ca3a10cbad142167ea7b8")
        page.get_by_label("Sales Person").select_option("f6db082365eb9ccb1f1f1a0315811523")

        # ----------------- SAVE MERCHANT -----------------
        page.get_by_role("button", name="Save").click()

        # ----------------- MERCHANT LIST & VIEW -----------------
        page.get_by_role("link", name="Merchant List").click()

        # Use .first to avoid strict mode violation
        page.get_by_role("row", name="Hannah Nick@gmail.com Nick").locator("#bg-nested-dropdown").first.click()
        page.get_by_role("menuitem", name="View", exact=True).click()

        # Go to Dashboard
        page.get_by_role("button", name="Dashboard").click()

        # Close browser
        browser.close()


# ----------------- RUN TEST -----------------
if __name__ == "__main__":
    test_create_merchant()

