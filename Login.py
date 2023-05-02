import streamlit as st
from streamlit.components.v1 import html
import re
import gspread
import time
from datetime import datetime
# st.set_page_config(
# 	page_title = "skipText Login Page")
import st_pages
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title("Home")

# Specify what pages should be shown in the sidebar, and what their titles
# and icons should be
show_pages(
    [
        Page("Login.py", "Home", "🏠"),
        Page("pages/one.py", "Summarization Input Selection", ":books:"),
		Page("pages/two.py", "Summarization Play Ground", ":bar_chart:"),
        Page("pages/image.py", "Image Generation Tool", ":books:"),
        Page("pages/chatgpt.py", "ChatGPT Tool", ":books:"),
    ]
)

#st.sidebar.image: st.sidebar.image("SkipText Offiical Logo.png", use_column_width=True)
def is_valid_email(email):
    # Define a regular expression for checking the email format
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # Check if the email matches the regular expression
    if re.match(regex, email):
        st.session_state["email_id"] = email_id
        return True
    else:
        return False

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s)." + "links: "+ links[0]);
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

def append_row_to_gsheet(email_id):
    SHEET_ID = '16VaBizqUWdPa_JNCizMnbNHx-UPFrpehA9vqY1EhwpI'
    SHEET_NAME = 'Sheet1'
    gc = gspread.service_account('gsheet_credentials.json')
    spreadsheet = gc.open_by_key(SHEET_ID)
    worksheet = spreadsheet.worksheet(SHEET_NAME)
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    worksheet.append_row([email_id, dt_string])
    return True


# st.write("Hi! ")
tool_selection = str(st.selectbox("Which tool you wanted to use: ", ["None", "Summarization Tool", "Image Genration Tool", "ChatGPT Tool"]))

if tool_selection == "Summarization Tool":
    nav_page("Summarization%20Input%20Selection")
elif tool_selection == "Image Genration Tool":
    nav_page("Image%20Generation%20Tool")
elif tool_selection == "ChatGPT Tool":
    nav_page("ChatGPT%20Tool")



# if "email_id" not in st.session_state:
# 	email_id = str(st.text_input('Enter your email_id to continue..'))
# 	#st.session_state["email_id"] = email_id
# 	if is_valid_email(email_id) and append_row_to_gsheet(email_id):
# 		nav_page("Task%20Selection%20Page")
# 	elif len(email_id):
# 		st.write("Please enter a valid email_id")
# else:
# 	st.write("You are in!!! Click below button to use the tool")
# 	with st.form("form1"):
# 		use_tool = st.form_submit_button(label = 'Use Tool')
# 	if use_tool:
# 	    nav_page("Task%20Selection%20Page")
