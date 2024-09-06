# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from eda import eda
from ml import ml

def main():

	menu = ["Home", "Exploratory Data Analysis Section", "Prediction Section", "About"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("# Early Stage heart attack risk predictor app")
		img = Image.open("heart.jpeg")
		st.image(img)

		

		st.write("""

The data that we use in this particular app contain the features of a newly heart disease patient 
or a diabetic patient.

### DataScource

	- https://archive.ics.uci.edu/ml/datasets/heart+disease

### App Content

	- This app has four sections
	1) Home Page - The page you are currently in

	2) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

	3) Prediction- The page in which you will be asked to give the information on all the medical aspects
		and we will predict the desired the output

	4) About - This Page is about me

			""")
	elif choice=="Exploratory Data Analysis Section":
		eda()
	elif choice == "Prediction Section":
		ml()
	else:
		st.subheader("About")
		
		st.write("### Ritik Kumar - The Tech Guy")
		img = Image.open("pic.jpg")
		st.image(img)

		st.text("""
		My ambitious dream to become a software engineer is soon to be a reality.
		As I am pursuing computer science, I build computer applications and muscles too.
		I strive to use my energy in data science to make significant contributions to society by 
		tackling complex problems through research and cutting edge technologies.
		Creative problem solver with strong interpersonal skills. Dreaming of taking the world 
		towards a safer and healthier future.
		I love meeting people working on exciting things. If there is any suitable role for me, 
		don't hesitate. I am open to communication on all channels. Let's discuss.
""")
		socials = ["LinkedIn","Github","GMail"]
		linkedin = "https://www.linkedin.com/in/ritikkrsingh01/"
		
		github = "https://github.com/ritikkumar55"
		mail = "hrithik21sgh@gmail.com"
		
		with st.expander("Links to all my Socials"):
			a = st.selectbox("Socials", socials)
			if a =="LinkedIn":
				st.write(linkedin)
			elif a =="Github":
				st.write(github)
			elif a=="GMail":
				st.write(mail)
			

			
			


main()
