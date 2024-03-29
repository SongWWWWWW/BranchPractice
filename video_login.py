# import streamlit as st

# # 视频文件路径
# video_path = "./hitwh.mp4"

# # 使用Streamlit的video组件展示视频
# st.video(video_path, format='mp4',width="100%")



# import streamlit as st

# # 视频文件路径
# video_path = "./hitwh.mp4"

# # 使用HTML自定义视频播放器，并设置为全屏显示
# video_html = f"""
# <video width="100%" height="100%" controls autoplay>
#   <source src="{video_path}" type="video/mp4">
#   Your browser does not support the video tag.
# </video>
# """

# # 使用CSS将视频全屏
# fullscreen_css = """
# <style>
#     video {
#         position: fixed;
#         width: 100%;
#         height: 100%;
#         top: 0;
#         left: 0;
#     }
# </style>
# """

# # 展示自定义视频播放器和CSS
# st.markdown(video_html + fullscreen_css, unsafe_allow_html=True)



# import streamlit as st

# # 视频文件路径
# video_path = "https://www.hitwh.edu.cn/_upload/article/videos/cb/d8/74e031f84885b4daaa85b4786f2c/e0051483-aa20-4c29-a51c-d604a4d402b2.mp4"
# # video_path = "./hitwh.mp4"
# # 使用HTML自定义视频播放器，并设置为全屏显示
# video_html = f"""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Local Video Player</title>
#     <link rel="stylesheet" href="styles.css">
# </head>
# <body>
#     <div class="video-container">
#         <video autoplay muted loop controls> <!-- 添加 controls 属性 -->
#             <source src="{video_path}" type="video/mp4">
#             Your browser does not support the video tag.
#         </video>
#     </div>
# </body>
# </html>"""



# # 使用CSS将视频全屏
# fullscreen_css = """
# <style>
#   body, html {
#       margin: 0;
#       padding: 0;
#       height: 100%;
#   }

#   .video-container {
#       width: 100%;
#       height: 100%;
#       position: relative;
#       overflow: hidden;
#   }

#   .video-container video {
#       position: absolute;
#       top: 0;
#       left: 0;
#       width: 100%;
#       height: 100%;
#   }
# </style>
# """


# # 展示自定义视频播放器和CSS
# st.markdown(video_html + fullscreen_css, unsafe_allow_html=True)







import streamlit as st

# 视频文件路径
video_path = "https://www.hitwh.edu.cn/_upload/article/videos/cb/d8/74e031f84885b4daaa85b4786f2c/e0051483-aa20-4c29-a51c-d604a4d402b2.mp4"

# 自定义HTML视频播放器，并设置为全屏显示
video_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fullscreen Video Player</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }}
        .video-container {{
            
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%)
            width: 100vw;
            height: 100vh;
        }}
        video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <div class="video-container">
        <video controls autoplay muted loop>
            <source src="{video_path}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
</body>
</html>
"""

# 展示自定义视频播放器
st.markdown(video_html, unsafe_allow_html=True)



