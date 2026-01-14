import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    # ================= LOGIN =================
    await page.goto("https://payvibe-frontend2024.dealopia.com/login")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Email Address", exact=True).fill("devraj+2@laitkor.com")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Email Address", exact=True).press("Tab")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Password").fill("Lcs1423$#")
    await asyncio.sleep(4)

    await page.locator("form").filter(has_text="LoginLost your password").get_by_role("button").click()
    await asyncio.sleep(4)

    # ================= NAVIGATION =================
    await page.locator("a").filter(has_text="Offers").click()
    await asyncio.sleep(4)

    await page.get_by_role("link", name="Create New").click()
    await asyncio.sleep(4)

    # ================= MERCHANT DETAILS =================
    await page.locator("#formMerchantID").select_option("5302422a7a419138384d8c38455b4c92")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Contact Name").fill("contact")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Contact Phone").fill("989-336-36548")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Contact Email").fill("x1@gmail.com")
    await asyncio.sleep(4)

    await page.get_by_label("Contract/Proposal Type").select_option("5")
    await asyncio.sleep(4)

    # ================= OFFER DETAILS =================
    await page.get_by_role("textbox", name="* Title").fill("wedenesfay offer 2026")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Overall Quantity").fill("20")
    await asyncio.sleep(4)

    await page.locator("#formTermsAndConditions").fill("Terms and condition test")
    await asyncio.sleep(4)

    await page.locator("#formfrench_termsAndConditions").fill("Terms and condition Test")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="* Offer Title", exact=True).fill("Wednesday offer 2026")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="* Offer Title (Canadian").fill("Wednesday offer 2026")
    await asyncio.sleep(4)

    # ================= PRICING & QUANTITY =================
    await page.get_by_placeholder("Maximum Available").fill("20")
    await asyncio.sleep(4)

    await page.get_by_placeholder("Retail Price").fill("10")
    await asyncio.sleep(4)

    await page.get_by_label("* How Long Until Purchased").select_option("0")
    await asyncio.sleep(4)

    await page.get_by_placeholder("Offer Price").fill("6")
    await asyncio.sleep(4)

    await page.get_by_placeholder("Remittance Per Unit").fill("5")
    await asyncio.sleep(4)

    await page.get_by_role("textbox", name="Minimum Quantity Required To").fill("1")
    await asyncio.sleep(4)

    await page.get_by_placeholder("Max As Gifts").fill("10")
    await asyncio.sleep(4)

    await page.get_by_placeholder("Max Per Customer").fill("2")
    await asyncio.sleep(4)

    # ================= NOTES & PAYMENT =================
    await page.get_by_role("textbox", name="Additonal Notes").fill("Additional Note Test")
    await asyncio.sleep(4)

    await page.get_by_label("Payment terms").select_option("6f81eca9f589c39036be86eb16d66713")
    await asyncio.sleep(4)

    await page.get_by_label("Sales Person").select_option("771c4c087d92627d1835abdb02973925")
    await asyncio.sleep(4)

    # ================= SAVE =================
    await page.locator("#schedule").wait_for(state="visible")
    await page.locator("#schedule").click()
    await asyncio.sleep(4)

    # ================= CLOSE =================
    await context.close()
    await browser.close()


async def main():

    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
