import streamlit as slt
import requests
from streamlit_lottie import st_lottie

hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
"""
def local_css(file_name):
    with open(file_name) as f:
        slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        
def load(url):
    r = requests.get(url)
    if r.status_code!=200: 
        return None
    return r.json()

lottie_coding1 = load("https://assets7.lottiefiles.com/packages/lf20_pjaextie.json")
lottie_coding2 = load("https://assets1.lottiefiles.com/packages/lf20_mf5j5kua.json")
lottie_coding3 = load("https://assets6.lottiefiles.com/packages/lf20_mdbdc5l7.json")
lottie_coding4 = load("https://assets2.lottiefiles.com/packages/lf20_26KVdO.json")
lottie_coding5 = load("https://assets8.lottiefiles.com/packages/lf20_1lgyzo9c.json")

slt.set_page_config(page_title="Fun Era",page_icon=":tropical_fish:",layout="wide")
slt.markdown(hide_style,unsafe_allow_html=True)

with slt.container():
    left, right = slt.columns((2,1))
    with left:
        slt.header("Fun Era :eagle:")
        slt.title("Welcome to our swimming club :surfer:")
        slt.write("### Do you wanna want some fun? :fish:")
        slt.write("### Join our fun era club :fish:")
    with right:
        st_lottie(lottie_coding1,height=300,key="Swim")
slt.write("---")

with slt.container():
    left1, right1 = slt.columns(2)
    left2, right2 = slt.columns(2)
    with left1:
        slt.write("""
        Details:
        - Club Name : Fun Era
        - Location  : Harawala Dehradun Uttarakhand, India
        - Open Timing : Morning - 8 AM to 11 AM , Evening - 3 PM to 6 PM
        - Sunday Closed!
        - Entry Fee : Rs 500 :dollar:
        - Ratings : 14.8 :star: :star: :star: :star: :star:
        """)
        slt.write("---")
    with right1:
        st_lottie(lottie_coding2,height=250,key="Detail")

slt.markdown(">## Article :pencil:")
slt.write(""" 
        The joys of swimming in a club
        - For a sport that is fundamentally an individual endeavour, there is something more to a swimming club than 
          a bunch of people slogging up and down, in splendid isolation, being shouted at by a coach. Being crammed half 
          naked into a small overheated swimming pool with your club mates, with too many people sharing a lane and swimming at speed, 
          requires seamless cooperation from all who are present. Very quickly in a club, at any one time, you have to work out who 
          is fastest on stroke x; who is having a good day and has lots of energy and has to go at the front and "lead the lane", 
          and who is having a rubbish day and should be left to draft and work their frustrations out. Who should be slightly chided 
          for being lazy and who needs extra encouragement because they really need it that day. Close physical proximity breeds closeness. 
          Closeness breeds support.

        - There is the shared pain of a hard session, when everyone encourages one other when flagging 
          ("Come on, only four more lengths to go!"). And the collective euphoria and pride when the swimming coach praises 
          you all at the end of a session for working hard. Club mates text you to ask why you skipped that early-morning session last week, 
          and peer pressure makes you turn up when you'd much rather be sleeping.
        - Most masters clubs will welcome swimmers of any age over 18, as long as they can swim a decent distance without stopping.
        - Today swimming is the second most popular exercise activity in the India, with approximately 360 million 
          annual visits to recreational water venues. Swim clubs, recreation centers, Y's, and many other facilities feature swimming pools.
          Many high schools and colleges have competitive swim teams, and of course, swimming is one of the most popular Olympic sports. 
          Millions of Americans are swimming each year. 
        
        Health Benefits of swimming:-
        - Low Impact.
        - Can be continued for a lifetime.
        - Build cardiorespiratory fitness.
        - Build muscle mass.
        - An alternative when injured.
        - It's a family affair.
        - Burns calories.
        - Accessibility.
        - Stress relief.
        - Relaxation.
        - Coordination and balance.
        """)
slt.write("---")
with slt.container():
    left1, right1 = slt.columns((2,2))
    with left1:
        st_lottie(lottie_coding3,height=250,key="fun")
    with right1:
        slt.subheader("Have a fun")
        slt.write(":point_right: Provide best quality swimming products.")
        slt.write(":point_right: Healthy food for every time (Breakfast, Lunch, Dinner).")
        slt.write(":point_right: Family hotel rooms available.")
        slt.write("---")
slt.write("># :point_right: Hotels:- :hotel:")
with slt.container():
    left1, right1 = slt.columns((2,2))
    with left1:
        st_lottie(lottie_coding4,height=300,key="hotel1")
    with right1:
        slt.write("### 1. The Solitaire Express")
        slt.write("3.9 :star: :star: :star: :star: (767)")
        slt.write("Fees: Rs 1,646 :dollar:")
        slt.write("Very Good")
        slt.write("---")
with slt.container():
    left1, right1 = slt.columns((2,2))
    with left1:
        st_lottie(lottie_coding4,height=300,key="hotel2")
    with right1:
        slt.write("### 2. Hotel Doon's Pride")
        slt.write("4.2 :star: :star: :star: :star: (293)")
        slt.write("Fees: Rs 1,992 :dollar:")
        slt.write("Excellent")
        slt.write("---")
with slt.container():
    left1, right1 = slt.columns((2,2))
    with left1:
        st_lottie(lottie_coding4,height=300,key="hotel3")
    with right1:
        slt.write("### 3. JJK Resort")
        slt.write("4.5 :star: :star: :star: :star: :star: (50)")
        slt.write("Fees: Rs 2,016 :dollar:")
        slt.write("Excellent")
        slt.write("---")
with slt.container():
    left1, right1 = slt.columns((2,2))
    with left1:
        st_lottie(lottie_coding4,height=300,key="hotel4")
    with right1: 
        slt.write("### 4. Hotel Shivam Residency")
        slt.write("3.3 :star: :star: :star: (192)")
        slt.write("Fees: Rs 1,024 :dollar:")
        slt.write("Good")
        slt.write("---")
slt.write("---")
with slt.container():
    slt.write('## Join Our Fun Era Club :thought_balloon:'); slt.write("##")
    contact_form = """
    <form action="https://formsubmit.co/3469harshsharma@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left1, right1 = slt.columns((2,2))
    with left1:
        slt.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
    with right1:
        st_lottie(lottie_coding5,height=250,key="Join")
