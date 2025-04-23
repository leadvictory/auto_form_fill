import json
from seleniumbase import SB

# Load JSON data
with open("urls.json", "r", encoding="utf-8") as f:
    data = json.load(f)

while True:
    with SB(uc=True) as sb:
        sb.open("https://reportcontent.google.com/forms/counter_notice?hl=en&web-redirect=f&product=websearch")
        sb.sleep(5)
        
        # Select Country (Turkey, index 230)
        sb.click("div.button.border.floated-label")
        sb.sleep(1)
        sb.click("material-select-dropdown-item:nth-of-type(230)")
        
        # Fill form fields from JSON
        sb.input('.mdc-text-field__input', data["your_name"])
        sb.input('input[aria-label="Your title"]', data["your_title"])
        sb.input('input[aria-label="Your company"]', data["your_company_name"])
        sb.input('input[aria-label="Contact email address"]', data["your_email"])
        sb.input('textarea[aria-label="Address"]', data["your_address"])
        sb.input('input[aria-label="Phone number"]', data["your_phone_number"])
        sb.input('textarea[aria-label="Url(s) of the content in question"]', "\n".join(data["website_url"]))
        sb.input('textarea[aria-label="Please provide more details to justify your request"]', data["your_details"])
        sb.input('input[aria-label="Signature"]', data["your_signature"])
        sb.click('//material-radio[.//div[text()="I am the owner of the content."]]')
        sb.wait_for_element_visible('//material-checkbox[@aria-labelledby="mat-label-jurisdiction-acknowledgement"]')
        sb.click('//material-checkbox[@aria-labelledby="mat-label-jurisdiction-acknowledgement"]')

        sb.wait_for_element_visible('//material-checkbox[@aria-labelledby="mat-label-good-faith-belief"]')
        sb.click('//material-checkbox[@aria-labelledby="mat-label-good-faith-belief"]')

        sb.wait_for_element_visible('//material-checkbox[@aria-labelledby="mat-label-accurate-information"]')
        sb.click('//material-checkbox[@aria-labelledby="mat-label-accurate-information"]')
        sb.sleep(36000)
