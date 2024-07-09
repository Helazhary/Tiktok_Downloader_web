# Import necessary libraries
import streamlit as st
import pyktok as pyk
import os

# Function to save TikTok video
def save_tiktok_video(url):
    video_filename = 'video.mp4'
    pyk.save_tiktok(url, True, video_filename)
    return video_filename

# Streamlit app
def main():
    st.title("TikTok Video Saver")
    
    # Input field for TikTok URL
    url = st.text_input("Enter TikTok URL", "https://www.tiktok.com/@amr_eldezil/video/7389314858321267976?q=%D8%A7%D9%84%D8%A7%D9%87%D9%84%D9%8A&t=1719529026229")
    
    # Button to save video
    if st.button("Save TikTok Video"):
        video_filename = save_tiktok_video(url)
        st.success("Video saved successfully!")

        # Display the video
        video_file = open(video_filename, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

        # Provide a download link
        st.download_button(label="Download Video", data=video_bytes, file_name=video_filename, mime='video/mp4')

if __name__ == "__main__":
    main()
