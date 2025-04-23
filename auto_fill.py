from seleniumbase import SB

while True:
    with SB(uc=True) as sb:
        sb.open("https://reportcontent.google.com/forms/counter_notice?web-redirect=f&product=websearch")
        sb.sleep(5)
        dropdown_selector = "div.button.border.floated-label"
        sb.wait_for_element_visible(dropdown_selector)
        sb.click(dropdown_selector)
        sb.sleep(1)
        selector = "material-select-dropdown-item:nth-of-type(230)"
        sb.click(selector)
        sb.sleep(1)
        sb.input('.mdc-text-field__input', "demir seromic")
        sb.input('.mdc-text-field__input:nth-of-type(2)', "exulucive")
        sb.sleep(3600)
