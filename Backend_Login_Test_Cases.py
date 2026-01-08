from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://payvibe-frontend2024.dealopia.com/login"

# Global list to store results
test_results = []

def run_login_test(name, email, password, expected_error=None):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Hit URL
        page.goto(LOGIN_URL)

        # Fill credentials
        page.fill('input[placeholder="Email Address"]', email)
        page.fill('#inputPassword', password)

        # Click Login
        page.click('button[data-id="Login"][type="submit"]')

        # Check result
        try:
            if expected_error:
                error_locator = page.locator(
                    f'div.alert.alert-danger:has-text("{expected_error}")'
                )
                expect(error_locator).to_be_visible(timeout=5000)
                message = f"✅ {name} - Error verified: {expected_error}"
            else:
                expect(page).not_to_have_url(LOGIN_URL, timeout=5000)
                message = f"✅ {name} - Login successful"

        except Exception as e:
            message = f"❌ {name} - Test Failed: {str(e)}"

        # Store result
        test_results.append(message)

        # Close browser
        browser.close()


def test_payvibe_login_cases():

    scenarios = [
        {
            "name": "Valid Email & Valid Password",
            "email": "devraj+2@laitkor.com",
            "password": "Lcs1423$#",
            "error_msg": None,
        },
        {
            "name": "Invalid Email & Invalid Password",
            "email": "devrajsir@laitkor.com",
            "password": "Lcs@@1423$#",
            "error_msg": "Please enter valid credential",
        },
        {
            "name": "Invalid Email & Valid Password",
            "email": "devrajsir@laitkor.com",
            "password": "Lcs1423$#",
            "error_msg": "Please enter valid credential",
        },
        {
            "name": "Valid Email & Invalid Password",
            "email": "devraj+2@laitkor.com",
            "password": "Lcs@@1423$#",
            "error_msg": "Please enter valid credential",
        },
        {
            "name": "No Credentials",
            "email": "",
            "password": "",
            "error_msg": "Email and Password fields are required",
        },
        
    ]

    # Run all scenarios
    for scenario in scenarios:
        run_login_test(
            name=scenario["name"],
            email=scenario["email"],
            password=scenario["password"],
            expected_error=scenario["error_msg"]
        )

    # Print final summary
    print("\n================ Test Summary ================\n")
    for result in test_results:
        print(result)
    print("\n=============================================\n")
