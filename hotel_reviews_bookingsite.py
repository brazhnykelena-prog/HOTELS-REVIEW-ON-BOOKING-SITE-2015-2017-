
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
from plotly.subplots import make_subplots
import streamlit as st

# ---- Page config ----
st.set_page_config(layout='wide')

# ---- Initialize session state ----
if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False

if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = True  # sidebar appears in dashboard

# ---- Function to display main markdown ----
def main_markdown():
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #001f3f, #003f7f, #001f3f);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
        box-shadow: 0px 0px 25px #00d4ff;
    ">
        <h1 style="
            font-size: 45px;
            font-weight: bold;
            color: #00eaff;
            text-shadow: 0px 0px 12px #00eaff;
            margin: 0;
            padding: 0;
        ">
            <span style="font-size:50px;">🏨</span>
            <span style="text-decoration: underline;">
                Hotels Reviews in Booking Site (2015–2017)
            </span>
            <span style="font-size:50px;">🌊</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)


# ---- Home Page ----
if not st.session_state.show_dashboard:
    main_markdown()

    # صورة
    st.image(
        "https://storage.googleapis.com/twg-content/images/booking-com-video-hero.width-1200.jpg",
        width=1200
    )

    # زرار في النص تحت الصورة
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("📂  Click double to navigate"):
            st.session_state.show_dashboard = True

# ---- Dashboard Page ----
if st.session_state.show_dashboard:
    main_markdown()  # يظهر الـ markdown فقط بدون الصورة

    # ---- Sidebar ----
    with st.sidebar:
        st.title("📊 Data navigation")

        # ---- أسماء الأزرار ----
        button_names = [
            "overview", "reviewers nationality", "years", "seasons","hotels",
            "trip type", "travelers status", "pets_lovers", "best_destinations" 
        ]

        # ---- CSS للأزرار ----
        st.markdown("""
        <style>
        .custom-btn {
            background: #0a192f;
            color: #00e5ff;
            font-weight: 800;
            font-size: 24px;
            padding: 18px 28px;
            border-radius: 14px;
            width: 100%;
            text-align: center;
            margin: 14px 0;
            border: none;
            cursor: pointer;
            box-shadow: 0 0 12px rgba(0, 229, 255, 0.4);
            animation: glow 2s infinite ease-in-out;
        }
        .custom-btn:hover {
            background: #112240;
        }

        @keyframes glow {
            0%   { box-shadow: 0 0 6px rgba(0, 229, 255, 0.4); }
            50%  { box-shadow: 0 0 20px rgba(0, 229, 255, 0.9); }
            100% { box-shadow: 0 0 6px rgba(0, 229, 255, 0.4); }
        }
        </style>
        """, unsafe_allow_html=True)


        # نحتاج session_state لتتبع الضغط
        if "clicked" not in st.session_state:
            st.session_state.clicked = None


        # JavaScript function to trigger streamlit event
        trigger_js = """
        <script>
        function trigger(name) {
            const input = window.parent.document.querySelector(
                `input[data-testid="${name}"]`
            );
            if (input) { input.click(); }
        }
        </script>
        """
        st.markdown(trigger_js, unsafe_allow_html=True)


        # عرض الأزرار
        for name in button_names:

            # HTML زر واحد فقط
            st.markdown(
                f"<button class='custom-btn' onclick=\"trigger('btn-{name}')\">{name.title()}</button>",
                unsafe_allow_html=True
            )

            # زر streamlit مخفي لاستقبال الضغط
            pressed = st.checkbox("", key=f"btn-{name}", label_visibility="hidden")

            if pressed:
                st.session_state.clicked = name
#..............................................................................................................................................

    # عرض المحتوى
    if st.session_state.clicked == "overview":
        st.markdown("""
        <div style="
            text-align: center;
            font-weight: bold;
            font-size: 32px;
            background: linear-gradient(to right, gold, darkorange);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            display: inline-block;
        ">
            DATA CONTENT
            <span style="
                display: block;
                width: 100%;
                height: 4px;
                background-color: red;
                margin-top: 6px;
                border-radius: 2px;
            "></span>
        </div>
        """, unsafe_allow_html=True)

        df=pd.read_csv('hotel_review_final.csv')
        st.dataframe(df)

        st.markdown("""
        <div style="
            text-align: center;
            font-weight: bold;
            font-size: 32px;
            background: linear-gradient(to right, gold, darkorange);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            display: inline-block;
        ">
            DATA BASICS
            <span style="
                display: block;
                width: 100%;
                height: 4px;
                background-color: red;
                margin-top: 6px;
                border-radius: 2px;
            "></span>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(df.describe())
        st.dataframe(df.describe(include='object'))

        st.markdown("""
        <div style="
            text-align: center;
            font-weight: bold;
            font-size: 32px;
            background: linear-gradient(to right, gold, darkorange);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            display: inline-block;
        ">
            DATA CRITERIA
            <span style="
                display: block;
                width: 100%;
                height: 4px;
                background-color: red;
                margin-top: 6px;
                border-radius: 2px;
            "></span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            font-family: 'Arial', sans-serif; 
            font-size: 18px; 
            line-height: 1.8; 
            color: #7FDBFF;  /* سماوي فاتح مريح للعين */
            padding: 10px;
        ">
            <p>👉 <b>Hotel_Address:</b> Address of hotels.</p>
            <p>👉 <b>Review_Date:</b> Date when reviewer posted the corresponding review.</p>
            <p>👉 <b>Average_Score:</b> Average Score of the hotel, calculated based on the latest comment in the last year.</p>
            <p>👉 <b>Hotel_Name:</b> Name of Hotel</p>
            <p>👉 <b>Reviewer_Nationality:</b> Nationality of Reviewer</p>
            <p>👉 <b>Negative_Review:</b> Negative Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Negative'</p>
            <p>👉 <b>Review_Total_Negative_Word_Counts:</b> Total number of words in the negative review.</p>
            <p>👉 <b>Positive_Review:</b> Positive Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Positive'</p>
            <p>👉 <b>Review_Total_Positive_Word_Counts:</b> Total number of words in the positive review.</p>
            <p>👉 <b>Reviewer_Score:</b> Score the reviewer has given to the hotel, based on his/her experience</p>
            <p>👉 <b>Total_Number_of_Reviews_Reviewer_Has_Given:</b> Number of Reviews the reviewers has given in the past.</p>
            <p>👉 <b>Total_Number_of_Reviews:</b> Total number of valid reviews the hotel has.</p>
            <p>👉 <b>Tags:</b> Tags reviewer gave the hotel.</p>
            <p>👉 <b>days_since_review:</b> Duration between the review date and scrape date.</p>
            <p>👉 <b>Additional_Number_of_Scoring:</b> Number of valid scores without review.</p>
            <p>👉 <b>lat:</b> Latitude of the hotel</p>
            <p>👉 <b>lng:</b> Longitude of the hotel</p>
        </div>
        """, unsafe_allow_html=True)
        #..................................................
    elif st.session_state.clicked == "reviewers nationality":

        tab_names = [
        "total nationalities distributon", 
        "Top 10 nationalities", 
        "least 10 nationalities", 
        "total reviews distribution", 
        "top written  Reviews",
        "best & least nationality score"]

        # إنشاء 5 Tabs بالأسماء دي
        tab1, tab2, tab3, tab4, tab5 , tab6 = st.tabs(tab_names)

        with tab1:
            st.write("📌 Reviewer Nationalities Treemap")

            #  تحضير DataFrame
            df=pd.read_csv('hotel_review_final.csv')
            df1 = df['reviewer_nationality'].value_counts(ascending=False).reset_index()
            df1.columns = ['reviewer_nationality', 'count']


            fig = px.treemap(
                df1,
                path=['reviewer_nationality'],
                values='count',
                color='count',
                color_continuous_scale='Viridis',
                title='Reviewer Nationalities Treemap'
            )

            # عرض الاسم والقيمة داخل المربعات مع وضوح
            fig.update_traces(
                texttemplate="%{label}<br>%{value}",
                textfont_size=20,
                textfont_color="white"
            )

            # تصميم الشارت
            fig.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white'
            )

            # عرض الشارت داخل Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.write("📌 top 10 nationalites")

            df=pd.read_csv('hotel_review_final.csv')

            df2 = df['reviewer_nationality'].value_counts().head(10).reset_index()
            df2.columns = ['reviewer_nationality', 'count']

            # إنشاء Subplots
            fig1 = make_subplots(
                rows=1, cols=2,
                specs=[[{'type':'domain'}, {'type':'xy'}]],
                subplot_titles=("Top 10 Reviewer Nationalities (Pie)", "Count of Top 10 Reviewers")
            )

            # Pie
            fig1.add_trace(
                go.Pie(
                    labels=df2['reviewer_nationality'],
                    values=df2['count'],
                    name="Pie Chart"
                ),
                row=1, col=1
            )

            # Bar
            fig1.add_trace(
                go.Bar(
                    x=df2['reviewer_nationality'],
                    y=df2['count'],
                    text=df2['count'],
                    textposition='auto',
                    marker_color='lightskyblue'
                ),
                row=1, col=2
            )

            fig1.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                width=1200,
                height=600
            )

            # عرض Subplots في Streamlit
            st.plotly_chart(fig1, use_container_width=True)

        with tab3:
            st.write("📌least 10 nationalities")

            df=pd.read_csv('hotel_review_final.csv')
            df3=df['reviewer_nationality'].value_counts(ascending=True).head(10).T.to_frame().reset_index()
            df3.columns = ['reviewer_nationality' , 'count' ]


            fig2 = make_subplots(
                rows=1, cols=2,
                specs=[[{'type':'domain'}, {'type':'xy'}]],  # pie , bar
                subplot_titles=("Top 10 Reviewer Nationalities (Pie)", "count of top ten reviewers"))
            # Pie
            fig2.add_trace(
                go.Pie(
                    labels=df3['reviewer_nationality'],
                    values=df3['count'],
                    name="Pie Chart"),
                    row=1, col=1)


            # Bar
            fig2.add_trace(
                go.Bar(
                    x=df3['reviewer_nationality'] , 
                    y=df3['count'] ,text=df3['count'],
                    textposition='auto',
                    marker_color='lightskyblue'),
                    row=1, col=2)

            fig2.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                width=1200,
                height=600)

            st.plotly_chart(fig2, use_container_width=True)

        with tab4:
            st.write("📌total reviews distribution")


            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')  # أو 'latin1' لو فيه مشاكل في الترميز

            # Scatter plot
            fig20 = px.scatter(
                df,
                x='reviewer_nationality',
                y='total_number_of_reviews_reviewer_has_given',
                color='total_number_of_reviews_reviewer_has_given',
                size='total_number_of_reviews_reviewer_has_given',
                title="Review Activity by Nationalities",
                height=800
            )

            # عرض الشارت في Streamlit
            st.plotly_chart(fig20, use_container_width=True)

        with tab5:

            st.write("📌top written Reviews")

            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

            df17 = df[['hotel_name', 'total_number_of_reviews', 'additional_number_of_scoring', 'reviewer_nationality']].copy()
            df17['written_reviews'] = df17['total_number_of_reviews'] - df17['additional_number_of_scoring']

            # حذف الأعمدة القديمة
            df17.drop(['total_number_of_reviews', 'additional_number_of_scoring'], axis=1, inplace=True)

            # حساب عدد المراجعين لكل جنسية
            nat_count = (
                df17.groupby('reviewer_nationality')['written_reviews']
                    .count()
                    .sort_values(ascending=False)
                    .head(20)
            )

            # رسم Bar Chart باستخدام Plotly Express
            import plotly.express as px

            fig5 = px.bar(
                x=nat_count.index,
                y=nat_count.values,
                title="Top 20 Nationalities by Number of Reviewers",
                color=nat_count.values,
                color_continuous_scale="Turbo",
                height=600,
                text=nat_count.values
            )

            fig5.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white'
            )

            # عرض الشارت في Streamlit
            st.plotly_chart(fig5, use_container_width=True)
        with tab6:
            st.write("📌Treemap of Average Reviewer Score by Nationality")


            # حساب متوسط تقييم المراجعين لكل جنسية
            df11 = (
                df.groupby('reviewer_nationality')['reviewer_score']
                .mean()
                .to_frame()
                .reset_index()
                .sort_values('reviewer_score', ascending=False)
            )

            # رسم Treemap باستخدام Plotly Express
            import plotly.express as px

            fig6 = px.treemap(
                df11,
                path=['reviewer_nationality'],
                values='reviewer_score',
                color='reviewer_score',
                color_continuous_scale='Viridis',
                title='Treemap of Average Reviewer Score by Nationality'
            )

            # تحسين النصوص واللون للداش بورد الداكن
            fig6.update_traces(texttemplate="%{label}<br>%{value:.2f}", textfont_size=16, textfont_color="white")
            fig6.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')

            # عرض الشارت في Streamlit
            st.plotly_chart(fig6, use_container_width=True)


    #>.................................................................
    elif st.session_state.clicked == "years":


        tab_names = [
        "reviewer_distribution", 
        "reviews_distribution", 
        "top 10 each year"]

        # إنشاء 5 Tabs بالأسماء دي
        tab1, tab2, tab3= st.tabs(tab_names)

        with tab1:

            st.subheader("📊 Total Reviewers Distribution Among Years")

            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')
            df21= df['review_year'].value_counts(ascending=False).head().T.to_frame().reset_index()
            df21.columns = ['review_year' , 'count']


            fig22 = px.bar(df21 , x= 'review_year' , y='count' , color='review_year' , text_auto=True)

            fig22.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                width=600,
                height=600)

            st.plotly_chart(fig22, use_container_width=True)

        with tab2:
            st.subheader("📌 Top reviews numbers distributions")

            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

            reviews_per_year = df.groupby('review_year')['total_number_of_reviews_reviewer_has_given'].sum().reset_index()

            fig30 = px.bar(
                reviews_per_year,
                x='review_year',
                y='total_number_of_reviews_reviewer_has_given',
                title="Total Reviews by Year",
                color='total_number_of_reviews_reviewer_has_given',
                text='total_number_of_reviews_reviewer_has_given',
                color_continuous_scale='Viridis',
                height=500
            )

            # تصميم الشارت للداش بورد الداكن
            fig30.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                xaxis_title="Year",
                yaxis_title="Total Reviews"
            )

            # عرض الشارت في Streamlit
            st.plotly_chart(fig30, use_container_width=True)

        with tab3:
            st.subheader("📌 Top Hotels by Average Reviewer Score per Year")

            # قراءة البيانات
            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

            # حساب متوسط تقييم المراجعين لكل فندق لكل سنة
            avg_score_year = (
                df.groupby(['hotel_name','review_year'])['reviewer_score']
                .mean()
                .reset_index()
                .sort_values(['hotel_name','review_year'])
            )

            # تقسيم البيانات حسب السنة
            df16  = avg_score_year[avg_score_year[ 'review_year'] == 2015].sort_values(by='reviewer_score', ascending=False).head()
            df16.columns = ['hotel_name','review_year','review_score']

            df16_1 = avg_score_year[avg_score_year['review_year'] == 2016].sort_values(by='reviewer_score', ascending=False).head()
            df16_1.columns = ['hotel_name','review_year','review_score']

            df16_2 = avg_score_year[avg_score_year['review_year'] == 2017].sort_values(by='reviewer_score', ascending=False).head()
            df16_2.columns = ['hotel_name','review_year','review_score']

            # عرض DataFrames في Streamlit
            st.write("**Top Hotels 2015**")
            st.dataframe(df16.style.background_gradient(cmap='Blues'))

            st.write("**Top Hotels 2016**")
            st.dataframe(df16_1.style.background_gradient(cmap='Greens'))

            st.write("**Top Hotels 2017**")
            st.dataframe(df16_2.style.background_gradient(cmap='Reds'))

            # رسم الشارت
            fig16 = make_subplots(
                rows=1, cols=3,
                subplot_titles=("2015", "2016", "2017")
            )

            fig16.add_trace(
                go.Bar(
                    x=df16['hotel_name'],
                    y=df16['review_score'],
                    marker=dict(color=df16['review_score'], colorscale='Rainbow'),
                    text=df16['review_score'],
                    textposition='auto'
                ),
                row=1, col=1
            )

            fig16.add_trace(
                go.Bar(
                    x=df16_1['hotel_name'],
                    y=df16_1['review_score'],
                    marker=dict(color=df16_1['review_score'], colorscale='Rainbow'),
                    text=df16_1['review_score'],
                    textposition='auto'
                ),
                row=1, col=2
            )

            fig16.add_trace(
                go.Bar(
                    x=df16_2['hotel_name'],
                    y=df16_2['review_score'],
                    marker=dict(color=df16_2['review_score'], colorscale='Rainbow'),
                    text=df16_2['review_score'],
                    textposition='auto'
                ),
                row=1, col=3
            )

            # تصميم الشارت للداش بورد الداكن
            fig16.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font=dict(color='white'),
                width=1200,
                height=600
            )

            fig16.update_xaxes(tickangle=45)

            # عرض الشارت
            st.plotly_chart(fig16, use_container_width=True)
            #...............................................................................
    #button_names = [
           # "hotels", trip type", "travelers status", "pets_lovers", "best_sea_destinations"
        #]
    elif st.session_state.clicked == "seasons":

        tab_names = [
        "reviewer_distribution", 
        "reviews_distribution", 
        "top 10 each season"]

        # إنشاء 5 Tabs بالأسماء دي
        tab1, tab2, tab3= st.tabs(tab_names)

        with tab1:

            st.subheader("📊 Total Reviewers Distribution Among seasons")

            df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

            order = df['review_season'].value_counts().index

            fig31= px.histogram(df , x='review_season' ,
                        text_auto=True ,
                            color= 'review_season' ,
                            width=600 , height=600 ,
                            category_orders={'review_season': order} )

            st.plotly_chart(fig31, use_container_width=True)

        with tab2:
            st.subheader("📊 Total Number of Reviews Given by Reviewers per Season")

            # تجميع البيانات حسب الموسم
            season_reviews = df.groupby('review_season')['total_number_of_reviews_reviewer_has_given'].sum().reset_index()

            # رسم Bar Chart باستخدام Plotly Express
            fig_season = px.bar(
                season_reviews,
                x='review_season',
                y='total_number_of_reviews_reviewer_has_given',
                text='total_number_of_reviews_reviewer_has_given',
                color='total_number_of_reviews_reviewer_has_given',
                color_continuous_scale='Viridis',
                title="Total Reviews per Season",
                height=500
            )

            # تصميم الشارت للداش بورد الداكن
            fig_season.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                xaxis_title="Season",
                yaxis_title="Total Reviews"
            )

            # عرض الشارت في Streamlit
            st.plotly_chart(fig_season, use_container_width=True)

        with tab3:
            st.subheader("📌 most Hotels reviewed per Season with Average Score")

            # ---- جداول لكل موسم ----
            seasons = ['Summer', 'Winter', 'Autumn', 'Spring']
            df_season_dict = {}

            for season in seasons:
                df_season = df[df['review_season'] == season]
                df_count = df_season['hotel_name'].value_counts(ascending=False).head().reset_index()
                df_count.columns = ['hotel_name', 'count']
                df_count = df_count.merge(df[['hotel_name', 'average_hotel_score']].drop_duplicates(), on='hotel_name')
                df_season_dict[season] = df_count

                st.write(f"**Top Hotels in {season}**")
                st.dataframe(df_count.style.background_gradient(cmap='Blues'))

            # ---- شارت subplot لكل موسم ----
            fig_seasons = make_subplots(
                rows=1, cols=4,
                subplot_titles=seasons
            )

            colorscale = ['Rainbow', 'Rainbow', 'Rainbow', 'Rainbow']

            for i, season in enumerate(seasons):
                df_s = df_season_dict[season]
                fig_seasons.add_trace(
                    go.Bar(
                        x=df_s['hotel_name'],
                        y=df_s['count'],
                        marker=dict(color=df_s['average_hotel_score'], colorscale=colorscale[i]),
                        text=df_s['average_hotel_score'],
                        textposition='auto',
                        name=season
                    ),
                    row=1, col=i+1
                )

            # تصميم الشارت للداش بورد الداكن
            fig_seasons.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font=dict(color='white'),
                width=1400,
                height=500
            )

            fig_seasons.update_xaxes(tickangle=45)

            st.plotly_chart(fig_seasons, use_container_width=True)
        #...............................................................................................
    elif st.session_state.clicked == "hotels":

        df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

        tab_names = [
            "Top 10", 
            "Least 10", 
            "top 10 take score only",
            "Correlation", 
            "Negative & Positive Distribution"
        ]

        tab1, tab2, tab3, tab4,tab5 = st.tabs(tab_names)

        with tab1:
            st.subheader("📌 Top 10 Hotels")

            df8 = (
                df[['average_hotel_score', 'hotel_name']]
                .drop_duplicates()
                .sort_values(by='average_hotel_score', ascending=False)
                .reset_index(drop=True)
                .head(10)
            )

            fig8 = px.bar(
                df8,
                x='hotel_name',
                y='average_hotel_score',
                text='average_hotel_score',
                color='average_hotel_score',
                color_continuous_scale='Viridis',
                title='Top 10 Hotels by Average Score'
            )

            fig8.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                yaxis={'categoryorder': 'total ascending'}
            )

            st.plotly_chart(fig8, use_container_width=True)

        with tab2:
            st.subheader("📌 Least 10 Hotels")

            df8_1 = (
                df[['average_hotel_score', 'hotel_name']]
                .drop_duplicates()
                .sort_values(by='average_hotel_score', ascending=True)
                .reset_index(drop=True)
                .head(10)
            )

            fig33 = px.bar(
                df8_1,
                x='hotel_name',
                y='average_hotel_score',
                text='average_hotel_score',
                color='average_hotel_score',
                color_continuous_scale='Viridis',
                title='Least 10 Hotels by Average Score'
            )

            fig33.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                yaxis={'categoryorder': 'total descending'}
            )

            st.plotly_chart(fig33, use_container_width=True)


        with tab3:
            st.subheader("📌 most 10 hotels get score without written reviews")


            df7 = df[['additional_number_of_scoring', 'hotel_name']].drop_duplicates().sort_values(by='additional_number_of_scoring' , ascending=False).reset_index(drop=True)

            fig7= px.bar(df7.sort_values(by='additional_number_of_scoring' , ascending=False).reset_index().drop('index' , axis=1).head(10) ,
                    x='hotel_name' ,
                    y='additional_number_of_scoring' , 
                    text_auto=True ,
                    color='hotel_name',
                    title='top ten additional scoring number')


            fig7.update_layout(
                plot_bgcolor='black',
                paper_bgcolor='black',
                font_color='white',
                height=900
                )

            st.plotly_chart(fig7, use_container_width=True)

        with tab4:
            st.subheader("📌 Correlation between word counts and reviewer score")

            corr_df = df[['review_total_negative_word_counts',
                        'review_total_positive_word_counts',
                        'reviewer_score']].corr()

            fig34 = px.imshow(
                corr_df,
                text_auto=True,
                title="Correlation Heatmap",
                width=600,
                height=600
            )

            st.plotly_chart(fig34, use_container_width=True)

        with tab5:
            st.subheader("📌 Negative & Positive Words Distribution")

            fig35 = px.scatter(
                df,
                x='review_total_positive_word_counts',
                y='review_total_negative_word_counts',
                size='total_number_of_reviews',
                color='total_number_of_reviews',
                title='Positive vs Negative Word Counts per Hotel',
                hover_data=['hotel_name']
            )

            st.plotly_chart(fig35, use_container_width=True)
    #...........................................................................................

    elif st.session_state.clicked == "trip type":
        st.subheader("📌 number of viewers among each trip types")

        df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')


        fig36=px.histogram(df , x='reviewer_trip_type',
             color='reviewer_trip_type',
             text_auto=True)

        st.plotly_chart(fig36, use_container_width=True)
    #.............................................................................................
    elif st.session_state.clicked == "travelers status":

        st.subheader("📌 top number of viewers ber each trip types")

        df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

        df6 = df['travelers_type'].value_counts().to_frame().reset_index()
        df6.columns = ['travelers_type' , 'count']


        fig5 = make_subplots(
            rows=1, cols=2,
            specs=[[{'type':'domain'}, {'type':'xy'}]],  # pie , bar
            subplot_titles=("top reviewers_trip_type percentage ", "reviewers_trip_type")
        )


        fig5.add_trace(
            go.Pie(
                labels=df6['travelers_type'],
                values=df6['count'],
                name = "pie chart",
            ) , row=1, col=1
            )

        fig5.add_trace(
            go.Bar(
                x=df6['travelers_type'] , 
                y=df6['count'] ,text=df6['count'],
                textposition='auto',
                marker_color='lightskyblue'
            ),
            row=1, col=2
        )

        fig5.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            width=1200,
            height=600
        )

        st.dataframe(df6)
        st.plotly_chart(fig5, use_container_width=True)
    #...........................................................................................
    elif st.session_state.clicked == "pets_lovers":

        st.subheader("📌 top number of viewers ber each trip types")

        df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

        df_filter11=df['pets_allowed'].value_counts().to_frame()



        fig6 = px.histogram(df ,
                     x='pets_allowed',
                       text_auto=True )

        fig6.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            width=500,
            height=600)

        st.dataframe(df_filter11)
        st.plotly_chart(fig6, use_container_width=True)
    #............................................................................................
    elif st.session_state.clicked == "best_destinations":

        df = pd.read_csv('hotel_review_final.csv', encoding='utf-8')

        tab_names = [
            "Top 20", 
            "meditrerranean coast top"]

        tab1, tab2 = st.tabs(tab_names)

        with tab1:
            st.subheader("📌 top 20 hotels destination")

            df15 = df[['hotel_name', 'average_hotel_score', 'hotel_address', 'lat', 'lng']].drop_duplicates()
            top_20 = df15.sort_values(by='average_hotel_score', ascending=False).reset_index(drop=True).head(20)

            # عرض جدول منسق
            st.write("### 📋 Top 20 Hotels Table")
            st.dataframe(
                top_20.style.format({
                    "average_hotel_score": "{:.2f}"
                }).background_gradient(cmap="viridis"),
                use_container_width=True
            )

            # إضافة jitter لمنع تداخل النقاط
            top_20['lat_jitter'] = top_20['lat'] + np.random.uniform(-0.0005, 0.0005, size=len(top_20))
            top_20['lng_jitter'] = top_20['lng'] + np.random.uniform(-0.0005, 0.0005, size=len(top_20))

            # تحديد مركز الخريطة
            center_lat = top_20['lat'].mean()
            center_lon = top_20['lng'].mean()

            # خريطة
            st.write("### 🗺️ Map of Top 20 Hotels")

            fig41= px.scatter_mapbox(
                top_20,
                lat='lat_jitter',
                lon='lng_jitter',
                hover_name='hotel_name',
                hover_data=['hotel_address', 'average_hotel_score'],
                color='average_hotel_score',
                size='average_hotel_score',
                size_max=15,
                zoom=3,
                height=650,
                mapbox_style='carto-positron'
            )
            fig41.update_layout(mapbox_center={"lat": center_lat, "lon": center_lon})

            st.plotly_chart(fig41, use_container_width=True)

        with tab2:
            st.subheader("📌 top 20 hotels destination in meditrerranean coast ""barcelona")

            sea_hotels = df15[
                (df15['lat'] > 41.3) & (df15['lat'] < 41.5) &
                (df15['lng'] > 2.0) & (df15['lng'] < 2.2)
            ]

            # أعلى 10 فنادق
            sea_top10 = (
                sea_hotels.sort_values(by='average_hotel_score', ascending=False)
                .reset_index(drop=True)
                .head(10)
            )

            # عرض الجدول
            st.write("### 📋 Top 10 Sea-Side Hotels Table")
            st.dataframe(
                sea_top10.style.format({"average_hotel_score": "{:.2f}"})
                .background_gradient(cmap="Blues"),
                use_container_width=True
            )

            # jitter علشان نقط الخريطة متبقاش فوق بعض
            sea_top10['lat_jitter'] = sea_top10['lat'] + np.random.uniform(-0.0005, 0.0005, size=len(sea_top10))
            sea_top10['lng_jitter'] = sea_top10['lng'] + np.random.uniform(-0.0005, 0.0005, size=len(sea_top10))

            # مركز الخريطة
            center_lat = sea_top10['lat'].mean()
            center_lon = sea_top10['lng'].mean()

            # الرسم على الخريطة
            fig50 = px.scatter_mapbox(
                sea_top10,
                lat='lat_jitter',
                lon='lng_jitter',
                hover_name='hotel_name',
                hover_data=['hotel_address', 'average_hotel_score'],
                color='average_hotel_score',
                size='average_hotel_score',
                size_max=15,
                zoom=12,
                height=650,
                mapbox_style='carto-positron'
            )

            fig50.update_layout(
                mapbox_center={"lat": center_lat, "lon": center_lon}
            )

            # عرض الخريطة
            st.plotly_chart(fig50, use_container_width=True)

