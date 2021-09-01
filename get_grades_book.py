import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import unicodedata


""" Copy and rename the secrets_env template in this repo to secrets.env.
    Add your own login and password for https://myschool.pacyber.org"""
load_dotenv('secrets.env')

""" Your login information below. It's probably best to store this in environment variables."""
tbLogin = os.environ.get('TBLOGIN')
tbPassword = os.environ.get('TBPASSWORD')

""" Uncomment below and comment out above if you're not using environment variables"""
# tbLogin = "login_id"
# tbPassword = "login_pass"

""" Internal URL that requires user to be logged in"""
SCRAPEURL = 'https://myschool.pacyber.org/FEGradebook.aspx'

"""Here is where we setup headers to make it look like a browser"""
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.99 Safari/537.36'
}

"""This is a dictionary for storing the login post request. 
Notice '__VIEWSTATE, __VIEWSTATEGENERATOR, __EVENTVALIDATION' are set to None. They will be populated."""
login_data = dict(__VIEWSTATE=None,
                  __VIEWSTATEGENERATOR=None,
                  __EVENTTARGET="",
                  __EVENTARGUMENT="",
                  __EVENTVALIDATION=None,
                  tbLogin=tbLogin,
                  tbPassword=tbPassword,
                  btLogin="")  # We'll populate this below after we initilize the session.


def get_academic_snapshot():
    with requests.Session() as s:
        """Open a requests session, Store the correct auth headers."""
        url = 'https://myschool.pacyber.org/Login.aspx'  # Login URL
        r = s.get(url, headers=headers)  # This is where we make the first request to generate an authenticity_token
        """We're using Beautiful Soup to scrape the token form the page source"""
        soup = BeautifulSoup(r.content, 'html.parser')

        """Here we are populating login_data dictionary with the scraped auth tokens"""
        login_data['__VIEWSTATE'] = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
        login_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'name': '__VIEWSTATEGENERATOR'})['value']
        login_data['__EVENTVALIDATION'] = soup.find('input', attrs={'name': '__EVENTVALIDATION'})['value']
        """Finally we submit the post request with the same 's' session passing the url,
         login_data, and headers for user agent."""
        r = s.post(url, data=login_data, headers=headers)

        """Now we can scrape any url that requires a user to be logged in
        as long as we use the same session object 's' """
        page = s.get(SCRAPEURL)

        bs = BeautifulSoup(page.content, 'html.parser')

        """ Grab the tables for the subjects and their corresponding info """
        try:
            grade_book_table = bs.find("table", {"id": "ctl00_ContentPlaceHolder1_GradebookInfo1_gvCourses"})
            grade_book_rows = grade_book_table.findAll('tr')

        except Exception as e:
            # If the above doesn't work there is a good chance it's because the password isn't correct.
            return "Please Check your secrets.env and ensure your login and password are correctly set."

        msg = ""
        for row in grade_book_rows:
            td = row.find_all('td')
            row = [unicodedata.normalize("NFKD", i.text) for i in td]
            try:
                msg += "\n".join([f"Subject: {row[2]}",  # Third Column
                                  f"Score: {row[5].split(' ')[0] or None}",  # Fourth Column or 'None' if there isn't a grade yet
                                  f"Progress: {row[6]}",  # Fifth Column
                                  "\n"])
            except IndexError:
                """Some of the rows returned do not have data in the expected format. 
                We don't need these so we just pass."""
                pass

        return msg


if __name__ == "__main__":
    print(get_academic_snapshot())
