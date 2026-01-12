import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_create_merchant():
    async with async_playwright() as p:

        # ---------------- BROWSER ----------------
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=300
        )
        page = await browser.new_page()
        page.set_default_timeout(60000)

        # ---------------- LOGIN ----------------
        await page.goto("https://payvibe-frontend2024.dealopia.com/login")

        login_form = page.locator("form")

        # Email (FIXED strict mode)
        await login_form.locator("input[name='email']").fill(
            "devraj+2@laitkor.com"
        )

        # Password
        await login_form.locator("input[type='password']").fill(
            "Lcs1423$#"
        )

        # Login button (FIXED strict mode)
        await login_form.locator("button[type='submit']").click()

        # ---------------- WAIT FOR DASHBOARD ----------------
        await page.wait_for_url("**/dashboard**")
        await page.screenshot(path="after_login.png", full_page=True)

        # ---------------- SIDEBAR (IF COLLAPSED) ----------------
        toggle = page.locator("button[aria-label*='Toggle']")
        if await toggle.count() > 0 and await toggle.is_visible():
            await toggle.click()

        # ---------------- NAVIGATE TO MERCHANTS ----------------
        await page.locator("a:has-text('Merchants')").first.click()
        await page.locator("a:has-text('Create New')").click()

        # ---------------- MERCHANT DETAILS ----------------
        await page.get_by_label("* Merchant Name").fill("Hannah")
        await page.get_by_label("Meta Keywords").fill("HannahKeyword")
        await page.get_by_label("* Legal Name").fill("Legal Test")
        await page.get_by_label("Meta Description").fill("Meta desc Test")

        await page.get_by_label("Enter Website URL").fill(
            "https://www.google.com/"
        )
        await page.get_by_label("Facebook Page").fill(
            "https://www.facebook.com/"
        )
        await page.get_by_label("Twitter Page").fill(
            "https://x.com/"
        )

        await page.get_by_role(
            "checkbox",
            name="List in Merchant Directory"
        ).check()

        # ---------------- USER DETAILS ----------------
        await page.get_by_label("User Name").fill("Nick")
        await page.get_by_label("First Name").fill("Nick")
        await page.get_by_label("Last Name").fill("George")

        # second email field (user email)
        await page.locator("input[name='email']").nth(1).fill(
            "nick@gmail.com"
        )

        # ---------------- DOB ----------------
        await page.get_by_text("Date Of Birth").click()
        await page.get_by_role("button", name="1 January 2026").click()

        # ---------------- PHONE ----------------
        await page.get_by_label("Enter Phone Number").fill("9839903374")

        # ---------------- ADDRESS ----------------
        await page.locator("select[name='Country']").select_option("CA")
        await page.locator("select[name='state']").select_option("MB")

        await page.get_by_label("Address 1").fill("gfgfg")
        await page.get_by_label("Address 2").fill("xccv")
        await page.get_by_label("*City").fill("fdg")
        await page.get_by_label("Zip Code").fill("20112")

        # ---------------- DROPDOWNS ----------------
        await page.get_by_label("* City:").select_option(
            "59bc4089ed8ca3a10cbad142167ea7b8"
        )
        await page.get_by_label("Sales Person").select_option(
            "f6db082365eb9ccb1f1f1a0315811523"
        )

        # ---------------- SAVE ----------------
        await page.get_by_role("button", name="Save").click()

        await page.wait_for_timeout(5000)
        await page.screenshot(path="merchant_created.png", full_page=True)

        await browser.close()
