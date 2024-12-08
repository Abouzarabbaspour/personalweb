# write my personal web page
# first segment about me and there is my photo
# second segment about my education
# third segment about my work experience
# fourth segment about my skills
# fifth segment about my hobbies
import streamlit as st 

# Custom CSS for vertical line timeline
st.markdown(
    """
   <style>
    .timeline-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-left: 20px; /* Adjust for positioning */
        position: relative;
    }

    .timeline-line {
        position: absolute;
        left: 120px; /* Adjust to align with dots */
        top: 0;
        bottom: 0;
        width: 2px;
        background-color: #ccc;
    }

    .timeline-event {
        position: relative;
        margin: 0px 0;
        margin-top: 20px;
        display: flex;
        align-items: center;
        width: 100%;
    }

    .timeline-logo {
        position: absolute;
        left: 0px; /* Align logo to the left side of the line */
        width: 20px; /* Adjust logo size */
        height: 20px;
        padding: 2px;
        background: white;
    }

    .timeline-dot {
        position: absolute;
        left: 115px; /* Align with the timeline line */
        width: 12px;
        height: 12px;
        background-color: #007BFF;
        border-radius: 50%;
    }

    .timeline-text {
        margin-left: 140px; /* Space between dot and text */
        font-size: 14px;
    }
   .timeline-img {
        margin-left: 200px; /* Space between dot and text */
        font-size: 14px;
    }
   
   .timeline-event img {
        margin-top: 15px;
        width: 100px; /* Adjust size */
        height: auto;
        border-radius: 4px; /* Optional for rounded corners */
    }
    .timeline-img .img_full {
        margin-top: 2px;
        width: 250px; /* Adjust size */
        height: auto;
        border-radius: 8px; /* Optional for rounded corners */
    }
    .timeline-img .img_full_land {
        margin: 2px;
        height: 250px;
        width: auto; /* Adjust size */
        border-radius: 8px; /* Optional for rounded corners */
    }

    .timeline-img .img_screenshot {
        margin: 5px;
        width: 190px; /* Adjust size */
        height: auto;
        border-radius: 8px; /* Optional for rounded corners */
    }
    .timeline-img .img_logo {
        margin-top: 2px;
        width: 100px; /* Adjust size */
        height: auto;
        border-radius: 8px; /* Optional for rounded corners */
    }
    .timeline-event iframe {
        margin-top: 15px;
        width: 100px; /* Adjust size */
        height: auto;
        border-radius: 8px; /* Optional for rounded corners */
    }
    .benameoo {
        width: 100px; /* Adjust logo size */
        height: auto;
        padding: 10px;
        background: white; 
        border-radius: 6px; /* Optional for rounded corners */
        z-index:1;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# Add other Streamlit content
# st.write("This is a vertical timeline aligned to the left side of the page.")

# center image
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 80%;  /* Adjust this value as needed */
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

     .header-container {
        position: relative;
        height: 300px;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
    }
    .header-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 0;
    }
    .note{
     position:absolute;
     font-size: 0.9em;

    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown("""<div> <img src="https://i.ibb.co/pytJM8W/benamekhoda.png" class="center benameoo" > </div>""", unsafe_allow_html=True)
# st.image("./res/benamekhoda.png", use_column_width=False, width=90)



st.markdown("""
                <div class="header-container">
                        <video class="header-video" autoplay muted loop>
                                <source src="https://rr3---sn-5hne6nz6.googlevideo.com/videoplayback?expire=1733698721&ei=QdBVZ9-LD8O_vcAPh8aYwQ4&ip=117.5.146.101&id=o-AAgvV4rv9nCjArxfG8iIFwMpWPxf05DMdXi_hHqZlOwW&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AQn3pFTs5ecgbILik8WX7Imlo0T-YDRj9yt_j5Kaq2P5a3fB7YaMFQyfqtwSUJzPbQWfDdp7l4FGfGgP&vprv=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=356917681&dur=7488.582&lmt=1730920060203619&keepalive=yes&fexp=24350590,24350675,24350705,24350737,24350850,51326932,51335594,51347746&c=ANDROID_VR&txp=5432434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAP4L8PnuK44GueDgH84EZMtuJ2l-i5n_3iOq3IKUilx2AiA3Gu-oVjN9gDDL2lBEUf5QCKjk7i0GnMbc06P9VMxXPw%3D%3D&rm=sn-8pxuuxa-i5odr7s,sn-8pxuuxa-i5o6d7l&rrc=79,79,80&req_id=52c67fc005a9a3ee&cmsv=e&redirect_counter=3&cm2rm=sn-i3bd67l&cms_redirect=yes&met=1733677145,&mh=si&mip=85.146.125.156&mm=34&mn=sn-5hne6nz6&ms=ltu&mt=1733676748&mv=m&mvi=3&pl=20&rms=ltu,au&lsparams=met,mh,mip,mm,mn,ms,mv,mvi,pl,rms&lsig=AGluJ3MwRgIhANcKZCZmGyTLrhs_-E-XDXibnF-3NbreC45uYRgABWjnAiEAkvkenjpxQErWFM-c1R7G9kHRZJqZILXMFAIcDnsIPiA%3D" type="video/mp4">
                        </video>
                         <img src="https://i.ibb.co/pytJM8W/benamekhoda.png" class="center benameoo" >
                </div>
            """, unsafe_allow_html=True)
st.title("")

# add a photo of element
# rotate the photo
st.image("https://i.ibb.co/nwLL0FB/me.png", caption="Me", width=350, output_format="JPEG")



# st.caption("🚀 Let's get to know each other 👨‍💻"
#             "📚"  "🛠️"  "🧠"  "🎨")

st.header("👨‍💻 About Me")

st.write("I consider my self a problem solver that has a background in computer engineering. Currently I am more interested in machine learning and data engineering. I have passion for creating out of box solutions to complex problems. I conceptualize solutions using Java, Kotlin, and Python, bringing them to life on ESP32 boards."
     "📧"  "📱"  "🌐")

# video_file = open("./res/me.mp4", 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes, autoplay=True, start_time=0)

st.header("🛠️ Work Experience"
         "📈")

# ascii art of tesla logo


st.markdown(
    """
    <div class="timeline-container">
        <div class="timeline-line"></div>
        <div class="timeline-event">
            <img src="https://seekvectors.com/files/download/tesla-logo-02.jpg" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2023 - Now</strong> - <strong>Tesla</strong> - At Tesla, I focus 70% on data engineering and 30% on machine learning. I develop and deploy predictive maintenance ML models, create custom Airflow operators to make workflows run smoothly, and design CI/CD pipelines to simplify code deployment. I also manage Kubernetes applications for scalability and build base images to make ETL/ELT processes more efficient. </p>
            </div>
        </div>
        <div class="timeline-img">
                <img class="img_screenshot" src="https://i.ibb.co/M1Sg47d/P-20240227-153217.jpg" alt="Event Image 4">
                <img class="img_full_land" src="https://i.ibb.co/4Fv73Lf/Tesla-battery-3.webp" alt="Event Image 4">
        </div>
        <div class="timeline-event">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs3AKUU4lo_r_hoxgBtyHoghRvWpV9CZFxlw&s" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2021 - 2023</strong> - <strong>Bol(.)com</strong> - Employed as a Senior Data Engineer, I transitioned into a Machine Learning Engineer role. In this position, I developed, validated, and deployed ML models on GCP infrastructure. One of the highlights was the 'Favorite Brand' project, where we developed an internal app to test and validate the recommendation engine model. After successful validation, the model was deployed for approximately 6 million users. Additionally, I designed and deployed real-time inference pipelines.</p>
            </div>
        </div>
        <div class="timeline-img">
                <iframe width="400" height="240" src="https://www.youtube.com/embed/4trCxsMAUHg?si=TcDekI6pa6Ibnk4g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                <img class="img_full" style="position:absolute; margin-left:10px;" src="https://i.ibb.co/KDK59GY/Screenshot-2024-12-07-at-23-48-01.png" alt="Event Image 4">
                <p class="note" >Validating ML model by creating a web app</p>
        </div>
        <div class="timeline-img">
                <img class="img_full_land" style="width:400px; height:auto; margin-top:20px;" src="https://i.ibb.co/Yy1N1Lh/Screenshot-2024-12-07-at-23-29-51.png" alt="Event Image 4">
                <p class="note">Graph neural network representation</p>
        </div> 
        <div class="timeline-event">
            <img src="https://content.presspage.com/clients/o_1828.jpg" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2019 - 2021</strong> - <strong>Efteling</strong> - I was a data scientist in Efteling, but sometimes I had to develope a research/survey android app to collect data as well . My main contribution was to develope queue waiting time forecasting models,and  next best action recommendation engine for amusement park. Everyhting deployed on AWS, using Sagemaker, Athena, Dyanamo, Airflow. </p>
            </div>
        </div>
        <div class="timeline-img">
                <img class="img_full_land" src="https://i.ibb.co/h9kpsPd/Screenshot-2024-12-07-at-23-17-59.png" alt="Event Image 4">
                <p class="note">Recommendation app</p>
                <img class="img_full_land" src="https://i.ibb.co/VVdG14R/Screenshot-2024-12-07-at-23-17-34.png" alt="Event Image 4">
        </div>
        <div class="timeline-img">
                <iframe width="400" height="240" style="margin-top:10px; margin-top:20px;" src="https://www.youtube.com/embed/rMogWSvMmVU?si=nZsdXfUmD3zDLpxb"  frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                <p class="note">Visitors' movement analysis</p>
                <img class="img_full_land" style="position:absolute; margin-left:10px; margin-top:20px;"  src="https://i.ibb.co/pXkzN3G/Screenshot-2024-12-07-at-23-06-12.png" alt="Event Image 4">
         </div>
        <div class="timeline-event">
            <img src="https://www.win.tue.nl/SoCG2015/images/logos/tue.png" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2018 - 2020</strong> - <strong>TU/e Engineering Docotorate projects</strong> -  I worked with many companies to accelerate their adoption of data science for solving their problems, where applicable, implementing machine learning solutions on-prem or on cloud.</p>
            </div>
        </div>
        <div class="timeline-img">
                <iframe  width="400" height="240"  style="margin-right:10px;" src="https://www.youtube.com/embed/3JVW41NUiYA?si=O6GZceCfHhowrW8N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                <p class="note">Step detection</p>
                <iframe  width="400" height="240"  src="https://www.youtube.com/embed/AQzkKwYRjF4?si=4LJvt79dVh2Lgu2q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                <iframe width="400" height="240" style="margin-top:20px;"  style="margin-top:20px;" src="https://www.youtube.com/embed/N67juFaDSr0?si=4SlIdlFlVKWiLsMD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                <p class="note">Whooping cough spread</p>
        </div>
        <div class="timeline-event">
            <img src="https://i.ibb.co/SQC65bT/Screenshot-2024-12-01-at-20-42-11.png" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2015 - 2018</strong> - <strong>Netgat</strong> - I was co-founder of a startup called Netgat. Netgat was a tool that helped a mobile operator to monitor and evaluate it's network quality and services across the country. The raw data was coming in from an SDK within mobile app and routed to Netgat endpoints waiting to store and analyze the data. Netgat command center Would present the data to technical teams within the network operator.</p>
            </div>
        </div>
        <div class="timeline-img">
                <img class="img_full_land" src="https://i.ibb.co/D4Fx1QB/Copy-of-n-3.png" alt="Event Image 4">
                 <p class="note">Network data coverage layer map</p>
        </div>
        <div class="timeline-event">
            <img src="https://d1hbpr09pwz0sk.cloudfront.net/logo_url/hamrahe-aval-mci-41f2bca4" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2013 - 2018</strong> - <strong>Hamrah e Aval - MCI</strong> - I was software engineer in network department, I developed analytical softwares that helped management root cause problems. I introducted service oriented software development architecture. We did everything from A to Z, installing and maintain hardwares and servers to develope, test, deploy, maintain the applications. </p>
            </div> 
        </div>
         <div class="timeline-img">
                <img class="img_full_land" src="https://i.ibb.co/T8FJSCX/Screenshot-2024-12-07-at-17-57-51.png" alt="Event Image 4">
                <p class="note">Presentation in MCI</p>
        </div>
         <div class="timeline-event">
            <img src="https://static.vecteezy.com/system/resources/thumbnails/002/227/847/small/programmer-computer-expert-black-linear-icon-vector.jpg" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
                  <p><strong>2011 - 2016</strong> - <strong>App developer as a side hustle</strong> - I was doing freelance Android app development, developed multiple successfull apps. Getagram with over 200k installs, playit!, crosswords,...</p>
            </div> 
        </div>
        <div class="timeline-img"> 
                <img class="img_logo" src="https://s.cafebazaar.ir/images/upload/icons/com.nomad.comet.png" alt="Event Image 4">
                 <p class="note"> Apps in cafebazaar</p>
                <img class="img_logo" src="https://s.cafebazaar.ir/images/upload/icons/com.nomad.playit.png" alt="Event Image 4">
                <img class="img_logo" src="https://s.cafebazaar.ir/images/upload/icons/com.nomad.getagram.png" alt="Event Image 4">
                <img class="img_screenshot" src="https://i.ibb.co/syh6XJg/Screenshot-2024-12-07-at-19-41-16.png" alt="Event Image 4">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.header("📚 Education"
              "🎓" )


# Timeline structure
st.markdown(
    """
    <div class="timeline-container">
        <div class="timeline-line"></div>
        <div class="timeline-event">
            <img src="https://www.win.tue.nl/SoCG2015/images/logos/tue.png" alt="Logo 2" class="timeline-logo">   
            <div class="timeline-dot"></div>
            <div class="timeline-text">
            <p><strong>2018 - 2021 - EngD (Engineering Doctorate) at Eindhoven university of Technology (Eindhoven, The Netherlands).</strong> For my EngD I had projects regarding NLP, Graph theory, Signal processing, machine learning and their intersection. My final project was to develope and end-to-end recommendation system for Efteling in the Netherlands. I had privilage to be nominee for best thesis award of 2021."
       </p>
        </div>
        </div>
        <div class="timeline-img">
         <iframe width="400" height="240" style="margin-right:15px;" src="https://www.youtube.com/embed/mvT2HctOhpQ?si=pJU5xxpYNDPX7e_u&amp;start=15&amp;clip=Ugkx3j-oikrbrsJs-OuMwKDDFBR0eoGamx3R&amp;clipt=EP2HgAIYta6BAg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
          <p class="note"> TU/e Thesis award</p>
         <iframe width="400" height="240" src="https://www.youtube.com/embed/-VUU-dj8Dp8?si=0WsIqQT1tj2slrbs&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
         </div>
         <div class="timeline-img">
         <img class="img_full" style="margin-top:20px;" src="https://i.ibb.co/7YSfywT/Screenshot-2024-12-07-at-17-26-05.png" alt="Event Image 4">
          <img class="img_full_land" style="margin-left:160px;" style="margin-left:15px;" src="https://i.ibb.co/0syLN0C/20190129-182428.jpg" alt="Event Image 4">
         </div>
        <div class="timeline-event">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/University_of_Tehran_logo.svg/1200px-University_of_Tehran_logo.svg.png" alt="Logo 2" class="timeline-logo">
            <div class="timeline-dot"></div>
            <div class="timeline-text">
            <p><strong>2012 - 2015 - MSc in Computer Engineering from the university of Tehran (Tehran, Iran).</strong> I had privilage to work with some great professors that guided my interests into learning distributed systems and distributed programming like Hadoop, machine learning. My Thesis was churn analysis on social network data."
                </p>
                </div>
        </div>
        <div class="timeline-img">
        <iframe  width="400" height="240" src="https://www.youtube.com/embed/j5DuOCifX9s?si=UOBWqxGGwX4aQ73C&amp;start=15" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
         <p class="note"> Social network visualization</p>
        <img class="img_full_land" style="position:absolute; margin-left:10px;" src="https://i.ibb.co/1X01w0J/screenshot-132530.png" alt="Event Image 4">
        </div>
        <div class="timeline-img">
        <img class="img_full_land" style="margin-top:20px;" src="https://i.ibb.co/kDFLR1K/IMG-20160118-220435.jpg" alt="Event Image 4">
        </div>
        <div class="timeline-event">
           <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Azad_University_logo.png/800px-Azad_University_logo.png" alt="Logo 2" class="timeline-logo">
             <div class="timeline-dot"></div>
            <div class="timeline-text">
            <p><strong>2008 - 2012 - BSc in Computer Engineering from Azad university of Sari (Mazandaran, Iran).</strong> I was very much interested in any course software development related. usually tried to ace my programming courses wether it was in Assembly, Pascal or C++ ,... "
       </p>
        </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.write("Wherever I am, all my love goes to my root and my country as I would be nothing without it. Iran and Mazandaran."
        "❤️" "🇮🇷" "🌐")
st.markdown(
    """
    <iframe  width="1400" height="240" src="https://www.youtube.com/embed/tsIwBqXL4UM?si=oDzb3KwBuSruevb2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)


st.caption("🚀 Let's connect" "📧"  "📱"  "🌐")
st.caption("🚀 Thank you for visiting my page"
              "👋"  "🚀"  "🌟"  " 🎉")

# Path: test.py
# Compare this snippet from about_me.py:



