import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)  # Change to True for headless
        context = await browser.new_context()
        page = await context.new_page()

        # ----------------------
        # 1️⃣ Login
        # ----------------------


        await page.goto("https://payvibe-frontend2024.dealopia.com/login")
        await page.get_by_role("textbox", name="Email Address", exact=True).fill("devraj+2@laitkor.com")
        await page.get_by_role("textbox", name="Password").fill("Lcs1423$#")
        await page.locator("form").filter(has_text="LoginLost your password").get_by_role("button").click()
        await asyncio.sleep(5)

        # Wait for Merchants link
        await page.locator("a", has_text="Merchants").wait_for(state="visible", timeout=60000)

        # ----------------------
        # 2️⃣ Navigate to Merchant List
        # ----------------------


        await page.locator("a", has_text="Merchants").click()
        await asyncio.sleep(5)
        await page.get_by_role("link", name="Merchant List").click()
        await asyncio.sleep(5)

        # ----------------------
        # 3️⃣ Edit Merchant
        # ----------------------
        # Wait for rows to load


        await page.locator('role=row >> text=Pizza Hut Merchant').first.wait_for(state="visible", timeout=60000)

        rows = page.locator('role=row >> text=Pizza Hut Merchant')
        count = await rows.count()
        for i in range(count):
            await rows.nth(i).hover()
            await asyncio.sleep(1)  # short delay for dropdown to appear

            # Click the dropdown near the hovered row
            dropdown = rows.nth(i).locator('xpath=..//button[@id="bg-nested-dropdown"]')
            try:
                await dropdown.click()
                await asyncio.sleep(5)
                break
            except:
                continue

        # Click "Edit"
        await page.get_by_role("menuitem", name="Edit").click()
        await asyncio.sleep(5)

        # Fill merchant details
        await page.get_by_role("textbox", name="* Merchant Name").fill("Pizza Hut Merchant 001")
        await page.get_by_role("textbox", name="Meta Keywords").fill("Merchant Keyword Test")
        await page.get_by_role("textbox", name="First Name").fill("Merchant_Test")
        await asyncio.sleep(5)

        # Save
        await page.get_by_role("button", name="Save").click()
        await asyncio.sleep(5)

        # Wait for success message
        await page.get_by_text("success: Merchant detail has").wait_for(state="visible", timeout=60000)
        await asyncio.sleep(5)

        # ---------------------- 
        # 4️⃣ View Updated Merchant
        # ---------------------- 
        await page.get_by_role("link", name="Merchant List").click()
        await asyncio.sleep(5)

        updated_rows = page.locator('role=row >> text=Pizza Hut Merchant 001')
        updated_count = await updated_rows.count()
        for i in range(updated_count):
            await updated_rows.nth(i).hover()
            await asyncio.sleep(1)
            dropdown = updated_rows.nth(i).locator('xpath=..//button[@id="bg-nested-dropdown"]')
            try:

                await dropdown.click()
                await asyncio.sleep(5)
                break

            except:
                continue

        await page.get_by_role("menuitem", name="View", exact=True).click()
        await asyncio.sleep(5)

        # ----------------------
        # 5️⃣ Navigate to Dashboard
        # ----------------------

        
        await page.get_by_role("button", name="Dashboard").click()
        await asyncio.sleep(5)

        # ----------------------
        # Close browser
        # ----------------------
        await context.close()
        await browser.close()

# Run the async function
asyncio.run(run())
