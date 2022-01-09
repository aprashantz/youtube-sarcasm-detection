import googleapiclient.discovery


# function to return list of wanted youtube comments
# the source of reference in making this function is below
# https://developers.google.com/youtube/v3/docs/commentThreads/list
def extract_youtube_comments(video_id, google_api_key, approx_numof_comments):
    extracted_comments = []  # will append all collected comments here

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=google_api_key)
    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=approx_numof_comments,
        order="relevance",
        videoId=video_id,
    )
    response = request.execute()
    filtered_response = response["items"]

    for each in filtered_response:
        extracted_comments.append(
            each["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
        # we only need comments, so taking only textOriginal from json response
    while (("nextPageToken" in response) & (approx_numof_comments > 100)):
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            order="relevance",
            videoId=video_id,
            pageToken=response["nextPageToken"],
        )
        response = request.execute()
        filtered_response = response["items"]

        for each in filtered_response:
            extracted_comments.append(
                each["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

        if (len(extracted_comments) >= approx_numof_comments):
            break
    return extracted_comments
