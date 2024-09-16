# Import necessary libraries
import streamlit as st
import pyktok as pyk
import os

# Function to save TikTok video
def save_tiktok_video(url):
    video_filename = 'video.csv'
    pyk.save_tiktok(url, True, video_filename)
    # Get all .mp4 files in the directory
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

    # Return any .mp4 file in the directory
    if mp4_files:
        return mp4_files[0]
    else:
        return None
  

# Streamlit app
def main():
    st.title("TikTok Video Saver")
    
    # Input field for TikTok URL
    url = st.text_input("Enter TikTok URL", "")
    
    # Button to save video
    if st.button("Save TikTok Video"):
        for file in os.listdir():
            if file.endswith(".mp4"):
                os.remove(file)

        video_filename = save_tiktok_video(url)
        st.success("Video saved successfully!")

        # Display the video
        video_file = open(video_filename, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, format='video/mp4')

        # Provide a download link
        st.download_button(label="Download Video", data=video_bytes, file_name=video_filename, mime='video/mp4')


if __name__ == "__main__":
    main()
