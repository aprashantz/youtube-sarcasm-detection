"""
this python file can be used to manually test sarcasm detection of youtube comments
without using front end interface that is also made for this system
how to test? answer: by running this file
"""
from youtube_comments import extract_youtube_comments
from MultinomialNaiveBayes import production_multinomial

key = "enter your google api key with youtube enabled"  # google api client api key
# enter video id of any public youtube videos. Note: video id is the last part of the video link
youtube_video_id = "YbJOTdZBX1g"
number_of_comments = 100  # enter how many comments you want to

youtube_comments = extract_youtube_comments(
    youtube_video_id, key, number_of_comments)  # to store comments

# to store list containing 0 or 1 values
sarcasm_result = production_multinomial(youtube_comments)

total_comments_taken = len(sarcasm_result)
total_sarcastic_comments = 0

for each in sarcasm_result:
    if (each == 1):
        total_sarcastic_comments += 1   # to find out total sarcastic comments

print("Total comments taken:", total_comments_taken)
print("Total sarcastic comments:", total_sarcastic_comments)
print(((total_sarcastic_comments/total_comments_taken)*100),
      "% sarcastic")  # to find sarcascm rate in percent
