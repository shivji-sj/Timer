# making the timer app in streamlit
import streamlit as st
import time
from  PIL import Image
 
st.title("Timer")
image = Image.open("timer3.jpg")
st.image(image)

# link credit
url = "https://unsplash.com/photos/BXOXnQ26B7o"
st.markdown("Image Credit : [Unsplash](%s)" % url) # st.write()  we also use


# countdown function to perform timer operation
def countdown(ts):
	with st.empty():
		while ts:
			# for 2.30 minute          =  divmod(60*2.50, 60)
			# for 5.00 minute          =  divmod(60*5, 60)
			mins, secs  = divmod(ts, 60) # 24*60 divided by 60
			time_now = "{:02d}:{:02d}".format(mins, secs)
			st.header(time_now)
			time.sleep(1)
			ts-=1
		st.write("Times Up!")
		

def main():
	
	# imput variables
	time_in_minute = st.number_input("Time in Minute"	, min_value=0)
	time_in_second = time_in_minute*60


		# start the countdown
	col1, col2 = st.columns(2)


	with col1:
		if st.button("Start"):
			countdown(time_in_second)
			
	with col2:
		st.button("Stop")


	# Follow me link
	github_url = "https://github.com/shivji-sj"
	linkedin_url ="https://www.linkedin.com/in/shivji-881449205/recent-activity/"
	medium_url = "https://medium.com/@sjshivji"

	st.header("Follow Me : ")

	col1, col2, col3 = st.columns(3)

	with col1:
		st.markdown("[GitHub](%s)" % github_url)
	with col2:
		st.markdown("[LinkedIn](%s)" % linkedin_url)
	with col3:
		st.markdown("[Medium](%s)" % medium_url)


# deriver code
if __name__=="__main__":
	main()